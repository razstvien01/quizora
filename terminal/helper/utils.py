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
    
def get_new_path(self):
  new_path = input("Enter the new path: ").strip()
  if os.path.exists(new_path) and os.path.isdir(new_path):
    return new_path
  return None
