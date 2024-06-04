import numpy as np
import math
import random

from entities import Student, Challenge, Attempt
from parameters import attempt_weights, success_weights, starting_elo, k


def sigmoid(value: float):
    return 1 / (1 + np.exp(-value))


# This functions returns true if the student passes the challenge
def student_passes(student: Student, challenge: Challenge) -> bool:
    competence = challenge.competence
    student_skill = student.competence_skill[competence]
    challenge_difficulty = challenge.difficulty

    # Average of student skill and KCs involved

    # print(f"Student skill: {student_skill}")

    student_final_skill = student_skill / 2
    for kc in challenge.kcs:
        # print(f"KC {kc}: {student.kc_skill[kc]}")
        student_final_skill += student.kc_skill[kc] / (2 * len(challenge.kcs))

    # print(
    #     f"Student score: {student_final_skill}\nChallenge score: {challenge_difficulty}"
    # )

    # The duel score is 2**(skill/4)
    student_chances = math.floor(2 ** (student_final_skill / 4) * 100)
    challenge_chances = math.floor(2 ** (challenge_difficulty / 4) * 100)

    # print(f"Student chances: {student_chances}\nChallenge chances: {challenge_chances}")

    r = random.randint(0, student_chances + challenge_chances)
    if r <= student_chances:
        # print("\nStudent wins\n")
        return True
    # print("\nChallenge wins\n")
    return False


def calculate_chances(student: Student, challenge: Challenge) -> float:
    competence = challenge.competence
    student_score = student.competence_score[competence]
    challenge_score = challenge.score

    alpha = (student_score - starting_elo) / 400  # FIXME: in latex
    delta = (challenge_score - starting_elo) / 400

    # H function calculation

    h_function = 0

    count_attempts = [0, 0, 0, 0, 0]
    count_success = [0, 0, 0, 0, 0]

    for attempt in student.history:
        # Check if the attempt is related to the KCs of the challenge
        for kc in attempt.skills:
            if kc in challenge.kcs:
                if attempt.timelapse == 0:
                    count_attempts[0] += 1
                    if attempt.success:
                        count_success[0] += 1
                elif attempt.timelapse == 1:
                    count_attempts[1] += 1
                    if attempt.success:
                        count_success[1] += 1
                elif attempt.timelapse == 2:
                    count_attempts[2] += 1
                    if attempt.success:
                        count_success[2] += 1
                elif attempt.timelapse == 3:
                    count_attempts[3] += 1
                    if attempt.success:
                        count_success[3] += 1
                elif attempt.timelapse == 4:
                    count_attempts[4] += 1
                    if attempt.success:
                        count_success[4] += 1
                else:
                    raise ValueError("Invalid timelapse value")

    for i in range(5):
        h_function += success_weights[i] * np.log(
            1 + count_success[i]
        ) - attempt_weights[i] * (np.log(1 + count_attempts[i]))

    # End of H function calculation

    beta = 0
    for kc in challenge.kcs:
        beta += (student.kc_score[kc] - starting_elo) / 400
    # beta /= len(challenge.kcs)  # FIXME: in latex
    return sigmoid(alpha - delta + beta + h_function)


def generate_timestamp() -> int:
    value = random.randint(0, 300)
    if value < 5:
        return 0
    elif value < 20:
        return 1
    elif value < 50:
        return 2
    elif value < 100:
        return 3
    return 4


def update(challenge: Challenge, student: Student, student_wins: bool) -> None:
    student_prediction = calculate_chances(student, challenge)
    if student_wins:
        # Student update
        student.competence_score[challenge.competence] += math.floor(
            k * (1 - student_prediction)
        )
        # Challenge update
        challenge.score += math.floor(k * (student_prediction - 1))
        if challenge.score < 100:
            challenge.score = 100

        # KCs update
        for kc in challenge.kcs:
            student.kc_score[kc] += math.floor(k * (1 - student_prediction))

        # History update
        student.history.append(
            Attempt(
                challenge.name,
                challenge.competence,
                challenge.kcs,
                True,
                generate_timestamp(),
            )
        )
    else:
        # Student update
        student.competence_score[challenge.competence] += math.floor(
            k * (-student_prediction)
        )
        if student.competence_score[challenge.competence] < 100:
            student.competence_score[challenge.competence] = 100

        # Challenge update
        challenge.score += math.floor(k * (student_prediction))

        # KCs update
        for kc in challenge.kcs:
            student.kc_score[kc] += math.floor(k * (-student_prediction))
            if student.kc_score[kc] < 100:
                student.kc_score[kc] = 100

        # History update
        student.history.append(
            Attempt(
                challenge.name,
                challenge.competence,
                challenge.kcs,
                False,
                generate_timestamp(),
            )
        )
