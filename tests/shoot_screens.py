# Chụp lại ảnh cho docs/SCREENS.md bằng Chrome headless. Cần chạy app trước: sh serve.sh
# Dùng: python3 tests/shoot_screens.py [state1,state2,...]   (mặc định: tất cả màn hình trong tests/screens.html)
#       python3 tests/shoot_screens.py --check                 (regression: chỉ mở từng màn hình, báo lỗi JS hoặc trang trống, không chụp)
import os, re, subprocess, sys, tempfile, urllib.parse
from concurrent.futures import ThreadPoolExecutor

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get("APP_URL", "http://localhost:8000") + "/tests/screens.html"
OUT = os.path.join(ROOT, "docs", "screens")
ALL = re.findall(r'^  "([a-z]\d\d[a-z]?-[a-z0-9-]+)":', open(os.path.join(ROOT, "tests", "screens.html"), encoding="utf-8").read(), re.M)
CHECK = "--check" in sys.argv
args = [a for a in sys.argv[1:] if a != "--check"]
states = args[0].split(",") if args else ALL
os.makedirs(OUT, exist_ok=True)

def run(args, timeout):
    fd, path = tempfile.mkstemp()
    p = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
                          "--user-data-dir=" + tempfile.mkdtemp()] + args,
                         stdout=fd, stderr=subprocess.DEVNULL, start_new_session=True)
    try: p.wait(timeout=timeout)
    except subprocess.TimeoutExpired: pass
    try: os.killpg(p.pid, 9)
    except Exception: pass
    os.close(fd)
    return open(path, encoding="utf-8", errors="ignore").read()

def shoot(job):
    state, kind = job
    w, scale, winw = (1280, 1, 1280) if kind == "desktop" else (390, 2, 600)
    url = BASE + "#" + urllib.parse.quote(f"{state}|{w}")
    dom = run(["--window-size=%d,1000" % winw, "--virtual-time-budget=4000", "--dump-dom", url], 12)
    m = re.search(r"<title>(.*?)</title>", dom)
    t = m.group(1) if m else "?"
    if not t.startswith("H="): return f"{state} {kind}: FAIL {t}"
    h = int(t[2:])
    if CHECK: return f"{state} {kind}: ok"
    png = os.path.join(OUT, f"{state}-{kind}.png")
    run(["--window-size=%d,%d" % (winw, h), "--force-device-scale-factor=%d" % scale, "--virtual-time-budget=4000",
         "--screenshot=" + png, url], 12)
    if kind == "mobile":
        subprocess.run(["sips", "-c", str(h * scale), str(w * scale), png], capture_output=True)
    return f"{state} {kind}: {h}px"

jobs = [(s, k) for s in states for k in ("desktop", "mobile")]
failed = 0
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(shoot, jobs):
        print(r, flush=True); failed += "FAIL" in r
print(f"{len(jobs) - failed}/{len(jobs)} passed")
sys.exit(1 if failed else 0)
