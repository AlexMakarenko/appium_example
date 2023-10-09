import logging
import allure
import json

from api.http_client import HttpClient
from api.json_objects import User


# log = logging.getLogger()
class UserException(Exception):
    """Custom User exception

    Args:
        Exception (class): inheritance
    """

    def __init__(self, message, status_code=406):
        super().__init__(message)
        self.status_code = status_code


class UserApi(HttpClient):
    __BASE_URL = "https://gorest.co.in"
    __AT = "ef2ac2b9148d34730a26e72e80a7bd5d01103a117fce660b7302edb4a58c1a4b"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {__AT}",
    }

    @allure.step("POST /public/v2/users")
    def create_user(self, payload: dict):
        """Create a user
        Args:
            payload (dict): '{
                "name":"Tenali Ramakrishna",
                "gender":"male",
                "email":"tenali.ramakrishna@15ce.com",
                "status":"active"
                }'
        Returns:
            object: User
        """
        api_url = f"{self.__BASE_URL}/public/v2/users"
        response = self._post_request(
            url=api_url, headers=self.headers, data=json.dumps(payload)
        )
        if response.status_code != 201:
            raise UserException(
                f"Create user error: {response.status_code} {response.text}",
                response.status_code,
            )
        return User(response.json())

    @allure.step("GET /public/v2/users")
    def get_users(self, user_id: int = None):
        """Lists all users

        Returns:
            [object]: User
        """
        api_url = f"{self.__BASE_URL}/public/v2/users"
        if user_id:
            api_url = f"{self.__BASE_URL}/public/v2/users/{user_id}"
        response = self._get_request(url=api_url, headers=self.headers)
        if response.status_code != 200:
            raise UserException(
                f"Get users error: {response.status_code} {response.text}",
                response.status_code,
            )
        json_response = response.json()
        return (
            map(User, json_response)
            if isinstance(json_response, list)
            else User(json_response)
        )

    @allure.step("PATCH /public/v2/users/[user_id]")
    def update_user(self, user_id: int, payload: dict):
        """Updates a user

        Args:
            user_id (int): _description_
            payload (dict): _description_

        Returns:
            object: User
        """
        api_url = f"{self.__BASE_URL}/public/v2/users/{user_id}"
        response = self._patch_request(
            url=api_url, headers=self.headers, data=json.dumps(payload)
        )
        if response.status_code != 200:
            raise UserException(
                f"Update user error: {response.status_code} {response.text}",
                response.status_code,
            )
        return User(response.json())

    @allure.step("DELETE /public/v2/users/[user_id]")
    def delete_user(self, user_id: int):
        """Deletes a user

        Args:
            user_id (int): _description_

        Returns:
            object: Request
        """
        api_url = f"{self.__BASE_URL}/public/v2/users/{user_id}"
        response = self._delete_request(url=api_url, headers=self.headers)
        if response.status_code != 204:
            raise UserException(
                f"Delete user error: {response.status_code} {response.text}",
                response.status_code,
            )
