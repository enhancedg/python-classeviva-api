#
# Code by Francesco Pallara
#

from classeviva_request import classeviva_request as cvv_r
from endpoints import *
import re
from exceptions.ClasseVivaException import ClasseVivaException

class User:
    __attrs__ = [
        "user_id",
        "first_name",
        "last_name",
        "token",
        "release",
        "expire"
    ]

    def __init__(self, credentials: dict):

        """
          ? init method for generic user
          
            @param credentials: dictionary with credentials needed for auth, example:
                              * {"ident": null, "pass": "<password>", "uid": "<user_id>"}
        """

        user = self.auth(credentials)

        self.user_id = re.sub(r"\D", "", user['ident'])
        self.first_name = user['firstName']
        self.last_name = user['lastName']

        self.token = user['token']

        self.release = user["release"]
        self.expire = user["expire"]

    def auth(self, credentials: str) ->dict:

        """
         ?  Authenticate the user on classeviva

            @param credentials: dictionary with credentials needed for auth, example:
                              * {"ident": null, "pass": "<password>", "uid": "<user_id>"}

         *  Returns a dictionary with token and expiration date of the session:
            @attr user_id: user id
            @attr first_name: user first name
            @attr last_name: user last name
            @attr token: token needed for using the API
            @attr release: release date of the token
            @attr expire: expiration date of the token 
                        * expiration time = release time + 1h 30m
        """

        request = cvv_r.post_json(auth_endpoint, credentials) # authentication
        if request.status_code == 200: # Success!
            user = request.json()
        else:
            raise ClasseVivaException(request.json()['message'], request.status_code)

        return user

    def get(self, uri: str) -> dict:

        """
          ? GET request to classeviva API as a generic user

            @param uri: no description needed

          * Returns the json result of the request as a dictionary
        """

        request = cvv_r.get_json(uri, user_id=self.user_id, token=self.token)

        return request.json()
