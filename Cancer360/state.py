"""Base state for the app."""

import reflex as rx
import re


class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """

    pass


class ChatBotState(State):
    data: str
    data_formatted: list
    def submit_data(self, form_data: dict):
        data = form_data['msg']
        self.data = data
        self.data_formatted = split_chat(data)
    

def split_chat(data) -> list:
    s = data
    s = s.replace("<s>", "").replace("</s>", "")
    index1 = s.find("<</SYS>>")
    if index1 != -1:
        s = s[index1+12:]
    lst1 = s.split("[INST]")
    lst2 = [str.split("[/INST]") for str in lst1]
    lst3 = []
    for lst in lst2:
        lst3.append("Me:\\n" + lst[0])
        if len(lst) > 1:
            lst3.append("Ameya:\\n" + lst[1])
        else:
            lst3.append("")
    lst4 = []
    for lst in lst3:
        splitlst = lst.split("\\n")
        for s in splitlst:
            s = s.replace("\\", "")
            lst4.append(s)
    return lst4

class AppointmentFormState(State):
    form_data: dict = {}
    data_filled: bool = False
    def handle_submit_data(self, form_data: dict):
        self.form_data = form_data
        self.data_filled = True
    def handle_clear_data(self):
        self.form_data.clear()
        self.data_filled = False

class FormErrorState(State):
    input: str

    @rx.var
    def is_date(self) -> bool:
        return re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', self.input)

