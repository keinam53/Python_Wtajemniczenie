import pytest
from estudent.student import Student


@pytest.fixture
def student() -> Student:
    student = Student(first_name="Student-0", last_name="Test")
    return student


@pytest.fixture
def student_with_grades(student) -> Student:
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    return student


def test_str_contains_info_about_promotion_and_avg(student_with_grades):
    student_str = str(student)

    assert "Student: Student-0 Test" in student_str
    assert "promowany:" in student_str
    assert "średnia: 5" in student_str


def test_grades_avg(student):
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    student.add_final_grade(grade=3, check_promotion_policy=lambda grades: False)

    assert student.grades_avg() == 4


def test_promote(student):
    student.promote()

    assert student.promoted is True


def test_add_final_grade_register_new_grade(student):
    student.add_final_grade(grade=5)

    assert student.grades_avg() == 5


def test_add_final_grade_promotion_policy(student):
    student.add_final_grade(grade=5)

    assert student.promoted is True


def test_add_final_promote_student_when_have_proper_grades(student):
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: grades[0].value == 5)

    assert student.promoted is True


def test_add_final_wont_promote_student_when_doesnt_have_proper_grades(student):
    student.add_final_grade(grade=4, check_promotion_policy=lambda grades: grades[0].value == 5)

    assert student.promoted is False

