from logic import student_passes, update
from entities import Student, Challenge
from parameters import (
    time_adapt_weight_harder,
    attempts_adapt_weight_harder,
    hints_adapt_weight_harder,
    time_adapt_weight_easier,
    attempt_adapt_weight_easier,
    hints_adapt_weight_easier,
    time_aggresiveness,
    attempts_aggresiveness,
    hints_aggresiveness,
)


def simulate(start: int, cycles: int, students: list, challenges: list):
    for i in range(cycles):
        # print(f"Cycle {i + 1}")
        for student in students:
            challenge = challenges[start + i % len(challenges)]
            result = student_passes(student, challenge)
            update(challenge, student, result)


def adapt(student: Student, challenge: Challenge) -> Challenge:
    challenge_elo = challenge.score
    student_elo = student.competence_score[challenge.competence]

    # Calculate the gamma value
    Gamma = student_elo / challenge_elo

    # Calculate the gammas
    if Gamma < 1:
        time_adapt_weight = time_adapt_weight_easier
        hints_adapt_weight = hints_adapt_weight_easier
        attempts_adapt_weight = attempt_adapt_weight_easier
    else:
        time_adapt_weight = time_adapt_weight_harder
        hints_adapt_weight = hints_adapt_weight_harder
        attempts_adapt_weight = attempts_adapt_weight_harder

    # Calculate the gammas
    time_gamma = Gamma**time_adapt_weight
    attempt_gamma = Gamma**attempts_adapt_weight
    hints_gamma = Gamma**hints_adapt_weight

    # Calculate the new values
    time_adapt = round(
        challenge.min_time
        + (challenge.time - challenge.min_time) / time_gamma**time_aggresiveness
    )
    hints_adapt = max(
        0,
        round(
            challenge.max_hints
            - hints_gamma**hints_aggresiveness * (challenge.max_hints - challenge.hints)
        ),
    )
    attempts_adapt = max(
        1,
        round(
            challenge.attempts
            + (1 - attempt_gamma) * challenge.attempts * attempts_aggresiveness,
        ),
    )

    copy = challenge.copy()

    copy.time = time_adapt
    copy.hints = hints_adapt
    copy.attempts = attempts_adapt

    return copy
