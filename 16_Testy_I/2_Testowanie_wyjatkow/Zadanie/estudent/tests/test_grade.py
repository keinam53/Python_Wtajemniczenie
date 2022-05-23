from estudent.grade import Grade


def test_is_passing_grade_above_1():
    grade_above_1 = Grade(value=2)
    assert grade_above_1.is_passing() is True


def test_is_passing_grade_1():
    grade_1 = Grade(value=1)
    assert grade_1.is_passing() is False
