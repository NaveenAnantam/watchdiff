from .core import watch
import argparse

def main():
    p = argparse.ArgumentParser(prog="watchdiff", description="Watch a file and print line-level diffs as it changes.")
    p.add_argument("file")
    p.add_argument("--interval", "-i", type=float, default=1.0)
    p.add_argument("--once", action="store_true", help="print diff vs saved baseline and exit")
    a = p.parse_args()
    watch(a.file, a.interval, a.once)

if __name__ == "__main__":
    main()
