
from pytest_httpserver import HTTPServer
from external.client import UserClient

def test_fetch_user_from_external_api(httpserver: HTTPServer):
    httpserver.expect_request("/users/1").respond_with_json(
        {"id": 1, "first": "Ada", "last": "Lovelace"}, status=200
    )
    client = UserClient(httpserver.url_for(""))
    user = client.fetch_user(1)

    assert user is not None
    assert user["id"] == 1
    assert user["first"] == "Ada"
    assert user["last"] == "Lovelace"

def test_returns_none_on_404(httpserver: HTTPServer):
    httpserver.expect_request("/users/999").respond_with_data(status=404)
    client = UserClient(httpserver.url_for(""))
    assert client.fetch_user(999) is None

def test_returns_none_when_first_or_last_is_missing(httpserver: HTTPServer):
    httpserver.expect_oneshot_request("/users/2").respond_with_json(
        {"id": 2, "last": "Lovelace"}, status=200
    )
    httpserver.expect_oneshot_request("/users/3").respond_with_json(
        {"id": 3, "first": "Ada"}, status=200
    )
    client = UserClient(httpserver.url_for(""))

    assert client.fetch_user(2) is None
    assert client.fetch_user(3) is None

def test_user_id_5_returns_none_when_required_field_is_missing(httpserver: HTTPServer):
    httpserver.expect_request("/users/5").respond_with_json(
        {"id": 5, "first": "Ada"}, status=200
    )
    client = UserClient(httpserver.url_for(""))

    assert client.fetch_user(5) is None
