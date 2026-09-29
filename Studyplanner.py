from Prioritymanager import calculate_priority
#GENERATE STUDY PLAN

def generate_schedule(data):
    """
    Generates a study schedule according to subject priority
    and the student's available study time.
    """

    print("\n" + "=" * 60)
    print("              GENERATE STUDY PLAN")
    print("=" * 60)

    if not data["subjects"]:
        print("Please add subjects first.")
        return

    while True:
        try:
            hours = float(
                input("How many hours can you study today? ")
            )

            if hours <= 0:
                print("Study time must be greater than zero.")
                continue

            if hours > 24:
                print("Please enter a realistic number of hours.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    subject_scores = []

    for subject in data["subjects"]:

        score, priority, days_left = calculate_priority(subject)

        subject_scores.append({
            "subject": subject,
            "score": score,
            "priority": priority,
            "days_left": days_left
        })

    # Sorting subjects 
    subject_scores.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    total_score = sum(
        item["score"] for item in subject_scores
    )

    if total_score == 0:
        print("Unable to generate a study plan.")
        return

    print("\n" + "=" * 60)
    print("                  TODAY'S PLAN")
    print("=" * 60)

    remaining_hours = hours

    for item in subject_scores:

        if remaining_hours <= 0:
            break

        subject = item["subject"]

    
        allocated_hours = (
            hours * item["score"] / total_score
        )

        
        allocated_hours = max(0.25, allocated_hours)

        
        allocated_hours = min(
            allocated_hours,
            remaining_hours
        )

        minutes = round(allocated_hours * 60)

        print(
            f"\n{subject['name']}"
        )
        print(
            f"   Priority : {item['priority']}"
        )
        print(
            f"   Study    : {minutes} minutes"
        )
        print(
            f"   Progress : {subject['progress']:.1f}%"
        )

        remaining_hours -= allocated_hours

    print("\n" + "=" * 60)