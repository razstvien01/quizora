import pandas as pd

class ExcelService:

    def __init__(self, name, age):
        self.df = None

    def load_sheet(self, sheet_path):
        self.df = pd.read_csv(sheet_path)
        print(self.df)

