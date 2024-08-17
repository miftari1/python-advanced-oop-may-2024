from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Bob')

    def test_student_init(self):
        self.assertEqual('Bob', self.student.name)
        self.assertEqual({}, self.student.courses)

        self.student.courses = {'Python': ['n1', 'n2', 'n3'],
                                'JS': ['n1', 'n2']
                                }

        self.assertEqual({'Python': ['n1', 'n2', 'n3'],
                          'JS': ['n1', 'n2']
                          }, self.student.courses)

    def test_student_enroll_if_course_name_in_courses(self):
        self.student.courses = {'Python': ['n1', 'n2', 'n3']}

        result = self.student.enroll('Python', ['n4', 'n5'])

        self.assertEqual(['n1', 'n2', 'n3', 'n4', 'n5'], self.student.courses['Python'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_student_enroll_course_not_in_courses_if_add_course_is_y(self):
        result = self.student.enroll('JS', ['n1', 'n2', 'n3'], 'Y')

        self.assertEqual({'JS': ['n1', 'n2', 'n3']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_enroll_course_not_in_courses_if_add_course_is_empty(self):
        result = self.student.enroll('JS', ['n1', 'n2', 'n3'])

        self.assertEqual({'JS': ['n1', 'n2', 'n3']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_enroll_course_only(self):
        result = self.student.enroll('JS', ['n1', 'n2', 'n3'], 'N')

        self.assertEqual({'JS': []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_student_add_notes_if_course_name_in_courses(self):
        self.student.courses = {'Python': ['n1', 'n2', 'n3']}

        result = self.student.add_notes('Python', ['n4', 'n5'])

        self.assertEqual(['n1', 'n2', 'n3', ['n4', 'n5']], self.student.courses['Python'])
        self.assertEqual("Notes have been updated", result)

    def test_student_add_notes_if_course_name_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python', ['n1', 'n2', 'n3'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_leave_course_if_course_exists(self):
        self.student.courses = {'Python': ['n1', 'n2', 'n3']}

        result = self.student.leave_course('Python')

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_student_leave_course_if_course_does_not_exist_raises(self):
        self.student.courses = {'Python': ['n1', 'n2', 'n3']}

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('JS')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({'Python': ['n1', 'n2', 'n3']}, self.student.courses)


if __name__ == '__main__':
    main()