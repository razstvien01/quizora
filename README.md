# QuizSheetLoader

## Overview
QuizSheetLoader is a command-line application that simplifies importing and managing exam questions stored in Excel files. This tool allows users to load questions from specified directories, start exams, and view scores.

## Features
- **Import CSV Files**: Easily import exam questions from Excel files in user-defined directories.
- **Dynamic Loading**: Select and load specific or all Excel files to prepare for an exam.
- **User-Friendly Interface**: Clear prompts guide users through the process.
- **Error Handling**: Graceful handling for file access and loading issues.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python libraries (install via `pip`)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
    ```bash
    cd CSV-ExamInjector
    ```
    
3. **Set up a virtual environment** (recommended):
   - For Windows:
     ```bash
     python -m venv .venv
     venv\Scripts\activate
     ```
   - For Linux or macOS:
     ```bash
     python3 -m venv .venv
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Installation
1. Run the application:
    ```bash
    python main.py
    ```
2. Follow the on-screen instructions to import exam paths and load questions.