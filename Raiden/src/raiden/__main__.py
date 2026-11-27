"""Allow running the package with ``python -m raiden``."""

from raiden.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
