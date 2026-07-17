from dash import dcc

from app import create_app


def test_app_renders():
    app = create_app()
    assert app is not None
    assert app.layout is not None


def test_region_selector_is_present():
    app = create_app()
    found = False

    def walk(node):
        nonlocal found
        if isinstance(node, dcc.RadioItems):
            found = found or getattr(node, "id", None) == "region-radio"
        if isinstance(node, (list, tuple)):
            for child in node:
                walk(child)
        elif hasattr(node, "children"):
            walk(node.children)

    walk(app.layout)
    assert found
