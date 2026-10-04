#!/bin/sh
# Mở app qua http://localhost:8000 (cần cho Google Drive sync và cài app PWA). Dùng: sh serve.sh [port]
cd "$(dirname "$0")" && exec ruby -run -e httpd . -p "${1:-8000}"
