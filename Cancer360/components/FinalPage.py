
from Cancer360.state import State
import reflex as rx

class Result(State):
    ChatPercent : float
    ScansPercent: float
    ZeppPercent: float
    QualPercent: float
    
    def getAverage(self):
        self.ChatPercent = 0.8
        return str((self.ChatPercent + self.ScansPercent + self.ZeppPercent + self.QualPercent) / 4)