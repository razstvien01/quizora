import csv

def load_questions_from_csv(file_path):
  questions = []
  with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    
    #* Skipping the first row (column header)
    next(reader) 
    
    for row in reader:
      question = row[0]
      options = [f"A. {row[1]}", f"B. {row[2]}", f"C. {row[3]}", f"D. {row[4]}"]
      correct_answer = row[5].upper()
      
      questions.append((question, options, correct_answer))
    
    return questions
  
