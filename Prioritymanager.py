import datetime
#CALCULATE PRIORITY

def calculate_priority(subject):
    """
    Calculates a priority score for a subject.

    Factors:
    1. Exam urgency
    2. Difficulty
    3. Remaining syllabus

    Returns:
        score
        priority level
        days remaining
    """

    exam_date = datetime.datetime.strptime(
        subject["exam_date"], "%d-%m-%Y"
    ).date()

    days_left = (exam_date - datetime.date.today()).days

    
    if days_left < 1:
        urgency_score = 100
    else:
        urgency_score = min(100, (10 / days_left) * 10)

    difficulty_score = subject["difficulty"] * 10

    remaining_work = 100 - subject["progress"]

    remaining_score = remaining_work

    score = (
        urgency_score * 0.40
        + difficulty_score * 0.25
        + remaining_score * 0.35
    )

    # Priority level
    if score >= 65:
        priority = "HIGH"

    elif score >= 40:
        priority = "MEDIUM"

    else:
        priority = "LOW"

    return score, priority, days_left

#AT-RISK SUBJECT DETECTION

def show_at_risk_subjects(data):
    """
    Identifies subjects that may require immediate attention.
    """

    print("\n" + "=" * 60)
    print("                 AT-RISK SUBJECTS")
    print("=" * 60)

    if not data["subjects"]:
        print("No subjects available.")
        return

    found = False

    for subject in data["subjects"]:

        score, priority, days_left = calculate_priority(subject)


        if (
            (days_left <= 3 and subject["progress"] < 60)
            or
            (days_left <= 5 and subject["progress"] < 40)
            or
            score >= 70
        ):

            found = True

            print(f"\n⚠ {subject['name']}")
            print(f"   Days left : {max(days_left, 0)}")
            print(
                f"   Progress : "
                f"{subject['progress']:.1f}%"
            )
            print(
                f"   Difficulty : "
                f"{subject['difficulty']}/5"
            )
            print(f"   Priority : {priority}")

    if not found:
        print(
            "\nNo subjects are currently classified as at-risk."
        )

    print("=" * 60)