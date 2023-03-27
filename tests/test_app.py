from app import greet


def test_app():
    assert greet() == "Hello World"
