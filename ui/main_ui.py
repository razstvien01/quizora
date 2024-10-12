import os

def print_intro():
  # os.system('clear')
  
  print("=" * 50)
  print(" Welcome to CSV-Exam Injector! ".center(50))
  print("=" * 50)
  print("Easily import CSV-based exam questions".center(50))
  print("and take randomized tests directly in your terminal.".center(50))
  print("=" * 50)
  
def print_menu():
  print("\n" + "=" * 50)
  print(" Main Menu ".center(50, "="))
  print("=" * 50)
  print("1. Import CSV".ljust(30) + " - Load questions")
  print("2. Start Exam".ljust(30) + " - Begin a test")
  print("3. View Scores".ljust(30) + " - Review results")
  print("4. Exit".ljust(30) + " - Close the console") 