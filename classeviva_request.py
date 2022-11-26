#
# Code by Francesco Pallara
#

from requests import post, get, Response
from endpoints import base_url

class classeviva_request:
    @staticmethod
    def post_json(end_point: str, data: dict, **kwargs) -> Response:
        
        """ 
          ? Sends a POST request to classeviva API

            @param end_point: Endpoint for the API, see endpoints.py
            @param data: Data to use for the post request, it has to be a dictionary
            @param kwargs: Additional arguments, like token and student id
        """

        #* Without headers, the request will fail
        headers = {"User-Agent": "zorro/1.0", "Z-Dev-Apikey": "+zorro+"}
        if 'token' in kwargs and 'user_id' in kwargs:
            auth_token = {"Z-Auth-Token": kwargs["token"]}
            headers.update(auth_token)
            end_point % (kwargs['user_id'])
        r = post(base_url + end_point, json=data, headers=headers)
        
        return r

    @staticmethod
    def get_json(end_point: str, **kwargs) -> Response:
        
        """ 
          ? Sends a POST request to classeviva API

            @param end_point: Endpoint for the API, see endpoints.py
            @param kwargs: Additional arguments, like token and student id
        """

        #! Without headers, the request will fail
        headers = {"User-Agent": "zorro/1.0", "Z-Dev-Apikey": "+zorro+"}

        if 'token' in kwargs and 'user_id' in kwargs:
            auth_token = {"Z-Auth-Token": kwargs["token"]}
            headers.update(auth_token)
            end_point %= kwargs['user_id']

        r = get(base_url + end_point, headers=headers)
        
        return r