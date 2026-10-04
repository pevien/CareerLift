# Điều khiển Chrome headless qua DevTools Protocol, chỉ dùng thư viện chuẩn của Python.
# Dùng khi trang cần chờ việc bất đồng bộ (tải thư viện từ CDN, AI giả lập...) mà --dump-dom sẽ cắt ngang.
# Dùng: python3 tests/cdp.py URL "biểu thức JS trả về chuỗi khi xong, hoặc rỗng khi chưa xong" [giây chờ tối đa]
import base64, json, os, socket, struct, subprocess, sys, tempfile, time, urllib.request

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

class WS:
    def __init__(self, url):
        host, path = url[len("ws://"):].split("/", 1)
        h, p = host.split(":")
        self.s = socket.create_connection((h, int(p)))
        key = base64.b64encode(os.urandom(16)).decode()
        self.s.sendall(f"GET /{path} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
        buf = b""
        while b"\r\n\r\n" not in buf: buf += self.s.recv(4096)
        self.rest = buf.split(b"\r\n\r\n", 1)[1]
    def _read(self, n):
        while len(self.rest) < n: self.rest += self.s.recv(65536)
        d, self.rest = self.rest[:n], self.rest[n:]
        return d
    def send(self, obj):
        data = json.dumps(obj).encode(); mask = os.urandom(4); n = len(data)
        head = bytes([0x81]) + (bytes([0x80 | n]) if n < 126 else bytes([0x80 | 126]) + struct.pack(">H", n) if n < 65536 else bytes([0x80 | 127]) + struct.pack(">Q", n))
        self.s.sendall(head + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))
    def recv(self):
        msg = b""
        while True:
            b1, b2 = self._read(2); n = b2 & 0x7F
            if n == 126: n = struct.unpack(">H", self._read(2))[0]
            elif n == 127: n = struct.unpack(">Q", self._read(8))[0]
            msg += self._read(n)
            if b1 & 0x80: return json.loads(msg)

def run(url, done_expr, timeout=60):
    prof = tempfile.mkdtemp(); port = 9300 + os.getpid() % 500
    p = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--user-data-dir=" + prof,
                          "--allow-file-access-from-files", f"--remote-debugging-port={port}", "about:blank"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    try:
        for _ in range(100):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json")); break
            except Exception: time.sleep(0.1)
        ws = WS([t for t in tabs if t["type"] == "page"][0]["webSocketDebuggerUrl"])
        mid = [0]
        def call(method, params=None):
            mid[0] += 1; ws.send({"id": mid[0], "method": method, "params": params or {}})
            while True:
                m = ws.recv()
                if m.get("id") == mid[0]: return m.get("result", {})
        call("Page.navigate", {"url": url})
        end = time.time() + timeout
        while time.time() < end:
            r = call("Runtime.evaluate", {"expression": done_expr, "returnByValue": True})
            v = r.get("result", {}).get("value")
            if v: return v
            time.sleep(0.5)
        return "TIMEOUT"
    finally:
        try: os.killpg(p.pid, 9)
        except Exception: pass

if __name__ == "__main__":
    print(run(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 60))
