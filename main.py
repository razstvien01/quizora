from ui.main_ui import *
from services.csv_services import *
from helper.utils import *

def main():
  curr_exam_path = {}
  questions = []
  
  while True:
    print_intro()
    print_menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == '1':
      print("\nYou selected to import a CSV file.")
      
      ctr = True
      while ctr:
        path = input("Please input the exam folder path: ")
        
        if os.path.exists(path):
          alias = input("Please enter an alias for this path: ")
          if alias not in curr_exam_path:
            curr_exam_path[alias] = path
          else:
            print("The alias you entered already exists.")
          
          while True:
            choice = input("Do you wish to add more exam paths? (Y/N): ")
            if choice in ("Y", "y"):
              break
            elif choice in ("N", "n"):
              ctr = False
              break
            else: 
              print("Invalid input, please try again.")
        else:
          print("Invalid path. Please enter a valid path.")
    
    elif choice == '2':
      if curr_exam_path:
        print("\nSelect a path to load for the exam:")
        
        for i, (alias, path) in enumerate(curr_exam_path.items()):
          print(f"{i + 1}. {alias} -> {path}")
        
        file_choice = input("\nEnter the number of the path to load the exam from: ")
        
        try:
          selected_path = list(curr_exam_path.values())[int(file_choice) - 1]
          load_choice = input("Do you want to load all files in this path? (Y/N): ")

          if load_choice in ("Y", "y"):
            # Load all CSV files in the selected directory
            questions = []
            for filename in os.listdir(selected_path):
              if filename.endswith('.csv'):
                file_path = os.path.join(selected_path, filename)
                questions.extend(load_questions_from_csv(file_path))
            print("\nAll exam files have been successfully imported.")
          else:
            filename = input("Enter the specific CSV filename to load: ")
            questions = load_questions_from_csv(os.path.join(selected_path, filename))
            print("\nThe exam file has been successfully imported.")

        except (ValueError, IndexError):
          print("\nInvalid selection. Please choose a valid file number.")
        except FileNotFoundError:
          print("\nError: The specified file was not found. Please check the file path.")
        except IOError:
          print("\nError: There was an issue reading the file. Please ensure it's accessible.")
        except Exception as e:
          print(f"\nUnexpected error occurred: {str(e)}") 
      else:
        print("\nPlease import an exam file in CSV format.")

      if questions:
        print("\nYou selected to start an exam.\n")
        ask_questions(questions)

    elif choice == '3':
      print("\nYou selected to view scores.")
    elif choice == '4':
      print("\nExiting the application. Goodbye!")
      break
    else:
      print("\nInvalid option. Please select again.")

if __name__ == "__main__":
  main()
