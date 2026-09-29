import json
import os
DATA_FILE = "student_data.json"
# SAVED DATA

def load_data():

    if not os.path.exists(DATA_FILE):
        return {
            "student": {},
            "subjects": [],
            "study_history": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    
        if "student" not in data:
            data["student"] = {}

        if "subjects" not in data:
            data["subjects"] = []

        if "study_history" not in data:
            data["study_history"] = []

        return data

    except (json.JSONDecodeError, OSError):
        print("\nCould not read the saved data.")
        print("Starting with a fresh data file.\n")

        return {
            "student": {},
            "subjects": [],
            "study_history": []
        }

# SAVE DATA

def save_data(data):
    """
    Saves all student information to the JSON file.
    """

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:
        print("\nError: Could not save the data.")
        return False