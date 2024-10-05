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
  
def ask_questions(questions):
  score = 0
  for i, (question, options, correct) in enumerate(questions, 1):
    print(f"Question {i}: {question}")
    
    for option in options:
      print(option)
      
    # * Input the user's answer
    answer = input("Choose your answer (A/B/C/D): ").upper()
    
    # * Check if the answer is correct
    if answer == correct:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {correct}.\n")
        
    # * Final score
    print(f"Your final score is {score}/{len(questions)}.")