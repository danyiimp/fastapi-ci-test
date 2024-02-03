from fastapi.testclient import TestClient
from ci_test.main import app
from ci_test.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}
