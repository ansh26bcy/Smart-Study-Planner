import datetime
from Datamanager import load_data, save_data
from Subjectmanager import create_profile, add_subject, display_subjects, remove_subject
from Prioritymanager import show_at_risk_subjects
from Studyplanner import generate_schedule
from track import update_progress, log_study_session, view_study_history

# SMART STUDY PLANNER
# MAIN MENU

def main():

    data = load_data()

    print("\n" + "=" * 60)
    print("              SMART STUDY PLANNER")
    print("       Dynamic Study Planning System")
    print("=" * 60)

    if data["student"].get("name"):

        print(
            f"\nWelcome back, "
            f"{data['student']['name']}!"
        )

    else:

        print("\nNo student profile found.")
        create_profile(data)

    while True:

        print("\n")
        print("=" * 60)
        print("                       MENU")
        print("=" * 60)

        print("1. Create / Update Profile")
        print("2. Add Subject")
        print("3. View Subjects")
        print("4. Generate Today's Study Plan")
        print("5. Update Subject Progress")
        print("6. Show At-Risk Subjects")
        print("7. Log Study Session")
        print("8. View Study History")
        print("9. Remove Subject")
        print("10. Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            create_profile(data)

        elif choice == "2":
            add_subject(data)

        elif choice == "3":
            display_subjects(data)

        elif choice == "4":
            generate_schedule(data)

        elif choice == "5":
            update_progress(data)

        elif choice == "6":
            show_at_risk_subjects(data)

        elif choice == "7":
            log_study_session(data)

        elif choice == "8":
            view_study_history(data)

        elif choice == "9":
            remove_subject(data)

        elif choice == "10":
            save_data(data)

            print("\nYour data has been saved.")
            print("Thank you !")
            print("Good luck with your studies!")

            break

        else:
            print(
                "\nInvalid choice. "
                "Please select an option from 1-10."
            )

# MAIN PROGRAM
if __name__ == "__main__":
    main()