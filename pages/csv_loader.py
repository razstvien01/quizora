import os
from services.csv_services import load_questions_from_csv
from helper.utils import pause

def load_exam_paths(curr_exam_path):
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
    pause()
  return curr_exam_path

def load_questions(curr_exam_path):
  questions = []
  if curr_exam_path:
    print("\nSelect a path to load for the exam:")
    for i, (alias, path) in enumerate(curr_exam_path.items()):
      print(f"{i + 1}. {alias} -> {path}")
    
    file_choice = input("\nEnter the number of the path to load the exam from: ")
    try:
      selected_path = list(curr_exam_path.values())[int(file_choice) - 1]
      load_choice = input("Do you want to load all files in this path? (Y/N): ")

      if load_choice in ("Y", "y"):
        csv_files = [filename for filename in os.listdir(selected_path) if filename.endswith('.csv')]
        if not csv_files:
          print("\nNo CSV files found in the selected path.")
          pause()
        else:
          for filename in csv_files:
            file_path = os.path.join(selected_path, filename)
            questions.extend(load_questions_from_csv(file_path))
          print("\nAll exam files have been successfully imported.")
          pause()
      else:
        filename = input("Enter the specific CSV filename to load: ")
        file_path = os.path.join(selected_path, filename)
        if os.path.isfile(file_path):
          questions = load_questions_from_csv(file_path)
          print("\nThe exam file has been successfully imported.")
          pause()
        else:
          print("\nError: The specified file was not found. Please check the file name.")
          pause()

    except (ValueError, IndexError):
      print("\nInvalid selection. Please choose a valid file number.")
      pause()
    except FileNotFoundError:
      print("\nError: The specified file was not found. Please check the file path.")
      pause()
    except IOError:
      print("\nError: There was an issue reading the file. Please ensure it's accessible.")
      pause()
    except Exception as e:
      print(f"\nUnexpected error occurred: {str(e)}")
      pause()
  else:
    print("\nPlease import an exam file in CSV format.")
    pause()

  return questions
