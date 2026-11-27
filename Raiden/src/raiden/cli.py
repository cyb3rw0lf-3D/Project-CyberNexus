"""Command-line entry point for Raiden."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from raiden import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="raiden",
        description="Raiden: project scaffold (purpose to be decided).",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    build_parser().parse_args(argv)
    print(f"Raiden v{__version__} - hello")
    return 0
