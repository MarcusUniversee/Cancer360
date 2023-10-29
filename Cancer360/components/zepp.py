# import os

# print(os.listdir('./'))

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyAppointmentFormState, getPred, text_analysis
from Cancer360.state import State, FormErrorState, AppointmentFormState
from Cancer360.Zepp_API_utils import ZeppOSMetrics

import reflex as rx

def get_current_calories(self):
    calories_js_code = """
    let calorie = new Calorie();
    calorie.getCurrent();
    """
    # return self.context.eval(calories_js_code)
    ZeppOSMetrics.A = 50
    return 1550

def get_current_blood_oxygen(self):
    blood_oxygen_js_code = """
    let bloodOxygen = new BloodOxygen();
    bloodOxygen.getCurrent();
    """
    # return self.context.eval(blood_oxygen_js_code)
    ZeppOSMetrics.B = 50
    return 97

def get_current_fat_burning(self):
    fat_burning_js_code = """
    let fatBurning = new FatBurning();
    fatBurning.getCurrent();
    """
    # return self.context.eval(fat_burning_js_code)
    ZeppOSMetrics.C = 50
    return 50

def get_PAI(self):
    fat_burning_js_code = """
    let PAI = new Pai();
    PAI.getCurrent();
    """
    # return self.context.eval(fat_burning_js_code)
    ZeppOSMetrics.D = 80
    return 80

def zepp() -> rx.Component:
    # Input + Check + drop down
    return rx.vstack(
        rx.box(
            rx.image (
                src="/Zeppos.png", object_fit="contain"
            ),
            width="25em",
            height="25em",
            padding="5em"
        ),
        rx.vstack(
            rx.hstack(     
                rx.text("Blood Oxygen"),
                rx.button("Fetch", padding="0.25pm", on_click=ZeppOSMetrics.clicked, submit="submit"),
                
                
                rx.text("Calorie Burned"),
                rx.button("Fetch", padding="0.25pm", on_click=ZeppOSMetrics.clicked,submit="submit"),
            ),
            rx.hstack(
                rx.text("Fat Burned"),
                rx.button("Fetch", padding="0.25pm", on_click=ZeppOSMetrics.clicked,submit="submit"),
                
                rx.text("Personal Activity Index"),
                rx.button("Fetch", padding="0.25pm", on_click=ZeppOSMetrics.clicked,submit="submit")
            )
        ),
        
        rx.divider(),
        
        rx.circular_progress(
            rx.circular_progress_label("", color="pink"),
            value=ZeppOSMetrics.val,
        ),
        # rx.text(TimmyAppointmentFormState.results.to_string()),
        rx.text(ZeppOSMetrics.healthIndexText, font_weight="bold",
                font_size="2em",),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )

#AppointmentFormState.form_data.to_string() 