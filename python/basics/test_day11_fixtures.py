
import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def expected_status():
    return 200


def test_get_user(base_url, expected_status):
    response = requests.get(f"{base_url}/users/1", timeout=10)

    assert response.status_code == expected_status
    assert response.json()["id"] == 1


def test_get_posts(base_url, expected_status):
    response = requests.get(f"{base_url}/posts/1", timeout=10)

    assert response.status_code == expected_status
    assert response.json()["id"] == 1


def test_get_missing_user(base_url):
    response = requests.get(f"{base_url}/users/9999", timeout=10)

    assert response.status_code == 404
