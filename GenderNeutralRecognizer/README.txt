GENDER NEUTRAL LANGUAGE RECOGNIZER

DESCRIPTION
This desktop application opens a text file, detects 10 predefined gender-specific terms using regular expressions, and displays their occurrence counts and suggested gender-neutral alternatives. Matching ignores capitalization and avoids matching terms within larger words. The original file is not modified; review suggestions in context.

REQUIREMENTS
- Python 3 with Tkinter installed.
- No third-party Python packages are required.
- Input files must be .txt files saved as UTF-8 (with or without a byte-order mark).

PROJECT FILES
recognizer.py - Application source code.
sample.txt   - Sample input for demonstrating the application.
README.txt   - Setup and running instructions.

HOW TO RUN ON WINDOWS
1. Install Python 3 with Tkinter if it is not already installed.
2. If you received a ZIP file, extract it first.
3. Open the GenderNeutralRecognizer folder in File Explorer.
4. Click the File Explorer address bar, type cmd, and press Enter.
   This opens Command Prompt inside the project folder.
5. Enter this command and press Enter:

   py recognizer.py

   If the py command is unavailable but Python is installed and accessible,
   try:

   python recognizer.py

6. In the application, click "Open a .txt file".
7. Select the included sample.txt file and click Open.
8. Review the Detected term, Occurrences, and Suggested alternative columns.
9. Click "Open a .txt file" again to analyze another file.
10. Close the application window when finished.







