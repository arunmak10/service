Here's the updated README.md with the instructions for running tests using `run.py`:

```markdown
# Field Service Portal

This is a Django-based web application for managing complaints, tasks, and worker details in a field service scenario.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (3.6 or higher)
- Django
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/arunmak10/service
```

2. Navigate to the project directory:

```bash
cd to the root directory of project
```

3. Set up a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
# For macOS/Linux
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Set up environment variables:
   - `DJANGO_SETTINGS_MODULE`: Django settings module (`field_service.settings` in this case). 
   -  export DJANGO_SETTINGS_MODULE="field_service.settings"
   - `PYTHONPATH`: Root directory of the project.
   - export $PYTHONPATH = .

2. Configure database settings in `settings.py`. By default, SQLite is used.

## Running the Application

1. Run database migrations:

```bash
python manage.py migrate
```

2. Start the development server:

```bash
python manage.py runserver
```

3. Access the application in your web browser at http://127.0.0.1:8000/.

## Running Tests

## Running Tests and Generating Coverage Report

To run tests and generate a coverage report, you can use the `auto_run()` method defined in `run.py`. Follow the steps below:

1. Ensure you are in the root directory of your project in the terminal.

2. Run the following command:

```bash
python -c "from run import auto_run; auto_run()"
```

This script will execute the following steps:
- Run pytest with coverage.
- Generate an HTML coverage report.
- Open the HTML coverage report in the default web browser.

## Additional Notes

- For more information on Django, refer to the [Django Documentation](https://docs.djangoproject.com/).
- Make sure to customize the application according to your specific requirements.

```

This README.md provides instructions for running the application, configuring environment variables, and running tests using the `run.py` script.