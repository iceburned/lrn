from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    STUDENT_NAME = "Pesho"

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        courses = {"Python OOP": ["note1", "note2"]}

        student = Student(self.STUDENT_NAME, courses)

        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_student_update_course_when_course_enrolled(self):
        course_name = "Python OOP"
        courses = {course_name: ["note1", "note2"]}

        student = Student(self.STUDENT_NAME, courses)
        result = student.enroll(course_name, ["note3", "note4"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note1", "note2", "note3", "note4"], student.courses[course_name])

    def test_enroll_student_when_course_notes_are_not_passed(self):
        course_name = "Python Advanced"
        course_notes = ["note1", "note2"]
        result = self.student.enroll(course_name, course_notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_when_course_notes_is_Y(self):
        course_name = "Python Advanced"
        course_notes = ["note1", "note2"]
        result = self.student.enroll(course_name, course_notes, "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extend_course_without_notes_when_invalid_course(self):
        course_name = "Python Advanced"
        course_notes = ["note1", "note2"]
        result = self.student.enroll(course_name, course_notes, "N")

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes("Python Advanced", "Note 3")
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_add_notes_update_course_notes(self):
        course_name = "Python Advanced"
        courses = {course_name: ["note1", "note2"]}
        student = Student(self.STUDENT_NAME, courses)
        result = student.add_notes(course_name, "note3")

        with self.assertRaises(Exception) as error:
            self.student.add_notes("Python Advanced", "Note3")
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1", "note2", "note3"], student.courses[course_name])

    def test_leave_course(self):
        self.student.enroll("Python Basic", [])
        with self.assertRaises(Exception) as error:
            self.student.leave_course("Python Advanced")
            self.assertEqual("Cannot remove course. Course not found.", str(error.exception))

    def test_leave_course_removed_when_student_enrolled(self):
        course_name = "Python Advanced"
        student = Student(self.STUDENT_NAME, {course_name: []})
        result = student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in student.courses)


if __name__ == "name":
    main()
