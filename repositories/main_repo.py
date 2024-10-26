import sqlite3

class MainRepo:
  def __init__(self):
    self.DB_PATH = "system.db"
  
  def initialize_db(self):
    try:
      with sqlite3.connect(self.db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS exam_paths (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alias TEXT UNIQUE NOT NULL,
            path TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          )
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
      print(f"Database error: {e}")