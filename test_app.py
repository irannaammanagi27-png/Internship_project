from app import create_app


def test_app_renders():
    app = create_app()
    assert app is not None
    assert app.layout is not None
