import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def check_path_exists(path):
  if os.path.exists(path):
      return True
  return False

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def pause(message="Press Enter to continue..."):
  input(message)