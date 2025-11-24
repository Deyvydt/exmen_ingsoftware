class GradeCalculator:
    """
    Calcula la nota final del estudiante.
    Cumple RF04 (cálculo) y RF05 (detalle del cálculo).
    """

    MAX_EVALUATIONS = 10

    def __init__(self, evaluations, attendance_policy, extra_points_policy):
        # RNF01: máximo 10 evaluaciones
        if len(evaluations) > self.MAX_EVALUATIONS:
            raise ValueError("No se permiten más de 10 evaluaciones.")

        self.evaluations = evaluations
        self.attendance_policy = attendance_policy
        self.extra_points_policy = extra_points_policy

    def calculate(self) -> float:
        """
        Calcula la nota final aplicando:
        - Evaluaciones
        - Política de asistencia
        - Política de puntos extra
        """

        # Calculamos nota base sumando score * weight
        base_grade = sum(e.score * e.weight for e in self.evaluations)

        # Aplicamos asistencia mínima
        base_grade = self.attendance_policy.apply(base_grade)

        # Aplicamos política de puntos extra
        base_grade = self.extra_points_policy.apply(base_grade)

        # RNF03: determinista → redondeo fijo
        return round(base_grade, 2)

    def detail(self) -> str:
        """
        Devuelve un string con el detalle del cálculo.
        Cumple RF05.
        """
        details = []

        for idx, e in enumerate(self.evaluations, start=1):
            details.append(f"Eval {idx}: nota={e.score}, peso={e.weight}")

        details.append(f"Asistencia mínima: {self.attendance_policy.has_minimum_attendance}")
        details.append(f"Puntos extra: {self.extra_points_policy.allow_extra_points}")
        details.append(f"Nota final: {self.calculate()}")

        return "\n".join(details)
