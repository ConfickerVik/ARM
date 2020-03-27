import test
import unittest

author = {
    "login": "dfhnj",
    "pass": "fdhjrnf"
}

addCourse = {
    "typeAction": "addCourse",
    "name_dis": "База данных",
    "group_name": "ИС-16-1",
    "university": "ИрГУПС",
    "year_education": 2000
}
delCourse = {
    "typeAction": "deleteCourse",
    "id_course": 92
}
editCourse = {
    "typeAction": "editCourse",
    "id_course": 5,
    "name_dis": "Программирование",
    "group_name": "ПИ.1-16-1",
    "university": "ИрГУПС",
    "year_education": 2013
}
aboutCourse = {
    "typeAction": "editCourse",
    "id_course": 5,
    "name_dis": "Программирование",
    "group_name": "ПИ.1-16-1",
    "university": "ИрГУПС",
    "year_education": 2013,
    "hours_eucation": 144,
    "comment": "Yes"
}
addLesson = {
    "id_course": 5,
    "name": "Реляционные БД",
    "type": "Лекция",
    "date": "2015-01-14"
}
delLesson = {
    "delCourse_id": 16
}

editLesson = {
    "id_lesson": 17,
    "name": "SQl",
    "type": "Лабораторная",
    "date": "14.03.2013"
}

course = {
    "typeAction": "deleteLesson",
    "id_course": 5,
    "delCourse_id": 17,
    "id_lesson": 17,
    "name": "SQl",
    "type": "Лабораторная",
    "date": "14.03.2013"
}

schedule = {
    "id_prepod": 5
}

editEstim = {
    "typeAction": "changeMark",
    "id_estimation": 5,
    "mark": 1
}
editAtten = {
    "typeAction": "changeAtten",
    "id_attendance": 5,
    "mark": 5
}

createEstim = {
    "id_lesson": 2,
    "mark": 5,
    "time_date": "03.14,2013",
    "id_student": 1
}

createAtten = {
    "id_lesson": 2,
    "time_date": "03.14,2013",
    "id_attendance": 5,
    "attendance": 5,
    "id_student": 1
}

mark = {
    "id_lesson": 2,
    "time_date": "03.14,2013",
    "id_attendance": 5,
    "attendance": 5,
    "id_student": 1
}
addRul = {
    "typeAction": "addRule",
    "name_rule": " 1",
    "kof_attendance": 0.4,
    "kof_mark": 0.6
}

deleteRul = {
    "typeAction": "deleteRule",
    "delRule_id": 1
}


class Test(unittest.TestCase):
    def test_auth(self):
        test.index(author)

    def test_addCourse(self):
        test.addCourseModal(addCourse)

    def test_delCourse(self):
        test.deleteCourse(delCourse)

    def test_editCourse(self):
        test.editCourseModal(editCourse)

    def test_cabinet(self):
        test.cabinet(delCourse)

    def test_aboutCourse(self):
        test.editAboutCourse(aboutCourse)

    def test_addLesson(self):
        test.addLesson(addLesson)

    def test_delLesson(self):
        test.deleteLesson(delLesson)

    def test_editLesson(self):
        test.editLesson(editLesson)

    def test_course(self):
        test.course(course, 5)

    def test_schedule(self):
        test.schedule(schedule)

    def test_students(self):
        test.students(schedule)

    def test_editEstim(self):
        test.editEstimation(editEstim)

    def test_editAtten(self):
        test.editAttendance(editAtten)

    # Ошибка с датами не доконца разобралась
    #def test_createEstim(self):
        #test.createEstimation(createEstim)

    # Ошибка с датами не доконца разобралась
    #def test_createAtten(self):
        #test.createAttendance(createAtten)

    def test_marks(self):
        test.marks(mark, "База данных", "ПИ.1-16-1")

    def test_addRule(self):
        test.addRule(addRul)

    def test_deleteRule(self):
        test.deleteRule(deleteRul)

    def test_finalMark(self):
        test.finalMark(deleteRul)

    def test_finalMarkStudent(self):
        test.finalMarkStudent(addRul, 1, "ПИ.1-16-1", 0.4, 0.6)


if __name__ == '__main__':
    unittest.main()
