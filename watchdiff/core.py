"""watchdiff: minimal file watcher with line-level diff output."""
import os, sys, time, difflib

def _snapshot(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()

def diff_lines(old, new, path):
    d = list(difflib.unified_diff(old, new, fromfile=f"{path} (old)", tofile=f"{path} (new)"))
    return "".join(d)

def watch(path, interval=1.0, once=False):
    old = _snapshot(path)
    if once:
        out = diff_lines([], old, path)
        sys.stdout.write(out)
        return
    print(f"watching {path} every {interval}s (Ctrl+C to stop)", file=sys.stderr)
    try:
        while True:
            time.sleep(interval)
            new = _snapshot(path)
            if new != old:
                sys.stdout.write(diff_lines(old, new, path))
                sys.stdout.flush()
                old = new
    except KeyboardInterrupt:
        pass
