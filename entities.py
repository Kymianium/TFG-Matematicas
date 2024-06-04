from data import kcs, competences, competence_kcs

import random

import names

from parameters import (
    starting_elo,
    easy_starting_elo,
    medium_starting_elo,
    hard_starting_elo,
)


class Attempt:
    def __init__(
        self,
        challenge: str,
        competence: str,
        skills: list,
        success: bool,
        timelapse: int,
    ):
        self.challenge = challenge
        self.competence = competence
        self.skills = skills
        self.success = success
        self.timelapse = timelapse  # 0 for last hour, 1 for last day, 2 for last week, 3 for last month, 4 for whenever

    def __str__(self):
        return (
            self.challenge
            + "\n Competence -> "
            + self.competence
            + "\n Skills -> "
            + str(self.skills)
            + "\n Success -> "
            + str(self.success)
            + "\n Timelapse -> "
            + str(self.timelapse)
            + "\n"
        )


class Student:
    def __init__(self):
        self.name = "Juan"  # names.get_full_name()
        self.competence_skill = {
            competence: random.randrange(0, 100) for competence in competences
        }
        self.kc_skill = {kc: random.randrange(0, 100) for kc in kcs}
        self.competence_score = {competence: starting_elo for competence in competences}
        self.kc_score = {kc: starting_elo for kc in kcs}
        self.history = list()

        # Make the skill approximate to the competence in which it belongs
        for competence, components in competence_kcs.items():
            for kc in components:
                self.kc_skill[kc] = round(
                    (self.kc_skill[kc] + self.competence_skill[competence]) / 2
                )

    def __str__(self):
        return (
            self.name
            + "\n\tTRUE SCORES"
            + "\n Competences -> "
            + str(self.competence_skill)
            + "\n KCs -> "
            + str(self.kc_skill)
            + "\n\tESTIMATIONS"
            + "\n Competence Score -> "
            + str(self.competence_score)
            + "\n KC Score -> "
            + str(self.kc_score)
            + "\n"
        )


class Challenge:
    def __init__(self):
        self.competence = random.choice(competences)
        self.name = self.competence + " " + random.randint(1, 100).__str__()
        self.kcs = random.sample(kcs, random.randint(2, 5))
        self.difficulty = random.randint(0, 100)
        self.time = random.randrange(300, 172800, 60)
        self.attempts = random.randint(1, 5)
        self.max_hints = len(self.kcs)
        self.hints = random.randint(0, self.max_hints)
        self.min_time = random.randint(180, round(self.time * 0.8))
        if self.difficulty < 30:
            self.score = easy_starting_elo
        elif self.difficulty < 70:
            self.score = medium_starting_elo
        else:
            self.score = hard_starting_elo

    def __str__(self):
        return (
            self.name
            + "\n Competence -> "
            + self.competence
            + "\n KCs -> "
            + str(self.kcs)
            + "\n Difficulty -> "
            + str(self.difficulty)
            + "\n Score -> "
            + str(self.score)
            + "\n"
            + "\n\n STATS"
            + "\n Time -> "
            + str(self.time)
            + "\n Attempts -> "
            + str(self.attempts)
            + "\n Hints -> "
            + str(self.hints)
        )

    def copy(self):
        copy = Challenge()
        copy.competence = self.competence
        copy.name = self.name
        copy.kcs = self.kcs
        copy.difficulty = self.difficulty
        copy.time = self.time
        copy.attempts = self.attempts
        copy.max_hints = self.max_hints
        copy.hints = self.hints
        copy.min_time = self.min_time
        copy.score = self.score
        return copy
