import random

import plotly.graph_objects as go
import matplotlib.pyplot as plt

from entities import Challenge, Student
from simulator import adapt, simulate
from data import kcs, competences
from scipy.stats import linregress

print("\tComenzando la simulación...")

# NOTE: Descomentar esto si se quiere probar
print("\tSelecciona un número de estudiantes.")
nstudents = int(input())
students = []
print("Generando estudiantes...")
for i in range(nstudents):
    students.append(Student())
print("Estudiantes generados.\n")
print("\tSelecciona un número de retos.")
nchallenges = int(input())
challenges = []
print("Generando retos...")
for i in range(nchallenges):
    challenges.append(Challenge())
print("Retos generados.\n")

cycles = int(input("Selecciona el número de retos a realizar por estudiante: "))

simulate(0, cycles, students, challenges)
# start = 0
start = cycles


def generate_r2(student_length: int, challenge_length: int):
    challenge_list = []
    student_list = []
    for i in range(challenge_length):
        challenge_list.append(Challenge())
    for i in range(student_length):
        student_list.append(Student())
    simulate(0, challenge_length, student_list, challenge_list)
    # Generate the matrix kc_scores_ with the kc i of student j
    kc_scores = []
    kc_skills = []
    competence_scores = []
    competence_skills = []
    for student in student_list:
        for kc in kcs:
            kc_scores.append(student.kc_score[kc])
            kc_skills.append(student.kc_skill[kc])
        for competence in competences:
            competence_scores.append(student.competence_score[competence])
            competence_skills.append(student.competence_skill[competence])

    slope, intercept, r_value, p_value, std_err = linregress(kc_skills, kc_scores)

    regression_line_kc = [slope * i + intercept for i in kc_skills]

    r2_kc = r_value**2

    slope, intercept, r_value, p_value, std_err = linregress(
        competence_skills, competence_scores
    )

    regression_line_challenge = [slope * i + intercept for i in competence_skills]

    r2_challenge = r_value**2

    plt.scatter(kc_skills, kc_scores, color="blue", label="KCs", s=3)
    plt.plot(kc_skills, regression_line_kc, color="green", label="Regresión KCs")
    plt.xlabel("Habilidad real")
    plt.ylabel("Inferencia")
    plt.legend()
    plt.show()

    plt.scatter(
        competence_skills, competence_scores, color="red", label="Competencias", s=4
    )
    plt.plot(
        competence_skills,
        regression_line_challenge,
        color="orange",
        label="Regresión Competencias",
    )
    plt.xlabel("Habilidad real")
    plt.ylabel("Inferencia")
    plt.legend()
    plt.show()

    print(f"R2 KCs: {r2_kc}\nR2 Competencias: {r2_challenge}")


def mean_r2(student_length: int, challenge_length: int, cycles: int):
    r2_kc_total = 0
    r2_challenge_total = 0
    for i in range(cycles):
        print(f"\n\t\tSimulation {i + 1} of {cycles}\n")
        challenge_list = []
        student_list = []
        for i in range(challenge_length):
            challenge_list.append(Challenge())
        for i in range(student_length):
            student_list.append(Student())
        simulate(0, challenge_length, student_list, challenge_list)
        # Generate the matrix kc_scores_ with the kc i of student j
        kc_scores = []
        kc_skills = []
        competence_scores = []
        competence_skills = []
        for student in student_list:
            for kc in kcs:
                kc_scores.append(student.kc_score[kc])
                kc_skills.append(student.kc_skill[kc])
            for competence in competences:
                competence_scores.append(student.competence_score[competence])
                competence_skills.append(student.competence_skill[competence])

        slope, intercept, r_value, p_value, std_err = linregress(kc_skills, kc_scores)

        r2_kc = r_value**2

        slope, intercept, r_value, p_value, std_err = linregress(
            competence_skills, competence_scores
        )

        r2_challenge = r_value**2

        r2_kc_total += r2_kc
        r2_challenge_total += r2_challenge
        print(f"R2 KCs: {r2_kc}\nR2 Competencias: {r2_challenge}")
    print("\n")
    print(
        f"Parámetros usados: N students: {student_length} N challenges: {challenge_length}"
    )
    print(
        f"Mean R2 KCs: {r2_kc_total / cycles}\nMean R2 Competencias: {r2_challenge_total / cycles}"
    )


def generate_stats(student_length: int, challenge_length: int, cycles: int):
    challenge_error = 0
    skill_error = 0
    for i in range(cycles):
        print(f"\n\t\tSimulation {i + 1} of {cycles}\n")
        student_list = []
        for i in range(student_length):
            student_list.append(Student())
        challenge_list = []
        for i in range(challenge_length):
            challenge_list.append(Challenge())

        simulate(0, challenge_length, student_list, challenge_list)

        competences, scores = [], []
        for c, v in student_list[len(student_list) - 1].competence_score.items():
            competences.append(c)
            scores.append(v / 1000)

        # Pequeño truco para que el mínimo sea 0 y el máximo sea 100
        minimum = min(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] - minimum
        maximum = max(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] * 100 / maximum

        challenge_scores = scores

        competences, scores = [], []
        for c, v in student_list[len(student_list) - 1].competence_skill.items():
            competences.append(c)
            scores.append(v / 50)

        # Pequeño truco para que el mínimo sea 0 y el máximo sea 100
        minimum = min(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] - minimum
        maximum = max(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] * 100 / maximum

        challenge_skills = scores

        kc, scores = [], []

        for c, v in student_list[len(student_list) - 1].kc_score.items():
            kc.append(c)
            scores.append(v / 1000)

        minimum = min(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] - minimum
        maximum = max(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] * 100 / maximum

        kc_scores = scores

        kc, scores = [], []

        for c, v in student_list[len(student_list) - 1].kc_skill.items():
            kc.append(c)
            scores.append(v / 50)

        minimum = min(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] - minimum
        maximum = max(scores)
        for i in range(len(scores)):
            scores[i] = scores[i] * 100 / maximum

        kc_skills = scores

        mse_challenges = 0
        for i in range(len(challenge_scores)):
            mse_challenges += (challenge_scores[i] - challenge_skills[i]) ** 2
        mse_challenges = mse_challenges / len(challenge_scores)
        print(f"Error measurement in challenge -> {mse_challenges}")

        mse_kcs = 0
        for i in range(len(kc_scores)):
            mse_kcs += (kc_scores[i] - kc_skills[i]) ** 2
        mse_kcs = mse_kcs / len(kc_scores)
        print(f"Error measurement in KC -> {mse_kcs}")

        challenge_error += mse_challenges
        skill_error += mse_kcs

    print("\n")
    print(f"Mean error measurement in challenge -> {challenge_error / cycles}")
    print(f"Mean error measurement in KC -> {skill_error / cycles}")
    print(
        f"N students: {student_length} N challenges: {challenge_length} Cycles: {cycles}"
    )


def show_stats():
    competence_graph = go.Figure()

    competences, scores = [], []
    for c, v in students[len(students) - 1].competence_score.items():
        competences.append(c)
        scores.append(v / 1000)

    # Pequeño truco para que el mínimo sea 0 y el máximo sea 100
    minimum = min(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] - minimum
    maximum = max(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] * 100 / maximum

    competence_graph.add_trace(
        go.Scatterpolar(
            r=scores,
            theta=competences,
            fill="toself",
            name="Inferencia sobre competencias",
        )
    )

    challenge_scores = scores

    competences, scores = [], []
    for c, v in students[len(students) - 1].competence_skill.items():
        competences.append(c)
        scores.append(v / 50)

    # Pequeño truco para que el mínimo sea 0 y el máximo sea 100
    minimum = min(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] - minimum
    maximum = max(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] * 100 / maximum

    competence_graph.add_trace(
        go.Scatterpolar(
            r=scores,
            theta=competences,
            fill="toself",
            name="Habilidades sobre competencias",
        )
    )

    challenge_skills = scores

    competence_graph.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
    )

    competence_graph.show()

    kc_graph = go.Figure()

    kc, scores = [], []

    for c, v in students[len(students) - 1].kc_score.items():
        kc.append(c)
        scores.append(v / 1000)

    minimum = min(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] - minimum
    maximum = max(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] * 100 / maximum

    kc_graph.add_trace(
        go.Scatterpolar(r=scores, theta=kc, fill="toself", name="Inferencia sobre KCs")
    )

    kc_scores = scores

    kc, scores = [], []

    for c, v in students[len(students) - 1].kc_skill.items():
        kc.append(c)
        scores.append(v / 50)
    minimum = min(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] - minimum
    maximum = max(scores)
    for i in range(len(scores)):
        scores[i] = scores[i] * 100 / maximum

    kc_graph.add_trace(
        go.Scatterpolar(r=scores, theta=kc, fill="toself", name="Habilidades sobre KCs")
    )

    kc_graph.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
    )

    kc_skills = scores

    kc_graph.show()

    # Print last student and challenge
    print(students[len(students) - 1])
    print(challenges[len(challenges) - 1])

    mse_challenges = 0
    for i in range(len(challenge_scores)):
        mse_challenges += (challenge_scores[i] - challenge_skills[i]) ** 2
    mse_challenges = mse_challenges / len(challenge_scores)
    print(f"Error measurement in challenge -> {mse_challenges}")

    mse_kcs = 0
    for i in range(len(kc_scores)):
        mse_kcs += (kc_scores[i] - kc_skills[i]) ** 2
    mse_kcs = mse_kcs / len(kc_scores)
    print(f"Error measurement in KC -> {mse_kcs}")


# show_stats()

while True:
    answer = input(
        "¿Continuar con la simulación [c], calcular estadísticas [s], calcular R² [r], simular un duelo [d] o salir [q]?"
    )
    if answer == "c":
        cycles = int(input("Número de ciclos a simular: "))
        simulate(start, cycles, students, challenges)
        start += cycles
        show_stats()
    elif answer == "d":
        candidates_s = random.sample(students, 3)
        candidates_c = random.sample(challenges, 3)
        print("1. ", candidates_s[0], "\n")
        print("2. ", candidates_s[1], "\n")
        print("3. ", candidates_s[2], "\n")
        print("Elija un estudiante:")
        student = int(input()) - 1

        print("1. ", candidates_c[0], "\n")
        print("2. ", candidates_c[1], "\n")
        print("3. ", candidates_c[2], "\n")
        print("Elija un reto:")
        challenge = int(input()) - 1

        adapted_challenge = adapt(candidates_s[student], candidates_c[challenge])

        print("Estudiante seleccionado: ", candidates_s[student])
        print("Reto seleccionado: ", candidates_c[challenge])
        print("Reto adaptado: ", adapted_challenge)

    elif answer == "s":
        print("Número de estudiantes:")
        student_length = int(input())
        print("Número de retos:")
        challenge_length = int(input())
        print("Número de ciclos:")
        cycles = int(input())
        generate_stats(student_length, challenge_length, cycles)

    elif answer == "r":
        print("Número de estudiantes:")
        student_length = int(input())
        print("Número de retos:")
        challenge_length = int(input())
        choice = input("¿Quieres generar gráficas o ver las medias? [g/m]")
        if choice == "g":
            generate_r2(student_length, challenge_length)
        elif choice == "m":
            print("Número de ciclos:")
            cycles = int(input())
            mean_r2(student_length, challenge_length, cycles)

    elif answer == "q":
        break
