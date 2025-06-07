# Dhivehi Reference Generator (Web-Based)

This application provides a web interface to generate academic references in a Dhivehi format.

## Setup and Installation

1.  **Ensure Python is installed.**
    This application requires Python 3.x.

2.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    *(Replace `<repository_url>` and `<repository_directory>` with actual values if applicable, otherwise omit this step if running locally)*

3.  **Install Flask:**
    Open your terminal or command prompt and run:
    ```bash
    pip install Flask
    ```

## Running the Application

1.  **Navigate to the directory containing `app.py`.**

2.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    Or, if you are using the `flask` command:
    ```bash
    flask run
    ```
    (You might need to set `FLASK_APP=app.py` as an environment variable for the `flask run` command to work directly: `export FLASK_APP=app.py` on Linux/macOS or `set FLASK_APP=app.py` on Windows).

3.  **Open your web browser:**
    Navigate to `http://127.0.0.1:5000/`.

    You should see the Dhivehi Reference Generator interface. Fill in the form fields and click "Generate Reference" to see the output.

## Files

-   `app.py`: Contains the Flask web application logic.
-   `dhivehi_reference_generator.py`: Contains the core Python function to generate the reference string.
-   `templates/index.html`: The HTML template for the web interface.
-   `README.md`: This file.
