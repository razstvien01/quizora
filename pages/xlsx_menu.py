import os
import random
from typing import List
from collections import deque
from data.topicData import ExamDetails, IdentificationQuestion, MultipleAnswerQuestion, MultipleChoiceQuestion, TrueOrFalseQuestion,XLSXInfo, QuestionDetail
from helper.utils import clear_screen, pause
from services import excel_services
from services.excel_services import ExcelService

class XLSXMenu:
    def __init__(self):
        self.curr_exam_path = {}
        self.xlsx_infos : List[XLSXInfo] = []
        self.exam_details : ExamDetails = None

    def load_exam_paths(self):
      print("\nYou selected to import a XLSX file.")
      inputDone = False
      while not inputDone:
        path = input("Please input the exam folder path: ")

        if os.path.exists(path):
          if not os.path.isdir(path):
            choice = input("Specified path is not a folder do you want to continue? (Y/N): ")

            if choice in ("N", "n"):
                 inputDone = True
          else: 
            alias = os.path.dirname(path)

            if alias not in self.curr_exam_path:
              self.curr_exam_path[alias] = path
            else:
              print("The alias you entered already exists.")
            
            choice = input("Do you wish to add more exam paths? (Y/N): ")
            
            if choice in ("N", "n"):
              inputDone = True
            else: 
              print("Invalid input, please try again.")
        else:
          print("Invalid path. Please enter a valid path.")
        pause()
      return self.curr_exam_path


    def load_questions(self):
      self.xlsx_infos= []

      if self.curr_exam_path:
        print("\nSelect a path to load for the exam:")
        for i, (alias, path) in enumerate(self.curr_exam_path.items()):
          print(f"{i + 1}. {alias} -> {path}")
        
        file_choice = input("\nEnter the number of the path to load the exam from: ")
        try:
          file_choice_int = int(file_choice)
          selected_path = list(self.curr_exam_path.values())[file_choice_int - 1]
          selected_alias = list(self.curr_exam_path.values())[file_choice_int - 1]
          load_choice = input("Do you want to load all files in this path? (Y/N): ")

          if load_choice in ("Y", "y"):
            xlsx_files = [filename for filename in os.listdir(selected_path) if filename.endswith('.xlsx')]
            if not xlsx_files:
              print("\nNo XLSX files found in the selected path.")
              pause()
            else:
              xlsx_info = XLSXInfo(Alias=selected_alias)
              for filename in xlsx_files:
                file_path = os.path.join(selected_path, filename)

                excel_service = ExcelService(file_path)
                topic = excel_service.load()
                xlsx_info.Topics.append(topic)
                
                # questions.extend(load_questions_from_csv(file_path))
              self.xlsx_infos.append(xlsx_info)
              print(self.xlsx_infos)
              print("\nAll exam files have been successfully imported.")
              pause()
          else:
            filename = input("Enter the specific XLSX filename to load: ")
            file_path = os.path.join(selected_path, filename)
            if os.path.isfile(file_path):
              xlsx_info = XLSXInfo(Alias=filename)
              excel_service = ExcelService(file_path)
              topic = excel_service.load()
              xlsx_info.Topics.append(topic)
              self.xlsx_infos.append(xlsx_info)
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
        print("\nPlease import an exam file in XLSX format.")
        pause()

      return self.xlsx_infos


    def ask_questions(self):
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
        while(len(questions) > 0):
            question_detail = questions.popleft()
            clear_screen()
            print("Current Score: ", current_score, "/", total_score)
            print("Remaining Questions: ", len(questions))
            print("Topic Belonged: ", question_detail.Topic, ".", question_detail.QuestionGroup)
            print("Question: ")
            question = question_detail.Question
            print(question.Question)

            is_correct = False
            is_skipped = False

            if isinstance(question, TrueOrFalseQuestion):
                input_done = False
                while not input_done:
                  action = input("(S to skip) Answer (T/F): ")
                  if(action in ('T', 't', 'F', 'f')):
                    is_correct = action.lower() == question.Answer.lower() 
                    input_done = True

                  elif(action in ('S', 's')):
                     is_skipped = True
                     input_done = True

                  else:
                     print("Invalid input")
                     continue

            if isinstance(question, IdentificationQuestion):
                action = input("(N/A to skip) Answer: ")
                if(action.upper() != "N/A"):
                  is_correct = action.lower().strip() == question.Answer.lower().strip() if not question.IsCaseSensitive else action.strip() == question.Answer.strip()
                else:
                  is_skipped = True

            if isinstance(question, MultipleChoiceQuestion):
                input_done = False
                while not input_done:
                  choices = question.WrongAnswers + [question.CorrectAnswer]
                  random.shuffle(choices)
                  for index, choice in enumerate(choices):
                    print(index + 1, ": ", choice)
                  action = input("(S to skip) Answer: ")

                  if(action in ('S', 's')):
                     is_skipped = True
                     input_done = True
                  else:
                      try:
                        answer_int = int(action)
                        if(answer_int < 1 or answer_int > len(choices)):
                            print("Input not in Range")
                            continue

                        selected_choice = choices[answer_int - 1]
                        is_correct = selected_choice == question.CorrectAnswer
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
                    is_correct = all(correct_answer in selected_answers for correct_answer in question.CorrectAnswers)
                    input_done = True

                  elif(action in ('A', 'a', 'D', 'd')):
                      choice_selected = False

                      while not choice_selected:
                        answer = input("(X to go back) Select choice:")
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

            if(is_skipped):
              questions.append(question_detail)

            if(is_correct):
              print("Correct")
              current_score = current_score + question.Points
             
            pause()

        print("Total Score: ", current_score, "/", total_score)
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
