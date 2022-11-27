#
# Code by Francesco Pallara
#

from user import User
from datetime import date

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
      ? Get the card of the student
      * Returns a dictionary with these informations:
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
    """

    card = self.get("card")

    return card['card']

  def get_subjects(self) -> list:

    """
      ? Get a list of all the subjects
      * Returns a list of Subjects.
      * A subject is a dictionary with these informations:
        @attr id: subject id
        @attr description: subject description, the name of the subject
        @attr order: a number utilized to order subjects
        @attr teachers: a list of Teachers of the subject
    """
    subjects = self.get("subjects")

    return subjects['subjects']

  def get_lessons(self, lessons_date: date) -> list:

    """
      ? Get a list of lessons of a specific day
      @param lessons_date: date of the lessons to get
      * Returns a list of Lessons.
      * A lesson is a dictionary with these informations:
        @attr evtId: lesson id
        @attr evtDate: lesson date expressed in YYYY-MM-DD
        @attr evtCode: I'm not sure what it is
        @attr evtHPos: school hour
        @attr evtDuration: duration of the lesson expressed in hour
        @attr classDesc: description of the class
        @attr authourName: teacher name
        @attr subjectId: subject id
        @attr subjectCode: the name of the subject expressed in a code with two letters
        @attr subjectDesc: subject description
        @attr lessonType: lesson type
        @attr lessonArg: lesson topic
    """

    lessons = self.get(f"lessons/" + lessons_date.strftime("%Y%m%d"))

    return lessons['lessons']

  def get_today_lessons(self) -> list:

    """
      ? Get a list of today lessons
      * Returns a list of Lessons, see get_lessons
    """
    today_lessons = self.get("lessons/today")

    return today_lessons['lessons']

  def get_noticeboard(self) -> list:

    """
      ? Get a list of all the publications on the noticeboard
      * Returns a list of Publications.
      * A publication is a dictionary with these informations:
        @attr pubId: publication id
        @attr pubDT: publication date
        @attr readStatus: boolean value, determines if the publication has been read
        @attr evtCode: I'm not sure what it is
        @attr cntId: content id
        @attr cntValidFrom: release date
        @attr cntValidTo: expiration date
        @attr cntTitle: publication title
        @attr cntCategory: publication category
        @attr cntHasChanged: boolean value, determines if the publication has been modified
        @attr cntHasAttach: boolean value, determines if the publication has attachments
        @attr needJoin: boolean value, I'm not sure what it is
        @attr needReply: boolean value, determines if the publication needs to be replied
        @attr needFile: boolean value, I'm not sure what it is
        @attr needSign: boolean value, determines if the publication needs a signature
        @attr evento_id: id of the event
        @attr dinsert_allegato: attachments insertion date
        @attr attachments: attachments list (fileName: str, attachNum: int)

    """

    noticeboard = self.get("noticeboard")

    return noticeboard['items']
    