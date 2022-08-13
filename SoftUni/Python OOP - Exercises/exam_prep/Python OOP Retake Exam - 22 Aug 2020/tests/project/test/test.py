from project.student_report_card import StudentReportCard

from unittest import TestCase


class StudentReportCardTest(TestCase):

    def setUp(self) -> None:
        self.card = StudentReportCard("Pesho", 10)

    def test_init(self):
        self.assertEqual("Pesho", self.card.student_name)
        self.assertEqual(10, self.card.school_year)
        self.assertDictEqual({}, self.card.grades_by_subject)

    def test_student_name_setter(self):
        with self.assertRaises(ValueError) as error:
            self.card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))

    def test_student_year_setter(self):
        with self.assertRaises(ValueError) as error:
            self.card.school_year = 20
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_student_year_setter_zero(self):
        with self.assertRaises(ValueError) as error:
            self.card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_student_year_setter_1(self):
        self.card.school_year = 1
        self.assertEqual(1, self.card.school_year)

    def test_student_year_setter_12(self):
        self.card.school_year = 12
        self.assertEqual(12, self.card.school_year)

    def test_add_grade_subject_not_in(self):
        self.card.add_grade("Math", 10.00)
        self.assertEqual({"Math": [10.00]}, self.card.grades_by_subject)

    def test_add_grade_subject_in(self):
        self.card.add_grade("Math", 10.00)
        self.card.add_grade("Math", 10.00)
        self.assertEqual({"Math": [10.00, 10.00]}, self.card.grades_by_subject)

    def test_average_grade(self):
        self.card.grades_by_subject = {"Math": [10, 20, 30], "Chemistry": [10, 10, 10]}
        actual = self.card.average_grade_by_subject()
        expected = "Math: 20.00\nChemistry: 10.00"
        self.assertEqual(expected, actual)

    def test_average_grade_all_subjects(self):
        self.card.grades_by_subject = {"Math": [10, 20, 30], "Chemistry": [10, 10, 10]}
        actual = self.card.average_grade_for_all_subjects()
        expected = "Average Grade: 15.00"
        self.assertEqual(expected, actual)

    def test_repr(self):
        self.card.grades_by_subject = {"Math": [10, 20, 30], "Chemistry": [10, 10, 10]}
        actual = self.card.__repr__()
        expected = "Name: Pesho\n" \
                   "Year: 10\n" \
                   "----------\n" \
                   "Math: 20.00\n" \
                   "Chemistry: 10.00\n" \
                   "----------\n" \
                   "Average Grade: 15.00"
        self.assertEqual(expected, actual)
