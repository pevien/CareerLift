#!/bin/sh
# Chạy unit test bằng Chrome headless. Dùng: sh tests/run.sh
DIR="$(cd "$(dirname "$0")" && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
PROFILE="$(mktemp -d)"
OUT="$PROFILE/dom.html"
"$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir="$PROFILE" \
  --allow-file-access-from-files --timeout=8000 --dump-dom "file://$DIR/unit.html" > "$OUT" 2>/dev/null &
PID=$!
( sleep 40; kill $PID 2>/dev/null ) &
wait $PID
# In từng test (✓ / ✗) và dòng tổng kết
perl -0ne 'while(/<li class="(?:pass|fail)">(.*?)<\/li>/gs){ my $t = $1; $t =~ s/<pre>/\n    /; $t =~ s/<[^>]*>//g; $t =~ s/&lt;/</g; $t =~ s/&gt;/>/g; $t =~ s/&amp;/&/g; print "$t\n"; }' "$OUT"
RESULT="$(grep -o 'RESULT: [^<]*' "$OUT" | head -1)"
rm -rf "$PROFILE"
echo "${RESULT:-RESULT: no output (Chrome không chạy được trang test)}"
case "$RESULT" in *" 0 failed"*) exit 0;; *) exit 1;; esac
