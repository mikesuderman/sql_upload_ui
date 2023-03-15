from dataclasses import dataclass
from datetime import datetime
import sqlalchemy
# import pandas as pd

@dataclass
class NewRow:
    date: datetime
    cost: float
    type: str
    amount: int
    unit: str
    comment: str
    
    # 'date','cost','type','amount','unit','comment'