from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class TrueOrFalseQuestion:
    Question: str
    Answer: bool
    Points: int

@dataclass
class IdentificationQuestion:
    Question: str
    Answer: str
    Points: int
    IsCaseSensitive: bool

@dataclass
class MultipleChoiceQuestion:
    Question: str
    Points: int
    CorrectAnswer: str
    WrongAnswers: List[str]

@dataclass
class MultipleAnswerQuestion:
    Question: str
    Points: int
    CorrectAnswers: List[str]
    WrongAnswers: List[str]

@dataclass 
class QuestionDetail:
  Topic: str
  QuestionGroup: str
  Question: Union[TrueOrFalseQuestion, IdentificationQuestion, MultipleChoiceQuestion, MultipleAnswerQuestion]

@dataclass
class ExamDetails:
  TotalPossibleScore: Optional[int] = 0
  TopicsCovered: List[str] = field(default_factory=list)
  QuestionDetails: List[QuestionDetail] = field(default_factory=list)
  
@dataclass
class QuestionGroup:
    Name: str
    TrueOrFalseQuestions: List[TrueOrFalseQuestion] = field(default_factory=list)
    IdentificationQuestions: List[IdentificationQuestion] = field(default_factory=list)
    MultipleChoiceQuestions: List[MultipleChoiceQuestion] = field(default_factory=list)
    MultipleAnswerQuestions: List[MultipleAnswerQuestion] = field(default_factory=list)

@dataclass
class Topic:
  Name: str
  QuestionGroups: List[QuestionGroup] = field(default_factory=list)

@dataclass 
class XLSXInfo:
  Alias: str
  Topics : List[Topic] = field(default_factory=list)

