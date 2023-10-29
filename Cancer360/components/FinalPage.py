
from Cancer360.state import State
import reflex as rx
import time

class Result(State):
    ChatPercent : float
    ScansPercent: float
    ZeppPercent: float
    QualPercent: float
    
    A : str
    B : str
    
    def getAverage(self):
        print("SDLFJSDFKLJSDFL:KD")
        self.ChatPercent = 0.8
        temp = (self.ChatPercent + self.ScansPercent + self.ZeppPercent + self.QualPercent) / 4
        temp = round(temp, 2)
        self.A = str(temp)
        asdf = ""
        if temp > 0.7:
            asdf = "We highly recommend you visit a licensed medical professional. Hold on while we connect you with a hospital near you."
        elif temp > 0.5:
            asdf = "We recommend that you still visit a licensed medical professional. Hold on while we connect you with a hospital near you."
        else:
            asdf = "You are probably safe, but we still recommend that you visit a licensed medical professional."
        print(asdf)
        self.B = str(asdf)