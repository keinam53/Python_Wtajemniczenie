def test_is_passing_grade_above_1(passing_grade):
    assert passing_grade.is_passing() is True


def test_is_passing_grade_1(failing_grade):
    assert failing_grade.is_passing() is False
