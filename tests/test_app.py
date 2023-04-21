from app import greet


def test_application():
    assert greet() == "Hello World"
