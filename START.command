#!/bin/bash
set -e
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
cd "$(dirname "$0")"

echo "SONO VIDZ TRSC"
echo "Starting local machine..."

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
else
  source .venv/bin/activate
fi

OLD_PID=$(lsof -ti tcp:8777 2>/dev/null || true)
if [ -n "$OLD_PID" ]; then
  kill $OLD_PID 2>/dev/null || true
  sleep 1
fi

python app.py &
SERVER_PID=$!

cleanup() { kill "$SERVER_PID" 2>/dev/null || true; }
trap cleanup EXIT INT TERM

sleep 4
open "http://127.0.0.1:8777/"
wait "$SERVER_PID"
