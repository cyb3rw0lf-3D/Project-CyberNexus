# Raiden

> **Status:** scaffold. The purpose of this project hasn't been decided yet. Replace this
> paragraph with a one-line description once it has.

## Requirements

- Python 3.10 or newer

## Setup

```bash
cd Raiden
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
raiden              # prints a greeting
raiden --version    # prints the version
python -m raiden    # same as `raiden`
```

## Test

```bash
pytest
```

## Layout

```
Raiden/
├── pyproject.toml      # package metadata and build config
├── src/raiden/         # package source
│   ├── __init__.py     # version
│   ├── __main__.py     # `python -m raiden`
│   └── cli.py          # command-line entry point
└── tests/              # pytest suite
```

CI runs the tests on every push and pull request that touches `Raiden/`
(see `.github/workflows/raiden-ci.yml` at the repository root).

## License

Apache License 2.0, the same as the rest of this repository. See [`LICENSE`](../LICENSE).
