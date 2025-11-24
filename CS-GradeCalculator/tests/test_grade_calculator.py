import pytest
from models.evaluation import Evaluation
from models.attendance_policy import AttendancePolicy
from models.extra_points_policy import ExtraPointsPolicy
from models.grade_calculator import GradeCalculator


def test_shouldReturnCorrectGradeWhenNormalCase():
    e1 = Evaluation(18, 0.3)
    e2 = Evaluation(15, 0.7)
    calc = GradeCalculator(
        [e1, e2],
        AttendancePolicy(True),
        ExtraPointsPolicy(True)
    )
    assert calc.calculate() == 16.9


def test_shouldReturnZeroWhenNoAttendance():
    e1 = Evaluation(20, 0.5)
    e2 = Evaluation(15, 0.5)
    calc = GradeCalculator(
        [e1, e2],
        AttendancePolicy(False),
        ExtraPointsPolicy(True)
    )
    assert calc.calculate() == 0.0


def test_shouldReturnSameGradeWhenNoExtraPoints():
    e1 = Evaluation(20, 0.5)
    e2 = Evaluation(10, 0.5)
    calc = GradeCalculator(
        [e1, e2],
        AttendancePolicy(True),
        ExtraPointsPolicy(False)
    )
    assert calc.calculate() == 15.0


def test_shouldRaiseErrorWhenInvalidWeight():
    with pytest.raises(ValueError):
        Evaluation(15, 2.0)


def test_shouldReturnZeroWhenZeroEvaluations():
    calc = GradeCalculator(
        [],
        AttendancePolicy(True),
        ExtraPointsPolicy(False)
    )
    assert calc.calculate() == 0.0
