import os
import random
from typing import List
from collections import deque
from data.topicData import ExamDetails, IdentificationQuestion, MultipleAnswerQuestion, MultipleChoiceQuestion, TrueOrFalseQuestion,XLSXInfo, QuestionDetail
from helper.utils import clear_screen, pause, get_new_path
from ui.confirm import confirm_update, confirm_delete
from services.excel_services import ExcelService
from repositories.path_repo import PathRepo

class XLSXMenu:
    def __init__(self):
        self.path_repo = PathRepo()
        self.exam_paths = self.path_repo.get_exam_paths()
        self.xlsx_infos : List[XLSXInfo] = []
        self.exam_details : ExamDetails = None
    
    def view_exam_paths(self):
      self.exam_paths = self.path_repo.get_exam_paths()
      
      if not self.exam_paths:
        print("There are no saved Excel folder paths.\n")
        pause()
        return
      
      print("Excel Folders:")
      for i, (alias, path) in enumerate(self.exam_paths.items()):
        print(f"{i + 1}. {alias} -> {path}")
      
      action = input("\nDo you want to edit or delete any path? (edit/delete/none): ").strip().lower()
      
      match action:
        case "none":
          print("No changes made.\n")
          pause()
        case "edit":
          self.handle_edit_path()
        case "delete":
          self.handle_delete_path()
        case _:
          print("Invalid choice. No changes made.\n")
          pause()
      
    def get_path_by_index(self, index):
      if 0 <= index < len(self.exam_paths):
        return list(self.exam_paths.items())[index]
      return None, None
    
    def handle_edit_path(self):
      try:
        index = int(input("Enter the number of the path to edit: ")) - 1
        alias, old_path = self.get_path_by_index(index)
        
        if alias is None:
          print("Invalid choice. No path exists at this index.")
          return
        
        print(f"\nYou are editing:  {alias} -> {old_path}")
        
        new_path = get_new_path()
        if new_path is None:
          print("Invalid path. Please ensure the directory exists.\n")
          pause()
          return
        
        if not confirm_update(alias, old_path, new_path):
          print("Update canceled.")
          return
        
        if self.path_repo.update_exam_path(alias, new_path):
            print("Path updated successfully.")
            self.exam_paths[alias] = new_path
        else:
          print("Failed to update the path.")
            
      except ValueError:
        print("Invalid input. Please enter a valid number.")
        
      print()
      pause()
      
    def handle_delete_path(self):
      try:
        index = int(input("Enter the number of the path to delete: ")) - 1
        alias, old_path = self.get_path_by_index(index)
        
        if alias is None:
          print("\nInvalid choice. No path exists at this index.")
          pause()
          return
        
        print(f"\nYou are to delete: {alias} -> {old_path}")
        
        if not confirm_delete(alias, old_path):
          print("\nDeletion canceled.")
          pause()
          return
        
        
        if self.path_repo.delete_exam_path(alias):
          print("Path deleted successfully.")
          del self.exam_paths[alias]
        else:
          print("Failed to delete the path.")
          
      except ValueError:
        print("Invalid input. Please enter a valid number.")
        
      print()
      pause()
    
    def load_exam_paths(self):
      inputDone = False
      while not inputDone:
        path = input("Please input the exam folder directory (or type 'back' to go back): ")
        
        if path.lower() == 'back':
          print("Going back to the previous menu...")
          inputDone = True
          return None

        if os.path.exists(path):
          if not os.path.isdir(path):
            choice = input("Specified directory is not a folder. Do you want to continue? (Y/N): ")

            if choice in ("N", "n"):
              inputDone = True
          else: 
            alias = os.path.basename(path)

            if alias not in self.exam_paths:
              if self.path_repo.save_exam_path(alias, path):
                self.exam_paths[alias] = path
                print("New path added successfully.\n")
            else:
              print("The path you entered already exists.")
            
            choice = input("Do you wish to add more exam paths? (Y/N): ")
            
            if choice in ("N", "n"):
              inputDone = True
            elif choice not in ("Y", "y"): 
              print("Invalid input, please try again.")
        else:
          print("Invalid path. Please enter a valid path.")
        pause()
      return self.exam_paths


    def load_questions(self):
      self.xlsx_infos= []

      if self.exam_paths:
        print("\nSelect a folder to load for the exam:")
        for i, (alias, path) in enumerate(self.exam_paths.items()):
          print(f"{i + 1}. {alias} -> {path}")
        print("0. Go back")
        
        file_choice = input("\nEnter the number of folder to load the exam from: ")
        
        if file_choice == "0":
          print("\nOperation cancelled.")
          pause()
          return
        
        try:
          file_choice_int = int(file_choice)
          selected_path = list(self.exam_paths.values())[file_choice_int - 1]
          selected_alias = list(self.exam_paths.values())[file_choice_int - 1]
          
          
          xlsx_files = [filename for filename in os.listdir(selected_path) if filename.endswith('.xlsx')]
          if not xlsx_files:
            print("\nNo XLSX files found in the selected path.")
            pause()
            return
            
          print("\nXLSX Files:")
          for i, filename in enumerate(xlsx_files):
            if filename.startswith('~$'):
              continue
            print(f"{i + 1}. {filename}")
          
          load_choice = input("\nDo you want to load all files in this path? (Y/N): ").lower()

          if load_choice == "y":
            xlsx_files = [filename for filename in os.listdir(selected_path) if filename.endswith('.xlsx') and filename.startswith('~$') == False]
            
            if not xlsx_files:
              print("\nNo XLSX files found in the selected path.")
              pause()
            else:
              xlsx_info = XLSXInfo(Alias=selected_alias)
              for filename in xlsx_files:
                file_path = os.path.join(selected_path, filename)

                excel_service = ExcelService(file_path)
                topic = excel_service.load()
                
                 # Check if there are no loaded questions
                if not topic.QuestionGroups or all(
                    not (qg.TrueOrFalseQuestions or qg.IdentificationQuestions or qg.MultipleChoiceQuestions or qg.MultipleAnswerQuestions)
                    for qg in topic.QuestionGroups
                ):
                    print("\nNo questions were loaded. Please add questions to the file.")
                    pause()
                    return
                
                xlsx_info.Topics.append(topic)
              
              self.xlsx_infos.append(xlsx_info)
              print("\nAll exam files have been successfully imported.")
              pause()
          elif load_choice == "n":
            file_index = int(input("Enter te number of the specific XLSX file to load: "))
            try:
              filename = xlsx_files[file_index - 1]
              file_path = os.path.join(selected_path, filename)
              
              if os.path.isfile(file_path):
                xlsx_info = XLSXInfo(Alias=filename)
                excel_service = ExcelService(file_path)
                topic = excel_service.load()
                xlsx_info.Topics.append(topic)
                self.xlsx_infos.append(xlsx_info)
                print("\nExam file has been successfully imported.")
                pause()
            except (ValueError, IndexError):
              print("\nInvalid selection. Please choose a valid file number.")
              pause()
          else:
            print("\nInvalid input. Please try again.")
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
        print("\nPlease import an exam file in XLSX format.")
        pause()

      return self.xlsx_infos


    def start_exam(self):
        if not self.xlsx_infos:
          print("You need to load the desired excel files first before taking an exam.\n")
          pause()
          return
          
        question_details = self._get_question_infos()
        print("Topics Covered: ", )
        for topic in question_details.TopicsCovered:
            print(topic)

        total_questions = len(question_details.QuestionDetails)
        total_score = question_details.TotalPossibleScore
        print("\n\nTotal Items: ", total_questions)
        print("Total Possble Score: ", total_score)
        pause();

        random.shuffle(question_details.QuestionDetails)
        
        questions = deque(question_details.QuestionDetails)
        current_score = 0
        while len(questions) > 0:
            question_detail = questions.popleft()
            clear_screen()
            print("Current Score: ", int(current_score), "/", int(total_score))
            print("Remaining Questions: ", len(questions))
            print("Topic Belonged: ", question_detail.Topic, ".", question_detail.QuestionGroup)
            print("Question: ")
            question = question_detail.Question
            print(question.Question)

            is_correct = False
            is_skipped = False
            curr_notes = None

            if isinstance(question, TrueOrFalseQuestion):
                input_done = False
                while not input_done:
                  answer = input("(S to skip) Answer (T/F): ").strip()
                  if(answer in ('T', 't', 'F', 'f')):
                    is_correct = answer.lower() == question.Answer.lower() 
                    input_done = True
                    curr_notes = question.Notes

                  elif(answer in ('S', 's')):
                     is_skipped = True
                     input_done = True

                  else:
                     print("Invalid input")
                     continue

            if isinstance(question, IdentificationQuestion):
                if question.IsCaseSensitive:
                  print("Note: A case-sensitive answer")
                  
                answer = input("(N/A to skip) Answer: ")
                if(answer.upper() != "N/A"):
                  is_correct = answer.lower().strip() == question.Answer.lower().strip() if not question.IsCaseSensitive else answer.strip() == question.Answer.strip()
                  curr_notes = question.Notes
                else:
                  is_skipped = True

            if isinstance(question, MultipleChoiceQuestion):
                input_done = False
                while not input_done:
                  correct_keys_list = list(question.CorrectAnswerWNotes.keys())
                  wrong_keys_list = list(question.WrongAnswersWNotes.keys())
                  
                  choices = correct_keys_list + wrong_keys_list
                  random.shuffle(choices)
                  for index, choice in enumerate(choices):
                    print(index + 1, ": ", choice)
                  action = input("(S to skip) Answer: ")

                  if action.lower() == 's':
                    is_skipped = True
                    input_done = True
                  else:
                      try:
                        answer_int = int(action)
                        if(answer_int < 1 or answer_int > len(choices)):
                            print("Input not in Range")
                            continue

                        selected_choice = choices[answer_int - 1]
                        
                        correct_key = correct_keys_list[0]
                        is_correct = selected_choice == correct_key
                        
                        if is_correct:
                          curr_notes = question.CorrectAnswerWNotes[selected_choice]
                        else:
                          curr_notes = question.WrongAnswersWNotes[selected_choice]
                          
                        input_done = True

                      except:
                        print("Invalid Input")
                      
            if isinstance(question, MultipleAnswerQuestion):
                input_done = False
                inputs = []
                choices = question.WrongAnswers + question.CorrectAnswers
                random.shuffle(choices)
                while not input_done:
                  for index, choice in enumerate(choices):
                    print(index + 1, ": ", choice, " (Selected)" if index in inputs else "")
                  action = input("(S to skip) (C to confirm) (A to Select) (D to Deselect) Choose Action: ")

                  if(action in ('S', 's')):
                    is_skipped = True
                    input_done = True
                  elif(action in ('C', 'c')):
                    selected_answers = list(map(lambda index: choices[index], inputs))
                    is_correct = all(correct_answer in selected_answers for correct_answer in question.CorrectAnswers) and all(wrong_answer not in selected_answers for wrong_answer in question.WrongAnswers)
                    curr_notes = question.Notes
                    input_done = True

                  elif(action in ('A', 'a', 'D', 'd')):
                      choice_selected = False

                      while not choice_selected:
                        answer = input("(X to go back) Select choice: ")
                        if(answer in ('X', 'x')):
                            choice_selected = True
                        else:
                            try:
                              answer_int = int(answer)
                              if(answer_int < 1 or answer_int > len(choices)):
                                  print("Input not in Range")
                                  continue
                              
                              answer_index = answer_int - 1

                              if(answer_index in inputs and action in ('A', 'a')):
                                  print("Input already selected")
                                  continue 
                              
                              if(answer_index not in inputs and action in ('D', 'd')):
                                  print("Input is not selected")
                                  continue 

                              if(action in ('A', 'a')):
                                  inputs.append(answer_index )
                              else:
                                  inputs.remove(answer_index )
                              choice_selected = True
                            except:
                              print("Invalid Input")
                  else:
                    print("Invalid Action")

            if is_skipped:
              questions.append(question_detail)
            
            elif is_correct:
              print("Correct!")
              print(curr_notes)
              current_score = current_score + question.Points
            else:
              print("Wrong!")
              print(curr_notes)
            
            pause()
        
        clear_screen()
        print("Exam completed!!!\nTotal Score: ", current_score, "/", total_score)
        pause()

    def _get_question_infos(self) -> ExamDetails:
        exam_details = ExamDetails()

        for xlsx_info in self.xlsx_infos:
          for topic in xlsx_info.Topics:
            for question_group in topic.QuestionGroups:
              related_topic = topic.Name + " : " + question_group.Name
              if(related_topic not in exam_details.TopicsCovered):
                exam_details.TopicsCovered.append(related_topic)
            
              
              for question in question_group.TrueOrFalseQuestions:
                question_detail = QuestionDetail(Topic = topic.Name, QuestionGroup = question_group.Name, Question=question)
                exam_details.QuestionDetails.append(question_detail)
                exam_details.TotalPossibleScore = exam_details.TotalPossibleScore + question.Points

              for question in question_group.IdentificationQuestions:
                question_detail = QuestionDetail(Topic = topic.Name, QuestionGroup = question_group.Name, Question=question)
                exam_details.TotalPossibleScore = exam_details.TotalPossibleScore + question.Points
                exam_details.QuestionDetails.append(question_detail)

              for question in question_group.MultipleChoiceQuestions:
                question_detail = QuestionDetail(Topic = topic.Name, QuestionGroup = question_group.Name, Question=question)
                exam_details.TotalPossibleScore = exam_details.TotalPossibleScore + question.Points
                exam_details.QuestionDetails.append(question_detail)

              for question in question_group.MultipleAnswerQuestions:
                question_detail = QuestionDetail(Topic = topic.Name, QuestionGroup = question_group.Name, Question=question)
                exam_details.TotalPossibleScore = exam_details.TotalPossibleScore + question.Points
                exam_details.QuestionDetails.append(question_detail)

        return exam_details
      
