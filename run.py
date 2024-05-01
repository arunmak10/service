import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_tests():
    try:
        # Run pytest with coverage
        subprocess.run(["pytest", "--cov=.", "--cov-report", "html", "--html=report.html"])
    except FileNotFoundError as e:
        logger.error(f"Error running tests: {e}")

def open_html_report():
    try:
        # Open the HTML coverage report
        subprocess.run(["open", "./htmlcov/index.html"])
        subprocess.run(["open", "report.html"])
    except FileNotFoundError as e:
        logger.error(f"Error opening HTML report: {e}")

if __name__ == "__main__":
    try:
        # Start the program
        run_tests()
    
        # Open HTML report
        open_html_report()
    except Exception as e:
        logger.error(f"Error starting the program: {e}")
    
    # Run tests
    
