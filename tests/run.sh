#!/bin/sh
# Chạy unit test bằng Chrome headless (điều khiển qua DevTools để chờ được các test bất đồng bộ). Dùng: sh tests/run.sh
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$(python3 "$DIR/cdp.py" "file://$DIR/unit.html" 'document.title.startsWith("RESULT") ? [...document.querySelectorAll("#list li")].map(li => li.innerText).join("\n") + "\n" + document.title : ""' 120)"
# In từng test (✓ / ✗) và dòng tổng kết
echo "$OUT"
case "$OUT" in *"RESULT: "*" 0 failed"*) exit 0;; TIMEOUT) echo "RESULT: no output (Chrome không chạy được trang test)"; exit 1;; *) exit 1;; esac
