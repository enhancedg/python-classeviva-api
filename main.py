#
# Code by Francesco Pallara
# Started: 25/11/2022
#  

import json
from student import Student
from datetime import date

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
    
    bacheca = user.get_noticeboard()

    print(bacheca[0])

if __name__ == "__main__":
    main()
