from estudent.grade import Grade
from unittest import TestCase


class GradeTestCase(TestCase):
    def setUp(self) -> None:
        self.passing_grade = Grade(value=5)
        self.failing_grade = Grade(value=1)

    def test_grade_above_1_is_passing(self):
        self.assertTrue(self.passing_grade.is_passing())

    def test_grade_below_2_is_failing(self):
        self.assertFalse(self.failing_grade.is_passing())
