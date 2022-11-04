"""
Doc String
"""
from flask.testing import FlaskClient
from _pytest.fixtures import fixture
from main import app


@fixture
def client() -> FlaskClient:
    """
    Doc String
    """
    app.config.update(SERVER_NAME="myserver.org")
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
