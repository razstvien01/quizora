from services.csv_services import *

file_path = 'exam_files/questions.csv'
questions = load_questions_from_csv(file_path)
ask_questions(questions)