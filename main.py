from data.topicData import QuestionGroup
from pages.menu import menu
from pages.questions import ask_questions
from helper.utils import clear_screen, pause
from pages.xlsx_menu import XLSXMenu
from repositories.main_repo import MainRepo

def main():
  xlsx_menu = XLSXMenu()

  while True:
    clear_screen()
    menu()
    choice = input("\nChoose an option (1-5): ")

    match choice:
      case '1':
        clear_screen()
        print("\nYou selected to import Excel folder.")
        xlsx_menu.load_exam_paths()

      case '2':
        clear_screen()
        print("\nYou selected to view the Excel folders.")
        xlsx_menu.view_exam_paths()

      case '3':
        clear_screen()
        print("\nYou selected to load XLSX questions.")
        xlsx_menu.load_questions()

      case '4':
        clear_screen()
        print("\nYou selected to start the exam.")
        xlsx_menu.start_exam()

      case '5':
        clear_screen()
        print("\nExiting the application. Goodbye!")
        break

      case _:
        print("\nInvalid option. Please select again.")
        pause()


if __name__ == "__main__":
  main()
