import pytest
from app import app

def test_invalid_method():
    #Test for an invalid request method
    with app.test_client() as client:
        response = client.post('/')  
        assert response.status_code == 405
