from data.topicData import QuestionGroup
from pages.menu import menu
from pages.questions import ask_questions
from helper.utils import clear_screen, pause
from pages.xlsx_menu import XLSXMenu

def main():
  curr_exam_path = {}
  questions = []

  xlsx_menu = XLSXMenu()

  while True:
    clear_screen()
    menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == '1':
      clear_screen()
      print("\nYou selected to import Excel folder.")
      xlsx_menu.load_exam_paths()

    elif choice == '2':
      clear_screen()
      print("\nYou selected to load XLSX questions.")
      xlsx_menu.load_questions()
      
    elif choice == '3':
      clear_screen()
      print("\nYou selected to start the exam.")
      xlsx_menu.start_exam()
      
    elif choice == '4':
      clear_screen()
      print("\nExiting the application. Goodbye!")
      break

    else:
      print("\nInvalid option. Please select again.")
      pause()

if __name__ == "__main__":
  main()
