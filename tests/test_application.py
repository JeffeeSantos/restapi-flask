import pytest
import uuid
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Jefferson",
            "last_name": "Santos",
            "cpf": "529.982.247-25",
            "email": "papa@gmail.com",
            "birth_date": "1991-04-10"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Jefferson",
            "last_name": "Santos",
            "cpf": "529.982.247-28",
            "email": "papa@gmail.com",
            "birth_date": "1991-04-10"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200

        response = client.post('/user', json=valid_user)
        assert response.status_code == 400

    def test_get_user(self, client, valid_user, invalid_user):
        client.post('/user', json=valid_user)

        response = client.get(f'/user/{valid_user["cpf"]}')
        assert response.status_code == 200

        response = client.get(f'/user/{invalid_user["cpf"]}')
        assert response.status_code == 400