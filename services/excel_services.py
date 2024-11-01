import os
from pathlib import Path
from numpy import result_type
import pandas as pd
from data.excelData import MultipleChoiceGroupedDataRow
from data.topicData import IdentificationQuestion, MultipleAnswerQuestion, MultipleChoiceQuestion, QuestionGroup, Topic, TrueOrFalseQuestion

class ExcelService:
    QUESTION_COLUMN = "Questions"
    ANSWER_COLUMN = "Answer"
    POINTS_COLUMN = "Points"

    ISCASESENSITIVE_COLUMN = "IsCaseSensitive"

    CHOICE_COLUMN = "Choice"
    CHOICE_TYPE_COLUMN = "ChoiceType"
    NOTE_COLUMN = "Notes"

    CORRECT_VALUE = "Correct"
    WRONG_VALUE = "Wrong"

    TRUE_OR_FALSE_PREFIX = "@trueorfalse"
    IDENTIFICATION_PREFIX = "@identification"
    MULTIPLE_CHOICE_PREFIX = "@multiplechoice"
    MULTIPLE_ANSWERS_PREFIX = "@multipleanswers"

    def __init__(self, excel_path : str):
        self.sheet_path = excel_path
        self.excel_file = pd.ExcelFile(excel_path)
        
        topicName = Path(excel_path).stem
        self.data : Topic = Topic(Name=topicName)


    def load(self):
        # Check question groups
        for question_group in self._get_question_groups():
            self._load_question_group(question_group)

        return self.data


    def _load_question_group(self, question_group_name : str):
        question_group = QuestionGroup(Name=question_group_name)
        
        self._load_trueorfalse(question_group)
        self._load_identification(question_group)
        self._load_multiple_choice(question_group)
        self._load_multiple_answer(question_group)

        self.data.QuestionGroups.append(question_group)


    def _load_multiple_answer(self, question_group : QuestionGroup):
        sheet_name = question_group.Name + self.MULTIPLE_ANSWERS_PREFIX

        if(sheet_name not in self._get_sheets()):
            return

        df = pd.read_excel(self.sheet_path, sheet_name)
        
        df = df.ffill()
        
        grouped_questions = df.groupby(self.QUESTION_COLUMN).apply(lambda g: [
            MultipleChoiceGroupedDataRow(
                Points = row[self.POINTS_COLUMN],
                Choice = row[self.CHOICE_COLUMN],
                ChoiceType = row[self.CHOICE_TYPE_COLUMN],
                Notes = row[self.NOTE_COLUMN]
                ) 
                for _, row in g.iterrows()
            ],
        )

        for name, grouped_data in grouped_questions.items():
            points, notes = grouped_data[0].Points, grouped_data[0].Notes
            
            correct_answer_rows = filter(lambda row: row.ChoiceType.lower() == self.CORRECT_VALUE.lower(), grouped_data)
            correct_answers = list(map(lambda row: row.Choice, correct_answer_rows))

            wrong_answers_rows = filter(lambda row: row.ChoiceType.lower() == self.WRONG_VALUE.lower(), grouped_data)
            wrong_answers = list(map(lambda row: row.Choice, wrong_answers_rows))
            
            question = MultipleAnswerQuestion(
                Question = name, 
                Points = points, 
                CorrectAnswers = correct_answers,
                WrongAnswers = wrong_answers,
                Notes = notes
            )
            question_group.MultipleAnswerQuestions.append(question)


    def _load_multiple_choice(self, question_group : QuestionGroup):
        sheet_name = question_group.Name + self.MULTIPLE_CHOICE_PREFIX

        if(sheet_name not in self._get_sheets()):
            return
        
        
        df = pd.read_excel(self.sheet_path, sheet_name)
        
        df = df.ffill()
        
        grouped_questions = df.groupby(self.QUESTION_COLUMN).apply(lambda g: [
            MultipleChoiceGroupedDataRow(
                Points = row[self.POINTS_COLUMN],
                Choice = row[self.CHOICE_COLUMN],
                ChoiceType = row[self.CHOICE_TYPE_COLUMN],
                Notes = row[self.NOTE_COLUMN]
                )  
                for _, row in g.iterrows()
            ]
        )

        for name, grouped_data in grouped_questions.items():
            points = grouped_data[0].Points
            
            # Find the correct answer with its note
            correct_answer_row = next((row for row in grouped_data if row.ChoiceType.lower() == self.CORRECT_VALUE.lower()), None)
            correct_answer_wnotes = {correct_answer_row.Choice: correct_answer_row.Notes} if correct_answer_row else {}

            # Find the wrong answers with their notes
            wrong_answers_wnotes = {row.Choice: row.Notes for row in grouped_data if row.ChoiceType.lower() == self.WRONG_VALUE.lower()}
            
            question = MultipleChoiceQuestion(
                Question=name, 
                Points = points, 
                CorrectAnswerWNotes = correct_answer_wnotes,
                WrongAnswersWNotes = wrong_answers_wnotes
            )
            question_group.MultipleChoiceQuestions.append(question)


    def _load_identification(self, question_group : QuestionGroup):
        sheet_name = question_group.Name + self.IDENTIFICATION_PREFIX

        if(sheet_name not in self._get_sheets()):
            return

        df = pd.read_excel(self.sheet_path, sheet_name)

        for _, row in df.iterrows():
            question = IdentificationQuestion(
                Question=row[self.QUESTION_COLUMN], 
                Answer=row[self.ANSWER_COLUMN], 
                Points=row[self.POINTS_COLUMN],
                IsCaseSensitive=row[self.ISCASESENSITIVE_COLUMN] == 'T',
                Notes = row[self.NOTE_COLUMN]
            )
            question_group.IdentificationQuestions.append(question)


    def _load_trueorfalse(self, question_group : QuestionGroup):
        sheet_name = question_group.Name + self.TRUE_OR_FALSE_PREFIX

        if(sheet_name not in self._get_sheets()):
            return

        df = pd.read_excel(self.sheet_path, sheet_name)

        for _, row in df.iterrows():
            question = TrueOrFalseQuestion(
                Question = row[self.QUESTION_COLUMN], 
                Answer = row[self.ANSWER_COLUMN], 
                Points = row[self.POINTS_COLUMN],
                Notes = row[self.NOTE_COLUMN]
            )
            question_group.TrueOrFalseQuestions.append(question)


    def _get_question_groups(self):
      return set([self._remove_sheet_type(sheet) for sheet in self._get_sheets()])


    def _get_sheets(self):
      return self.excel_file.sheet_names


    def _remove_sheet_type(self, sheet_name : str):
      result = sheet_name.replace(self.TRUE_OR_FALSE_PREFIX, "") \
                         .replace(self.IDENTIFICATION_PREFIX, "") \
                         .replace(self.MULTIPLE_CHOICE_PREFIX, "") \
                         .replace(self.MULTIPLE_ANSWERS_PREFIX, "")
      return result
