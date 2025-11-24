class ExtraPointsPolicy:
    """
    Representa la política de puntos extra.
    Cumple RF03: docentes acuerdan puntos extra.
    Parte del RF04: contribuye al cálculo final.
    """

    def __init__(self, allow_extra_points: bool):
        self.allow_extra_points = allow_extra_points

    def apply(self, grade: float) -> float:
        """
        Si los docentes están de acuerdo, suma 1 punto extra.
        Caso contrario, deja la nota igual.
        """
        return grade + 1 if self.allow_extra_points else grade
