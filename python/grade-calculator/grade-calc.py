import csv
from collections import defaultdict


def letter_grade(avg):

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_calculator():

    with open(
        "./grades.csv",
        mode="r",
        newline="",
        encoding="utf-8",
    ) as file:
        csv_reader = csv.DictReader(file)

        subject_scores = defaultdict(list)

        print("\n=== Student Scores: ===")
        for row in csv_reader:
            name = row["Name"]
            scores = []

            for subject, score in row.items():
                if subject != "Name":
                    score_int = int(score)
                    scores.append(score_int)
                    subject_scores[subject].append(score_int)

            avg = sum(scores) / len(scores)
            grade = letter_grade(avg)

            print(
                f"{name}: Grade: {grade}, Average: {avg:.1f}, High: {max(scores)}, Low: {min(scores)}"
            )

        print("\n=== Subject Scores: ===")

        for subject, scores in subject_scores.items():
            avg = sum(scores) / len(scores)
            grade = letter_grade(avg)
            high = max(scores)
            low = min(scores)
            print(
                f"{subject}: Grade: {grade} Average: {avg:.1f}, High: {high}, Low: {low}"
            )


if __name__ == "__main__":

    grade_calculator()
