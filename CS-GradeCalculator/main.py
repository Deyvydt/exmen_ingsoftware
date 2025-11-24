from models.evaluation import Evaluation
from models.attendance_policy import AttendancePolicy
from models.extra_points_policy import ExtraPointsPolicy
from models.grade_calculator import GradeCalculator

def main():
    print("=== CÁLCULO DE NOTA FINAL ===")

    evaluations = []
    n = int(input("¿Cuántas evaluaciones tiene el estudiante? (máx 10): "))

    for i in range(n):
        print(f"\n--- Evaluación {i+1} ---")
        score = float(input("Nota (0-20): "))
        weight = float(input("Peso (0-1): "))
        evaluations.append(Evaluation(score, weight))

    has_attendance = input("\n¿Cumplió la asistencia mínima? (s/n): ").lower() == "s"
    allow_extra = input("¿Todos los docentes acordaron puntos extra? (s/n): ").lower() == "s"
    
    attendance_policy = AttendancePolicy(has_attendance)
    extra_policy = ExtraPointsPolicy(allow_extra)

    calculator = GradeCalculator(evaluations, attendance_policy, extra_policy)
    
    print("\n=== RESULTADO ===")
    print("Nota final:", calculator.calculate())

    print("\n=== DETALLE DEL CÁLCULO ===")
    print(calculator.detail())


if __name__ == "__main__":
    main()
