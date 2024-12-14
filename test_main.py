import pytest
from main import app, greet_user, calculate_sum

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_greet_user():
    # Teste die Funktion greet_user
    result = greet_user("John")
    assert result == "Hello, John! Welcome to the Flask app!"

def test_calculate_sum():
    # Teste die Funktion calculate_sum
    result = calculate_sum(2, 3)
    assert result == 5

def test_home_page(client):
    # Teste die Startseite
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Simple Flask Application" in response.data

def test_greet(client):
    # Teste die /greet Route
    response = client.post('/greet', data={'name': 'John'})
    assert response.status_code == 200
    assert b"Hello, John! Welcome to the Flask app!" in response.data

def test_sum(client):
    # Teste die /sum Route
    response = client.post('/sum', data={'num1': 2, 'num2': 3})
    assert response.status_code == 200
    assert b"The sum is: 5" in response.data
