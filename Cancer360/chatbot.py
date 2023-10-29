#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import reflex as rx
from Cancer360.state import State
import together
together.api_key = "eba8b7224a7ca9d941a365ef2eb5fc207b923f11fbecf408acb3d09b02a8be40"
print("Hi, My name is Ameya and I am going to be your nurse today. Can you describe some of the symptoms you're experiencing?")
system_prompt = (
    "You are a lung cancer specialist nurse named Ameya for a human patient. You will ask patients questions, one at a time. Tailor your future questions to the patient's response. For example, you could start by asking if the patient has been feeling sick recently, and if they say they have, ask questions to see if these symptoms might be reflective of cancer (e.g., does this patient have a history of cancer?) Keep questions concise. Don’t respond with more than a paragraph. Diagnose the patient at the end with their chances of having lung cancer is on a scale of 0-100. Then, end the conversation with \"Have a great day!\" if the user doesn’t have any questions. Do not provide any suggestions, only ask questions to help diagnose."
    #"You will act as a cancer specialist nurse named Ameya for a human patient. You will ask patients a series of questions but ask one question at a time. Using the patient's response from each question, you aim to get a better understanding of if the patient has lung cancer and tailor your future questions in response. For example, you could start by asking if the patient has been feeling sick recently, and if they say they have, ask questions to see if these symptoms might be reflective of cancer (e.g., does this patient have a history of cancer?) Use a respectful and professional tone throughout. Keep questions concise. Once you've determined the possibility of lung cancer, wrap up the conversation with short suggestions on what to do next. Don't respond with more than 1 paragraph of text. Please diagnose the patient at the end with what their chances of having lung cancer is on a scale of 0-100. Then, end the conversation with \"Have a great day!\" if the user doesn't have any questions." 
)
# In[ ]:
class ChatBotState(State):
    data_formatted: list
    prompt: str = f"<s>[INST] <<SYS>>{system_prompt}<</SYS>>\n\n"
    end: bool = False
    loading: bool = False

    def refresh(self):
        self.prompt = f"<s>[INST] <<SYS>>{system_prompt}<</SYS>>\n\n"
        self.data_formatted = []
        self.end = False
        self.loading = False
    def start_loading(self):
        self.loading = True
    def submit_data(self, form_data: dict):
        data = form_data['msg']
        self.prompt += data + "[/INST]"
        string = "Have a great day!"
        first_occurrence = self.prompt.find(string)
        second_occurrence = self.prompt.find(string, first_occurrence + 1)
        if second_occurrence != -1:
            self.end = True
            self.loading = False
            return
        output = together.Complete.create(
            self.prompt, 
            model = "togethercomputer/llama-2-70b-chat", 
            max_tokens = 500,
            temperature = 0.6,
            top_k = 90,
            top_p = 0.8,
            repetition_penalty = 1.1,
            stop = ['</s>']
        )
        model_reply = output['output']['choices'][0]['text']
        self.prompt += model_reply + "</s><s>[INST]"
        self.data_formatted = split_chat(self.prompt)
        second_occurrence = self.prompt.find(string, first_occurrence + 1)
        self.loading = False
        if second_occurrence != -1:
            self.end = True
            return

def split_chat(data) -> list:
    s = data
    s = s.replace("<s>", "").replace("</s>", "")
    index1 = s.find("<</SYS>>")
    if index1 != -1:
        s = s[index1+10:]
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