from pages.menu import menu
from pages.csv_loader import load_exam_paths, load_questions
from pages.questions import ask_questions
from helper.utils import clear_screen, pause
from pages.xlsx_loader import XLSXLoader

def main():
  curr_exam_path = {}
  questions = []

  xlsx_loader = XLSXLoader()
  
  while True:
    clear_screen()
    menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == '1':
      curr_exam_path = load_exam_paths(curr_exam_path)

    elif choice == '2':
      clear_screen()
      questions = load_questions(curr_exam_path)

      if questions:
        clear_screen()
        print("\nYou selected to start an exam.\n")
        ask_questions(questions)
        pause()

    elif choice == '3':
      clear_screen()
      print("\nYou selected to view scores.")
      pause()

    elif choice == '4':
      clear_screen()
      print("\nYou selected to load xlsx paths.")
      curr_exam_path = xlsx_loader.load_exam_paths()

    elif choice == '6':
      clear_screen()
      print("\nExiting the application. Goodbye!")
      break


    else:
      print("\nInvalid option. Please select again.")
      pause()

if __name__ == "__main__":
  main()
