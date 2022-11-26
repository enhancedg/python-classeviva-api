#
# Code by Francesco Pallara
#

from user import User

class Student(User):
    
    def get(self, info: str) -> dict:

        """
          ? GET request to ClasseViva API as a student
            @param info: name of the information to request
          * Returns the result of the request as a dictionary
        """
        
        student_uri_base = "students/%s/"
        data = super().get(student_uri_base + info)

        return data
    
    def get_card(self) -> dict:

        """ 
          ? Get the card of the student with these informations:
            @attr ident: student id
            @attr usrType: determine the user type
            @attr usrId: user id
            @attr miurSchoolCode: miur school code
            @attr miurDivisionCode: same as miurSchoolCode (?)
            @attr firstName: first name of the student
            @attr lastName: last name of the student
            @attr birthDate: date of birth of student
            @attr fiscalCode: student's fiscal code
            @attr schCode: school code
            @attr schName: school name
            @attr schDedication: name of the person to whom the school was dedicated
            @attr schCity: school city
            @attr schProv: school province (code)
          * Returns a dictionary
        """

        card = self.get("card")

        return card

    def get_subjects(self) -> dict:
        subjects = self.get()

        return subjects