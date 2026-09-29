# Smart Study Planner

## Overview

Smart Study Planner is a Python-based command-line created to help students with their studies and preparation for multiple examinations.

It stores the data about the subjects, for example, when to take the tests, their complexity level and progress and determines the subject’s priority based on this information. It considers the priority and available time and creates an optimal study plan.

Moreover, the system helps to track progress, see what subjects need to be studied, record the study sessions and keep the statistics.

## Features

* Student profile management
* Add and manage subjects
* Set examination dates
* Set subject difficulty levels
* Track subject preparation progress
* Calculate subject priority
* Generate a dynamic daily study plan
* Identify at-risk subjects
* Update subject progress
* Log study sessions
* View study history
* Remove subjects
* JSON-based data storage

## Technologies Used

* Python
* JSON
* Python Standard Library
* Command-Line Interface (CLI)

## Project Structure

```text
Smart-Study-Planner/
│
├── main.py
├── Datamanager.py
├── Subjectmanager.py
├── Prioritymanager.py
├── Studyplanner.py
├── track.py
├── student_data.json
├── README.md
└── statement.md
```

## Installation

### Requirements

* Python 3.x
* A computer with a command-line/terminal environment

The project uses Python's standard library, so no additional external Python packages are required.

## How to Run

### Step 1: Open the GitHub Repository

Visit the project repository:

**GitHub Repository:** [Click here to open Repository](https://github.com/ansh26bcy/Smart-Study-Planner.git)

### Step 2: Download the Project

Open the GitHub repository and click:

**Code → Download ZIP**

Extract the downloaded ZIP file on your computer.

### Step 3: Open the Project

Open the extracted `Smart-Study-Planner` folder.

Open a terminal inside the project folder.

### Step 4: Run the Program

Run the following command:

```bash
python main.py
```

### Step 5: Use the Program

After running the program, the main menu will appear.

Select an option by entering its corresponding number and follow the instructions displayed by the program.

```bash
python main.py
```

4. Follow the instructions displayed in the menu.

## How to Use

After starting the program, the main menu provides different options:

1. Create/Update Profile
2. Add Subject
3. View Subjects
4. Generate Today's Study Plan
5. Update Subject Progress
6. Show At-Risk Subjects
7. Log Study Session
8. View Study History
9. Remove Subject
10. Exit

The user can select an option by entering its corresponding number.

## Data Storage

The application uses a JSON file named `student_data.json` to store:

* Student information
* Subject information
* Examination dates
* Difficulty levels
* Preparation progress
* Study session history

The data is loaded when the program starts and updated when changes are made.

## Priority Calculation

The system calculates subject priority using:

* Examination urgency
* Subject difficulty
* Remaining syllabus/preparation work

The calculated priority score is then used to determine whether a subject has a High, Medium or Low priority.

## Study Plan Generation

The user inputs the amount of time they have for studying.

The system prioritizes the subjects and then allocates the time of study based on the prioritization.

Allocation is dependent upon the prioritization; subjects that are prioritized higher spend more time being studied than those with lower priority.

## Testing

The application can be tested by checking each major menu function individually.

Examples of validation tests include:

* Adding a valid subject
* Preventing duplicate subjects
* Entering an invalid examination date
* Entering an invalid difficulty value
* Entering progress outside the 0-100 range
* Generating a study plan with valid study hours
* Entering invalid study hours
* Logging a valid study session
* Entering invalid study-session duration
* Updating subject progress
* Removing a subject
* Viewing stored study history
