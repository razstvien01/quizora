import sqlite3

from repositories.main_repo import MainRepo

class PathRepo(MainRepo):
  def __init__(self):
    super().__init__()
    
  def save_exam_path(self, alias: str, path: str) -> bool:
    try:
      with sqlite3.connect(self, self.DB_PATH) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
          INSERT INTO exam_paths (alias, path) VALUES (?, ?)
        ''', (alias, path))
        
        conn.commit()
        
        return True
    except sqlite3.IntegrityError:
      print(f"Error: The path '{path}' already exists in the database.")
      return False
    except sqlite3.Error as e:
      print(f"Database error: {e}")
      return False
    
  
  def get_exam_paths(self) -> dict:
    try:
      with sqlite3.connect(self.DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT alias, path FROM exam_paths")
        return dict(cursor.fetchall())
    except sqlite3.Error as e:
      print(f"Database error: {e}")
      return {}
    
  def delete_exam_path(self, alias: str) -> bool:
    try:
      with sqlite3.connect(self.DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM exam_paths WHERE alias = ?", (alias,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
      print(f"Database error: {e}")
      return False