import datetime
from Datamanager import save_data
from Prioritymanager import calculate_priority
# CREATE or UPDATE STUDENT PROFILE

def create_profile(data):
    """
    Creates or updates the student's profile.
    """

    print("\n" + "=" * 50)
    print("             STUDENT PROFILE")
    print("=" * 50)

    current_name = data["student"].get("name", "")

    if current_name:
        print(f"Current name: {current_name}")

        name = input("Enter new name (press Enter to keep current): ").strip()

        if name == "":
            name = current_name

    else:
        while True:
            name = input("Enter your name: ").strip()

            if name:
                break

            print("Name cannot be empty.")

    data["student"]["name"] = name

    save_data(data)

    print(f"\nProfile saved successfully, {name}!")

# ADD SUBJECT

def add_subject(data):
    """
    Adds a new subject to the student's subject list.
    """

    print("\n" + "=" * 50)
    print("                ADD SUBJECT")
    print("=" * 50)

    while True:
        name = input("Enter subject name: ").strip()

        if not name:
            print("Subject name cannot be empty.")
            continue

        
        duplicate = False

        for subject in data["subjects"]:
            if subject["name"].lower() == name.lower():
                duplicate = True
                break

        if duplicate:
            print("This subject already exists.")
            return

        break

    
    while True:
        exam_date = input(
            "Enter exam date (DD-MM-YYYY): "
        ).strip()

        try:
            exam = datetime.datetime.strptime(exam_date, "%d-%m-%Y").date()

            if exam < datetime.date.today():
                print("Exam date cannot be in the past.")
                continue

            break

        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY.")

    while True:
        try:
            difficulty = int(
                input("Enter difficulty level (1-5): ")
            )

            if 1 <= difficulty <= 5:
                break

            print("Difficulty must be between 1 and 5.")

        except ValueError:
            print("Please enter a number between 1 and 5.")

    while True:
        try:
            progress = float(
                input("Enter current progress (0-100%): ")
            )

            if 0 <= progress <= 100:
                break

            print("Progress must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    subject = {
        "name": name,
        "exam_date": exam.strftime("%d-%m-%Y"),
        "difficulty": difficulty,
        "progress": progress
    }

    data["subjects"].append(subject)

    save_data(data)

    print("\nSubject added successfully!")

# DISPLAY SUBJECTS

def display_subjects(data):
    """
    Displays all saved subjects with their current priority.
    """

    print("\n" + "=" * 75)
    print("                     YOUR SUBJECTS")
    print("=" * 75)

    if not data["subjects"]:
        print("No subjects have been added yet.")
        return

    for index, subject in enumerate(data["subjects"], start=1):

        score, priority, days_left = calculate_priority(subject)

        print(f"\n{index}. {subject['name']}")
        print(f"   Exam Date       : {subject['exam_date']}")
        print(f"   Days Remaining  : {max(days_left, 0)}")
        print(f"   Difficulty      : {subject['difficulty']}/5")
        print(f"   Progress        : {subject['progress']:.1f}%")
        print(f"   Remaining Work  : {100 - subject['progress']:.1f}%")
        print(f"   Priority Score  : {score:.2f}")
        print(f"   Priority Level  : {priority}")

    print("=" * 75)

# REMOVE SUBJECT

def remove_subject(data):
    """
    Removes a subject from the planner.
    """

    print("\n" + "=" * 50)
    print("              REMOVE SUBJECT")
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
                input("\nEnter subject number to remove: ")
            )

            if 1 <= choice <= len(data["subjects"]):
                break

            print("Invalid subject number.")

        except ValueError:
            print("Please enter a valid number.")

    removed = data["subjects"].pop(choice - 1)

    save_data(data)

    print(
        f"\n{removed['name']} removed successfully."
    )