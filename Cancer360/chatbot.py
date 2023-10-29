#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import together
together.api_key = "eba8b7224a7ca9d941a365ef2eb5fc207b923f11fbecf408acb3d09b02a8be40"


# In[ ]:


system_prompt = (
    "You will act as a cancer specialist nurse named Ameya for a human patient. You will ask patients a series of questions but ask one question at a time. Using the patient's response from each question, you aim to get a better understanding of if the patient has cancer and tailor your future questions in response. For example, you could start by asking if the patient has been feeling sick recently, and if they say they have, ask questions to see if these symptoms might be reflective of cancer (e.g., does this patient have a history of cancer?) Use a respectful and professional tone throughout. Keep questions concise. Once you've determined the possibility of cancer, wrap up the conversation with short suggestions on what to do next. Don't respond with more than 2 paragraphs of text. Please diagnose the patient at the end with what their chances of having lung cancer is on a scale of 0-100. Then, end the conversation with \"Have a great day!\" if the user doesn't have any questions." 
)


prompt = f"<s>[INST] <<SYS>>{system_prompt}<</SYS>>\n\n"

print("Hi, My name is Ameya and I am going to be your nurse today. Can you describe some of the symptoms you're experiencing?")

all_patient_responses = ""

while True:

    user_input = input("Input: ")

    prompt += user_input + "[/INST]"

    #string = ["Have a great day!", "Have a good day!"]
    string = "Have a great day!"
    #first_occurrence = prompt.find(string[0])
    first_occurrence = prompt.find(string)
    #second_occurrence = [prompt.find(string[i], first_occurrence + 1) for i in range(2)]
    #for val in second_occurrence:
        #if val != -1 :
            #break
    second_occurrence = prompt.find(string, first_occurrence + 1)
    if second_occurrence != -1:
        break

    output = together.Complete.create(
      prompt, 
      model = "togethercomputer/llama-2-70b-chat", 
      max_tokens = 500,
      temperature = 0.6,
      top_k = 90,
      top_p = 0.8,
      repetition_penalty = 1.1,
      stop = ['</s>']
    )

    model_reply = output['output']['choices'][0]['text']
    
    prompt += model_reply + "</s><s>[INST]"
    
    print("Output: " + output['output']['choices'][0]['text'])

    #second_occurrence = [prompt.find(string[i], first_occurrence + 1) for i in range(2)]
    #for val in second_occurrence:
        #if val != -1 :
            #break
    second_occurrence = prompt.find(string, first_occurrence + 1)
    if second_occurrence != -1:
        break
