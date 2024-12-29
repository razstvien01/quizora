from dataclasses import dataclass, field
from typing import List, Optional, Union

@dataclass
class MultipleChoiceGroupedDataRow:
    Points: int
    Choice: str
    ChoiceType: str
    Notes: str