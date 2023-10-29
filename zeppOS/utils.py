import PyV8

class ZeppOSMetrics:

    def __init__(self):
        # This context allows you to run JavaScript code within Python
        self.context = PyV8.JSContext()
        self.context.enter()
        
        # Load the necessary JS libraries or code snippets here
        self.context.eval("""
        import * as hmUI from "@zos/ui";
        import { push } from "@zos/router";
        import { getText } from "@zos/i18n";
        import { Calorie } from "@zos/sensor";
        import { log as Logger, px } from "@zos/utils";
        import { BloodOxygen } from "@zos/sensor";
        import { FatBurning } from "@zos/sensor";
        """)
        
    def get_current_calories(self):
        calories_js_code = """
        let calorie = new Calorie();
        calorie.getCurrent();
        """
        return self.context.eval(calories_js_code)
    
    def get_current_blood_oxygen(self):
        blood_oxygen_js_code = """
        let bloodOxygen = new BloodOxygen();
        bloodOxygen.getCurrent();
        """
        return self.context.eval(blood_oxygen_js_code)
    
    def get_current_fat_burning(self):
        fat_burning_js_code = """
        let fatBurning = new FatBurning();
        fatBurning.getCurrent();
        """
        return self.context.eval(fat_burning_js_code)
