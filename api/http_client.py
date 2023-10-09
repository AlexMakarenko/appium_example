"""Http client class"""


import logging
import requests


log = logging.getLogger()
TIMEOUT = 60  # seconds


class HttpClient:
    """Http client to perform requests"""

    def _post_request(self, url: str, headers: dict, data: dict):
        """Post HTTP request

        Args:
            url (str): requests url
            headers (dict): request headers
            data (dict): request body

        Returns:
            _type_: _description_
        """
        log.info(
            "\n * POST    *: %s \n * HEADERS *: %s \n * PAYLOAD *: %s",
            url,
            headers,
            data,
        )
        req = requests.request("POST", url, headers=headers, data=data, timeout=TIMEOUT)
        log.info("\n ** RESPONSE *: %s %s", req.status_code, req.content)
        return req

    def _get_request(self, url: str, headers: dict = None, data: dict = None):
        """Get HTTP request

        Args:
            url (str): _description_
            headers (dict, optional): _description_. Defaults to None.
            data (dict, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        log.info(
            "\n * GET     *: %s \n * HEADERS *: %s \n * PAYLOAD *: %s",
            url,
            headers,
            data,
        )
        req = requests.request("GET", url, headers=headers, data=data, timeout=TIMEOUT)
        log.info("\n ** RESPONSE *: %s %s", req.status_code, req.content)
        return req

    def _delete_request(self, url: str, headers: dict, data: dict = None):
        """Delete HTTP request

        Args:
            url (str): _description_
            headers (dict): _description_
            data (dict, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        log.info(
            "\n * DELETE  *: %s \n * HEADERS *: %s \n * PAYLOAD *: %s",
            url,
            headers,
            data,
        )
        req = requests.delete(url=url, headers=headers, timeout=TIMEOUT)
        log.info("\n ** RESPONSE *: %s %s", req.status_code, req.content)
        return req

    def _put_request(self, url: str, headers: dict, data: dict):
        """Put HTTP Request

        Args:
            url (str): _description_
            headers (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        log.info(
            "\n * PUT     *: %s \n * HEADERS *: %s \n * PAYLOAD *: %s",
            url,
            headers,
            data,
        )
        req = requests.request("PUT", url, headers=headers, data=data, timeout=TIMEOUT)
        log.info("\n ** RESPONSE *: %s %s", req.status_code, req.content)
        return req

    def _patch_request(self, url: str, headers: dict, data: dict):
        """Patch HTTP Request

        Args:
            url (str): _description_
            headers (dict): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        log.info(
            "\n * Patch   *: %s \n * HEADERS *: %s \n * PAYLOAD *: %s",
            url,
            headers,
            data,
        )
        req = requests.request(
            "PATCH", url, headers=headers, data=data, timeout=TIMEOUT
        )
        log.info("\n ** RESPONSE *: %s %s", req.status_code, req.content)
        return req
