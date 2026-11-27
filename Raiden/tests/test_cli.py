import pytest

from raiden import __version__
from raiden.cli import main


def test_main_returns_zero_and_greets(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out
    assert "Raiden" in out
    assert __version__ in out


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert __version__ in capsys.readouterr().out
