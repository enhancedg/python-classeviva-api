#
# Code by Francesco Pallara
#

from requests import post, get, Response
from endpoints import base_url

class classeviva_request:

    @staticmethod
    def get_headers(token="") -> dict:

        """
          ? Get headers for request
            @param token: needed for talking to classeviva API, use auth request to get it
          * Without headers, the request will fail
        """

        headers = {"User-Agent": "zorro/1.0", "Z-Dev-Apikey": "+zorro+"}
        if token != "":
            auth_token = {"Z-Auth-Token": token}
            headers.update(auth_token)

        return headers

    @staticmethod
    def post_json(end_point: str, data: dict, token="", user_id="") -> Response:
        
        """ 
          ? Sends a POST request to classeviva API

            @param end_point: Endpoint for the API, see endpoints.py
            @param data: Data to use for the post request, it has to be a dictionary
        """

        headers = classeviva_request.get_headers(token=token)
        
        if user_id != "":
            end_point %= (user_id)

        r = post(base_url + end_point, json=data, headers=headers)
        
        return r

    @staticmethod
    def get_json(end_point: str, token="", user_id="") -> Response:
        
        """ 
          ? Sends a GET request to classeviva API

            @param end_point: Endpoint for the API, see endpoints.py
            @param kwargs: Additional arguments, like token and student id
        """

        headers = classeviva_request.get_headers(token=token)

        if user_id != "":
            end_point %= (user_id)

        r = get(base_url + end_point, headers=headers)
        
        return r
        