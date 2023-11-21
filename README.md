# Anonymous Information Submission App

## Overview

This is a simple Python application that allows users to submit information anonymously. The app uses a graphical user interface (GUI) created with Tkinter, a standard GUI toolkit for Python.

## Features

- Users can submit information without providing personal details.
- Submissions are recorded with a unique identifier, timestamp, and the provided information.
- Submitted data is saved to a JSON file (`anonymous_submissions.json`).

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/temwni-msiska/silentsubmission.git
    ```

2. Navigate to the project directory:

    ```bash
    cd anonymous-info-app
    ```

3. Run the app:

    ```bash
    python app.py
    ```

4. The app window will appear with two buttons:
    - **Submit Information:** Opens a popup window for submitting information.
    - **Exit:** Closes the app.

5. Click the "Submit Information" button, enter the information in the popup window, and click OK.
6. A success message will appear, confirming the submission.

## Requirements

- Python 3.x
- Tkinter (usually included with Python, if not, install using `pip install tk`)

## Notes

- This app is designed for simple use cases where users can submit information anonymously.
- No personal data, such as names, is collected.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and extend the app according to your needs. If you encounter any issues or have suggestions, please open an issue or submit a pull request.

Happy submitting!
