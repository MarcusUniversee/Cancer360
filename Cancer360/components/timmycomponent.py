"""Component for quantitative data"""

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyAppointmentFormState, getPred, text_analysis
from Cancer360.state import State, FormErrorState, AppointmentFormState

import reflex as rx

def timmy_component() -> rx.Component:
    # Input + Check + drop down
    return rx.vstack(
        rx.text("Please provide us with a detailed description of your symptom. ", font_size="2em"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Age",
                    id="Age",
                ),
                rx.hstack(
                    rx.checkbox("Male", id="Male"),
                    rx.checkbox("Female", id="Female"),
                ),
                rx.input(
                    placeholder="Race/Ethnicity",
                    id="Race/Ethnicity",
                ),
                rx.input(
                    placeholder="Zipcode",
                    id="Zipcode",
                ),
                rx.input(
                    placeholder="Years of smoking",
                    id="Smoking_Years",
                ),
                rx.checkbox("Have Family History of Lung Cancer", id="History"),
                
                rx.text("Have you been experiencing any of the following?"),
                rx.hstack(
                    rx.checkbox("Shortness Of Breath", id="A"),
                    rx.checkbox("Coughing", id="B"),
                    rx.checkbox("Swallowing Difficulty", id="C"),
                    rx.checkbox("Yellow Fingers", id="D"),
                    rx.checkbox("Wheezing", id="E"),
                ),
                
                rx.text("Any Additional Comments?"),
                rx.input(
                    placeholder="Any Additional Comments?",
                    id="comments",
                ),
                
                rx.button("Submit", type_="submit"),
            ),
            on_submit=TimmyAppointmentFormState.handle_submit_data,
        ),
        rx.divider(),
        rx.text(TimmyAppointmentFormState.results.to_string()),
        
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )

#AppointmentFormState.form_data.to_string()