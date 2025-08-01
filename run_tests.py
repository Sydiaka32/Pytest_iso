import pytest
import datetime
import os
import sys

# Create the reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Generate timestamp for report filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = f"reports/report_{timestamp}.html"

# Optional: pass file path as a command-line argument
if len(sys.argv) > 1:
    test_target = sys.argv[1]
else:
    test_target = "tests"  # Default folder if no path is given

# Run pytest with HTML report
pytest.main([test_target, f"--html={report_path}", "--self-contained-html"])
