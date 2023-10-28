"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyAppointmentFormState, getPred, text_analysis
from Cancer360.state import State, FormErrorState, AppointmentFormState

import reflex as rx

def timmy_component() -> rx.Component:
    
    return rx.vstack(
        rx.text("Please provide us with a detailed description of your symptom. ", font_size="2em"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Age",
                    id="Age",
                ),
                rx.input(
                    placeholder="Gender",
                    id="Gender",
                ),
                rx.input(
                    placeholder="Input",
                    id="Input",
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
