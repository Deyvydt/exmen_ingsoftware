class Evaluation:
    """
    Representa una evaluación con una nota y un peso.
    Cumple RF01: registrar evaluaciones.
    """

    def __init__(self, score: float, weight: float):
        # Validaciones (calidad, RNF03 determinismo)
        if score < 0 or score > 20:
            raise ValueError("La nota debe estar entre 0 y 20.")
        if weight < 0 or weight > 1:
            raise ValueError("El peso debe estar entre 0 y 1.")

        self.score = score
        self.weight = weight
