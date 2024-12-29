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