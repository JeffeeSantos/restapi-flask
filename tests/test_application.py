import pytest
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
            "last_name": "Robert",
            "cpf": "121.393.604-78",
            "email": "contato@liso.com.br",
            "birth_date": "1978-01-11"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Jefferson",
            "last_name": "Santos",
            "cpf": "631.395.302-67",
            "email": "papa@gmail.com",
            "birth_date": "1991-04-10"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Jefferson"
        assert response.json[0]["last_name"] == "Santos"
        assert response.json[0]["cpf"] == "631.395.302-67"
        assert response.json[0]["email"] == "papa@gmail.com"

        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "1991-04-10T00:00:00Z"

        response = client.get('/user/%s' % invalid_user["cpf"])
        assert response.status_code == 400
        assert b"User does not exist in database!" in response.data
