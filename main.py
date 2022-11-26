#
# Code by Francesco Pallara
# Started: 25/11/2022
#  

from classeviva_request import classeviva_request as cvv_r
import json
from endpoints import *
from student import Student

#? TEMPORANEA
def read_json_file(file_name: str) -> dict:
    with open(file_name, 'r') as infile:
        result = json.loads(infile.read())

    return result

def main():
    login_dict = read_json_file("credenziali.json")
    print(login_dict)
    user = Student(login_dict)

    print(f"Autenticato come {user.first_name} {user.last_name}!")
    print(user.get_card())

if __name__ == "__main__":
    main()