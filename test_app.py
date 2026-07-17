import pytest
from dash import dcc

import app as dash_app


@pytest.fixture
def client():
    return dash_app.app.server.test_client()


def test_header_is_present(client):
    response = client.get("/")
    assert response.status_code == 200
    layout = dash_app.app.layout
    assert _contains_text(layout, "Pink Morsel Sales Visualiser")


def test_visualisation_is_present(client):
    response = client.get("/")
    assert response.status_code == 200
    layout = dash_app.app.layout
    assert _contains_component(layout, dcc.Graph, "sales-chart")


def test_region_picker_is_present(client):
    response = client.get("/")
    assert response.status_code == 200
    layout = dash_app.app.layout
    assert _contains_text(layout, "Filter by region")
    assert _contains_component(layout, dcc.RadioItems, "region-radio")


def _contains_text(node, text):
    if isinstance(node, str):
        return text in node
    if isinstance(node, (list, tuple)):
        return any(_contains_text(child, text) for child in node)
    if hasattr(node, "children") and node.children is not None:
        return _contains_text(node.children, text)
    return False


def _contains_component(node, component_type, component_id):
    if isinstance(node, component_type):
        return getattr(node, "id", None) == component_id
    if isinstance(node, (list, tuple)):
        return any(_contains_component(child, component_type, component_id) for child in node)
    if hasattr(node, "children") and node.children is not None:
        return _contains_component(node.children, component_type, component_id)
    return False
