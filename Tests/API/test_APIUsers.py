import pytest
from Utilities.api_client import APIClient

@pytest.mark.api
class Test_APIUsers:

    def setup_method(self):
        self.api_client = APIClient()

    def test_get_users_list(self):
        """Verify users API returns 200 and valid data."""

        url = "https://jsonplaceholder.typicode.com/users"

        response = self.api_client.get(url)
        assert response.status_code == 200
        response_json = response.json()

        assert len(response_json) > 0
        assert "id" in response_json[0]
        assert "email" in response_json[0]

    @pytest.mark.smoke
    def test_create_user(self):
        """ Verify user can be created through POST API. """

        url = "https://jsonplaceholder.typicode.com/users"

        payload = {"name": "Test", "email": "api@test.com"}

        response = self.api_client.post(url, payload)
        assert response.status_code == 201
        response_json = response.json()
        assert response_json["name"] == "Test"
        assert response_json["email"] == "api@test.com"



    def test_create_user_with_missing_fields(self):
        """ Verify API behaviour when required fields are missing. """

        url = "https://jsonplaceholder.typicode.com/users"

        payload = {"name": ""} # missing email
        response = self.api_client.post(url, payload)
        # API still returns 201 (fake API behavior)
        assert response.status_code == 201
        response_json = response.json()
        assert "email" not in response_json or response_json.get("email") in [None, ""]



    def test_invalid_endpoint(self):
        """ Verify users API returns 404. """

        url = "https://jsonplaceholder.typicode.com/invalid"

        response = self.api_client.get(url)
        assert response.status_code == 404


    def test_update_user(self):
        """Verify user data can be updated using PUT API. """

        url = "https://jsonplaceholder.typicode.com/users/1"

        payload = {"name": "Updated Test", "email": "updated_api@test.com"}

        response = self.api_client.put(url, payload)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["name"] == "Updated Test"
        assert response_json["email"] == "updated_api@test.com"

    def test_delete_user(self):
        """Verify user can be deleted using DELETE API."""

        url = "https://jsonplaceholder.typicode.com/users/1"

        response = self.api_client.delete(url)
        assert response.status_code == 200


    def test_unsupported_method(self):
        """ Verify framework fails for unsupported HTTP method. """

        api_client = APIClient()

        method = "PATCH"
        url = "https://jsonplaceholder.typicode.com/users"
        payload = {"name": "Updated Test", "email": "updated_api@test.com"}

        if method == "GET":
            response = api_client.get(url)
        elif method == "POST":
            response = api_client.post(url, payload)
        elif method == "PUT":
            response = api_client.put(url, payload)
        elif method == "DELETE":
            response = api_client.delete(url)
        else:
            print(f"Unsupported method: {method}")
            with pytest.raises(pytest.fail.Exception):
             pytest.fail(f"Unsupported method: {method}")

