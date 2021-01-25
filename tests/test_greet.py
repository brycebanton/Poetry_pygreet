from greet.location import greet

def test_greet():
    result = greet("America/New_York")
    assert "New York!" in result


from greet.location import cli

def test_greet_cli(capsys):
    args = ["America/Argentina/San_Juan"]
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "San Juan!" in result

import subprocess

def test_greet_cli2():
    result = subprocess.run(["greet", "America/Costa_Rica"], capture_output=True)
    assert b"Costa Rica!" in result.stdout