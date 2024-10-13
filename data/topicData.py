from dataclasses import dataclass, field
from typing import List

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
class QuestionGroup:
    Name: str
    TrueOrFalseQuestions: List[TrueOrFalseQuestion] = field(default_factory=list)
    IdentificationQuestions: List[IdentificationQuestion] = field(default_factory=list)

@dataclass
class Topic:
  Name: str
  QuestionGroups: List[QuestionGroup] = field(default_factory=list)


