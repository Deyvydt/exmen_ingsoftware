class AttendancePolicy:
    """
    Representa la política de asistencia mínima.
    Cumple RF02: indicar si alcanzó la asistencia mínima.
    """

    def __init__(self, has_minimum_attendance: bool):
        self.has_minimum_attendance = has_minimum_attendance

    def apply(self, grade: float) -> float:
        """
        Si NO cumple asistencia mínima, la nota final es 0.
        Si la cumple, devuelve la nota tal cual.
        """
        return grade if self.has_minimum_attendance else 0.0
