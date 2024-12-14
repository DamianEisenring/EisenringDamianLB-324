import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_database_interaction(client):
    # Simuliere eine POST-Anfrage, um einen Eintrag hinzuzufügen
    response = client.post('/add', data={'name': 'Test Item'})
    assert response.status_code == 200
    assert b'Item added' in response.data
