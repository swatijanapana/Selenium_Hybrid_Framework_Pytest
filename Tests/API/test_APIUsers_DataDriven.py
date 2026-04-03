import pytest
from Utilities.api_client import APIClient
from Utilities.excel_reader import get_api_test_data


class Test_APIUsers_DataDriven:

    @pytest.mark.parametrize("test_data", get_api_test_data())
    def test_api_users_data_driven(self, test_data):

            api_client = APIClient()

            method = test_data["Method"]
            url = str(test_data["URL"]).strip()
            expected_status = int(test_data["Expected_Status"])
            payload = {"name": test_data["Name"],
                       "email": test_data["Email"]
                       }
            print(test_data)
            if method == "GET":
                response = api_client.get(url)
            elif method == "POST":
                response = api_client.post(url,payload)
            elif method == "PUT":
                response = api_client.put(url,payload)
            elif method == "DELETE":
                response = api_client.delete(url)
            elif method == "PATCH":
                pytest.fail(f"Unsupported method: {method}")

            assert response.status_code == expected_status



