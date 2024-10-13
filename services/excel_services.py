import os
from numpy import result_type
import pandas as pd
from data.topicData import IdentificationQuestion, QuestionGroup, Topic, TrueOrFalseQuestion

class ExcelService:
    QUESTION_COLUMN = "Questions"
    ANSWER_COLUMN = "Answer"
    POINTS_COLUMN = "Points"

    ISCASESENSITIVE_COLUMN = "IsCaseSensitive"

    def __init__(self, excel_path : str):
        self.sheet_path = excel_path
        self.excel_file = pd.ExcelFile(excel_path)
        
        topicName = os.path.basename(excel_path)
        self.data : Topic = Topic(Name=topicName)
        print(self.data)


    def load(self):
        # Check question groups
        for question_group in self._get_question_groups():
            self._load_question_group(question_group)

        return self.data


    def _load_question_group(self, question_group_name : str):
        question_group = QuestionGroup(Name=question_group_name)
        
        self._load_trueorfalse(question_group)
        self._load_identification(question_group)

    def _load_identification(self, question_group : QuestionGroup):
        sheet_name = question_group.Name + "@identification"

        if(sheet_name not in self._get_sheets()):
            return

        df = pd.read_excel(self.sheet_path, sheet_name)

        for _, row in df.iterrows():
            question = IdentificationQuestion(Question=row[self.QUESTION_COLUMN], 
                                              Answer=row[self.ANSWER_COLUMN], 
                                              Points=row[self.POINTS_COLUMN],
                                              IsCaseSensitive=row[self.ISCASESENSITIVE_COLUMN])
            question_group.IdentificationQuestions.append(question)
        

    def _load_trueorfalse(self, question_group : QuestionGroup):
        sheet_name = question_group.Name + "@trueorfalse"

        if(sheet_name not in self._get_sheets()):
            return

        df = pd.read_excel(self.sheet_path, sheet_name)

        for _, row in df.iterrows():
            question = TrueOrFalseQuestion(Question=row[self.QUESTION_COLUMN], Answer=row[self.ANSWER_COLUMN], Points=row[self.POINTS_COLUMN])
            question_group.TrueOrFalseQuestions.append(question)


    def _get_question_groups(self):
      return set([self._remove_sheet_type(sheet) for sheet in self._get_sheets()])


    def _get_sheets(self):
      return self.excel_file.sheet_names


    def _remove_sheet_type(self, sheet_name : str):
      result = sheet_name.replace("@trueorfalse", "").replace("@identification", "")
      return result

