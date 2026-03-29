from onetoast import hello


def test_hello_default() -> None:
    assert hello() == "Hello, world!"


def test_hello_name() -> None:
    assert hello("pip") == "Hello, pip!"
