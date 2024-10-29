def print_intro():
  print("=" * 75)
  print(" Welcome to QuizSheetLoader! ".center(75))
  print("=" * 75)
  print("Easily import Excel-based exam questions".center(75))
  print("and take randomized tests directly in your terminal.".center(75))
  print("=" * 75)

def print_menu():
  print("\n" + "=" * 75)
  print(" MAIN MENU ".center(75, "="))
  print("=" * 75)
  print("1. Import Excel Folder      - Import all Excel files from a folder") 
  print("2. View Saved Excel Folders - View all available Excel folders") 
  print("3. Load XLSX Questions      - Select and load questions from Excel files") 
  print("4. Start Exam (XLSX)        - Begin the test with loaded questions")
  print("5. Exit                     - Close the application") 


def menu():
  print_intro()
  print_menu()
