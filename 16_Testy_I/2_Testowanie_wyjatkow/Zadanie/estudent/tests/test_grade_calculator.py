from estudent.grade_calculator import GradeCalculator
from estudent.grade import Grade


def test_normal_promotion_policy_pass():
    passing_grade = Grade(value=5)
    failing_grade = Grade(value=1)
    final_grades = [failing_grade, passing_grade, passing_grade]

    assert GradeCalculator.normal_promotion_policy(final_grades) is True


def test_normal_promotion_policy_fail():
    passing_grade = Grade(value=5)
    failing_grade = Grade(value=1)
    final_grades = [failing_grade, failing_grade, failing_grade, passing_grade]

    assert GradeCalculator.normal_promotion_policy(final_grades) is False


def test_strict_promotion_policy_pass():
    passing_grade = Grade(value=5)
    failing_grade = Grade(value=1)
    final_grades = [failing_grade, passing_grade, passing_grade, passing_grade]

    assert GradeCalculator.strict_promotion_policy(final_grades) is True


def test_strict_promotion_policy_fail_grades():
    passing_grade = Grade(value=5)
    failing_grade = Grade(value=1)
    final_grades = [failing_grade, failing_grade, failing_grade, passing_grade]

    assert GradeCalculator.strict_promotion_policy(final_grades) is False


def test_strict_promotion_policy_fail_avg():
    passing_grade = Grade(value=2)
    failing_grade = Grade(value=1)
    final_grades = [failing_grade, passing_grade, passing_grade]

    assert GradeCalculator.strict_promotion_policy(final_grades) is False


def test_get_number_of_failing_grades_return_fail():
    passing_grade = Grade(value=2)
    failing_grade = Grade(value=1)
    final_grades = [failing_grade, passing_grade, failing_grade]

    assert GradeCalculator.get_number_of_failing_grades(final_grades) == 2


def test_get_number_of_failing_gradesempty_list():
    final_grades = []

    assert GradeCalculator.get_number_of_failing_grades(final_grades) == 0


def test_calculate_student_avg():
    grade_5 = Grade(value=5)
    grade_3 = Grade(value=3)
    final_grades = [grade_3, grade_3, grade_5, grade_5]
    assert GradeCalculator.calculate_student_avg(final_grades) == 4


# def test_calculate_student_avg_empty_list():
#     final_grades = []
#     assert GradeCalculator.calculate_student_avg(final_grades) == 0
