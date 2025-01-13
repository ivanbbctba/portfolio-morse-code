# Morse Code Converter

A Python command-line application for **converting** text ↔ Morse code.  
Includes ASCII art banners, a looping interactive prompt, unit tests, and GitHub Actions CI.

---

## Features

1. **Text → Morse**  
   - Prompts the user for a string and converts it to Morse code.  
   - Uses `"/"` as a word separator and replaces unknown characters with `"???"`.

2. **Morse → Text**  
   - Converts user-input Morse code (split by spaces) back into readable text.  

3. **ASCII Art**  
   - Displays a welcome banner at startup and a goodbye banner on exit.

4. **Looping Prompt**  
   - Perform multiple conversions in one session.

5. **Unit Tests**  
   - A small suite covering both text-to-Morse and Morse-to-text.

6. **GitHub Actions CI**  
   - Automatically runs tests on every push or pull request to `main` or `dev`.

---

## Installation

We use [Pipenv](https://pipenv.pypa.io/en/latest/) for environment management, even though there are **no external dependencies**. This simply creates a clean virtual environment.

1. **Clone** the repository:
   ```bash
   git clone https://github.com/<your-username>/portfolio-morse-code.git
   cd portfolio-morse-code
   ```

2. **Install** using Pipenv:
   ```bash
   Since there are no external dependencies, this step just sets up a virtual environment with your current Python interpreter.
   ```
   
3. **Activate** the virtual environment:
   ```bash
   pipenv shell
   ```

## Usage
Once you're in the enviroment:
```bash
python main.py
```
    
## Workflow
Select a mode: [T] (Text → Morse) or [M] (Morse → Text).
Enter your text (if [T]) or Morse code (if [M]).
See the result.
Repeat until you choose to exit.
You’ll see ASCII art at startup and a goodbye ASCII art message when you choose to exit.

## Testing
```bash
python -m unittest discover tests
```

## Project Structure
```bash
portfolio-morse-code/
├── .github/
│   └── workflows/
│       └── python-tests.yml       # GitHub Actions for automated tests
├── morse_code_converter/          # Python package
│   ├── __init__.py
│   ├── ascii_art.py               # ASCII art functionality
│   └── morse_code.py              # Morse conversion logic
├── tests/
│   ├── __init__.py
│   └── morse_code_test.py         # Unit tests
├── main.py                        # Entry point (CLI)
├── .gitignore
├── LICENSE
├── Pipfile
├── Pipfile.lock
└── README.md
```
- morse_code_converter/: Contains the core modules (ASCII art and Morse logic).
- tests/: Holds unit tests for the converter logic.
- main.py: CLI script to run the app.
- .github/workflows/: GitHub Actions workflow for CI.
- Pipfile & Pipfile.lock: Manage the Pipenv virtual environment.
- LICENSE: GNU General Public License v3.0.





