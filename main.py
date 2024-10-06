from ui.main_ui import *
from services.csv_services import *

def main():
  print_intro()
  
  curr_exam_path = ""
  questions = []
  
  while True:
    print_menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == '1':
      print("\nYou selected to import a CSV file.")
      
      curr_exam_path = input("Please input the exam file path: ")
      
      try:
        questions = load_questions_from_csv(curr_exam_path)
        
        print("\nThe inputted file has been successfully imported.")
      except FileNotFoundError:
        print("\nError: The specified file was not found. Please check the file path.")
      except IOError:
        print("\nError: There was an issue reading the file. Please ensure it's accessible.")
      except Exception as e:
        print(f"\nUnexpected error occured: {str(e)}") 
      
    elif choice == '2':
      
      if curr_exam_path and questions:
        print("\nYou selected to start an exam.")
        ask_questions(questions)
      
      else:
        print("\n Please import an exam file in CSV format.")
        
      
    elif choice == '3':
      print("\nYou selected to view scores.")
    elif choice == '4':
      print("\nExiting the application. Goodbye!")
      break
    else:
      print("\nInvalid option. Please select again.")

if __name__ == "__main__":
  main()
  