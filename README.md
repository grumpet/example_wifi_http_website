# Flask Survey App

This is a simple Flask application that surveys users on whether they prefer dogs or cats. Users can enter their name, select their preference, and view the survey results in the form of a pie chart and a list of participants.

## Features

- Users can enter their name and select their preference (dogs or cats).
- The app displays a pie chart of the survey results.
- The app displays a list of participants and their preferences.
- Users cannot change their name or preference once submitted.

## Requirements

- Python 3.x
- Flask
- Flask-WTF
- Matplotlib
- python-dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-survey-app.git
    cd flask-survey-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your secret key:
    ```sh
    SECRET_KEY=your_secret_key
    ```

## Usage

1. Run the Flask app:
    ```sh
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000/`.

3. Enter your name and select your preference (dogs or cats).

4. View the survey results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.