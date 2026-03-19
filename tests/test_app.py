import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    # Arrange: (Setup any required state, already done by importing app and client)

    # Act: Make a GET request to the root endpoint
    response = client.get("/")

    # Assert: Check the response status and content
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text
    assert "<html" in response.text
