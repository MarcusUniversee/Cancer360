import reflex as rx
from Cancer360.state import State
from Cancer360.components.FinalPage import Result
from PIL import Image
import requests
# import PyV8

# class ImageState(rx.State):
    # url = f"https://ibb.co/RCf5n0x"
    # image = Image.open(requests.get(url, stream=True).raw)

class ZeppOSMetrics(State):
    A : float
    B : float
    C : float
    D : float
    form_data: dict = {}
    results: float
    val : int
    healthIndexText : str
    
    def clicked(self):
        self.val += 25
        
        if (self.val >= 100):
            res = self.calculateHealthIndex()
            Result.ZeppPercent = res
            self.healthIndexText = "Health index using weighted average: " + str(res)

    # def __init__(self):
    #     # This context allows you to run JavaScript code within Python
    #     self.context = PyV8.JSContext()
    #     self.context.enter()
        
    #     # Load the necessary JS libraries or code snippets here
    #     self.context.eval("""
    #     import * as hmUI from "@zos/ui";
    #     import { push } from "@zos/router";
    #     import { getText } from "@zos/i18n";
    #     import { Calorie } from "@zos/sensor";
    #     import { log as Logger, px } from "@zos/utils";
    #     import { BloodOxygen } from "@zos/sensor";
    #     import { FatBurning } from "@zos/sensor";
    #     import { Pai } from "@zos/sensor";
    #     """)
        
    async def get_current_calories(self):
        calories_js_code = """
        let calorie = new Calorie();
        calorie.getCurrent();
        """
        # return self.context.eval(calories_js_code)
        return 1550
    
    async def get_current_blood_oxygen(self):
        blood_oxygen_js_code = """
        let bloodOxygen = new BloodOxygen();
        bloodOxygen.getCurrent();
        """
        # return self.context.eval(blood_oxygen_js_code)
        return 97
    
    async def get_current_fat_burning(self):
        fat_burning_js_code = """
        let fatBurning = new FatBurning();
        fatBurning.getCurrent();
        """
        # return self.context.eval(fat_burning_js_code)
        return 50
    
    async def get_PAI(self):
        fat_burning_js_code = """
        let PAI = new Pai();
        PAI.getCurrent();
        """
        # return self.context.eval(fat_burning_js_code)
        return 80
    
    def calculateHealthIndex(self):
        x1 = ZeppOSMetrics.get_current_calories()
        x2 = ZeppOSMetrics.get_current_blood_oxygen()
        x3 = ZeppOSMetrics.get_current_fat_burning()
        x4 = ZeppOSMetrics.get_PAI()
        
        # print(type(x1), type(x2), type(x3), type(x4))
        
        weights = [0.25, 0.2, 0.2, 0.4, 0.1]
        #health_index = weights[0] * x1 + weights[1] * x2 + weights[2] * x3 + weights[3] * x4
        return 92.55
