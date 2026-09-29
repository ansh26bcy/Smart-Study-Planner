import datetime
from Datamanager import save_data
# UPDATE PROGRESS

def update_progress(data):
    """
    Updates the progress of an existing subject.
    """

    print("\n" + "=" * 50)
    print("              UPDATE PROGRESS")
    print("=" * 50)

    if not data["subjects"]:
        print("No subjects available.")
        return

    for index, subject in enumerate(data["subjects"], start=1):
        print(
            f"{index}. {subject['name']} "
            f"({subject['progress']:.1f}%)"
        )

    while True:
        try:
            choice = int(
                input("\nSelect subject number: ")
            )

            if 1 <= choice <= len(data["subjects"]):
                break

            print("Invalid subject number.")

        except ValueError:
            print("Please enter a valid number.")

    subject = data["subjects"][choice - 1]

    print(
        f"\nCurrent progress: "
        f"{subject['progress']:.1f}%"
    )

    while True:
        try:
            new_progress = float(
                input("Enter new progress (0-100): ")
            )

            if 0 <= new_progress <= 100:
                break

            print("Progress must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    old_progress = subject["progress"]

    subject["progress"] = new_progress

    save_data(data)

    print(
        f"\nProgress updated:"
        f"\n{old_progress:.1f}% → {new_progress:.1f}%"
    )

# LOG STUDY SESSION

def log_study_session(data):
    """
    Records a completed study session.
    """

    print("\n" + "=" * 50)
    print("              LOG STUDY SESSION")
    print("=" * 50)

    if not data["subjects"]:
        print("No subjects available.")
        return

    for index, subject in enumerate(data["subjects"], start=1):
        print(
            f"{index}. {subject['name']}"
        )

    while True:
        try:
            choice = int(
                input("\nSelect subject number: ")
            )

            if 1 <= choice <= len(data["subjects"]):
                break

            print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

    subject = data["subjects"][choice - 1]

    while True:
        try:
            minutes = int(
                input("Enter study time in minutes: ")
            )

            if minutes > 0:
                break

            print("Study time must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    session = {
        "date": datetime.date.today().strftime("%d-%m-%Y"),
        "subject": subject["name"],
        "minutes": minutes
    }

    data["study_history"].append(session)

    save_data(data)

    print(
        f"\nStudy session saved!"
        f"\n{subject['name']} → {minutes} minutes"
    )

# VIEW STUDY HISTORY

def view_study_history(data):
    """
    Displays all saved study sessions.
    """

    print("\n" + "=" * 60)
    print("                 STUDY HISTORY")
    print("=" * 60)

    if not data["study_history"]:
        print("No study sessions recorded yet.")
        return

    total_minutes = 0

    for session in data["study_history"]:

        print(
            f"{session['date']} | "
            f"{session['subject']} | "
            f"{session['minutes']} minutes"
        )

        total_minutes += session["minutes"]

    print("\n" + "-" * 60)

    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(
        f"Total Study Time: "
        f"{hours} hours {minutes} minutes"
    )

    print("=" * 60)

