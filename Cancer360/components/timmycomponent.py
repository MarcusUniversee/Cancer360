"""Component for quantitative data"""

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyAppointmentFormState, getPred, text_analysis
from Cancer360.state import State, FormErrorState, AppointmentFormState

import reflex as rx

def timmy_component() -> rx.Component:
    # Input + Check + drop down
    return rx.vstack(
        
        rx.cond(
            TimmyAppointmentFormState.data_filled,
            rx.vstack(
                rx.text("Thank you for submitting", font_size="2.5em"),
                rx.link(
                    rx.circle(
                        rx.text("Next", font_size="2em"),
                        bg="#FF69B4",
                        text_color="white",
                        padding="2em"
                    ),
                    href="/zepp_portal"
                ),
                rx.button("Resubmit Form", bg="#FF69B4", text_color="white", on_click=TimmyAppointmentFormState.handle_clear_data())
            ),
            rx.vstack(
                rx.text("Please fill all fields. ", font_size="2em"),
                rx.form(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Age: "),
                            rx.input(
                                placeholder="",
                                id="Age",
                                bg="white",
                            ),
                            width="100%",
                            padding="0.5em"
                        ),
                        rx.hstack(
                            rx.text("Sex: "),
                            rx.spacer(),
                            rx.checkbox("Male", id="Male", color_scheme="pink"),
                            rx.spacer(),
                            rx.checkbox("Female", id="Female", color_scheme="pink"),
                            rx.spacer(),
                            width="100%",
                            padding="0.5em"
                        ),
                        rx.hstack(
                            rx.text("Race/Ethnicity: "),
                            rx.input(
                                placeholder="",
                                id="Race/Ethnicity",
                                bg="white",
                            ),
                            width="100%",
                            padding="0.5em"
                        ),
                        rx.hstack(
                            rx.text("Zipcode: "),
                            rx.input(
                                placeholder="",
                                id="Zipcode",
                                bg="white",
                            ),
                            width="100%",
                            padding="0.5em"
                        ),
                        rx.hstack(
                            rx.text("Years of smoking: ", word_wrap="normal"),
                            rx.input(
                                placeholder="",
                                id="Smoking_Years",
                                bg="white",
                            ),
                            width="100%",
                            overflow="none",
                            padding="0.5em"
                        ),
                        rx.hstack(
                            rx.text("Family History of Lung Cancer: "),
                            rx.spacer(),
                            rx.checkbox("Select if Yes", id="History", color_scheme="pink"),
                            rx.spacer(),
                            width="100%",
                            padding="0.5em"
                        ),
                        rx.text("Have you been experiencing any of the following?"),
                        rx.hstack(
                            rx.checkbox("Shortness Of Breath", id="A", color_scheme="pink"),
                            rx.checkbox("Coughing", id="B", color_scheme="pink"),
                            rx.checkbox("Swallowing Difficulty", id="C", color_scheme="pink"),
                            rx.checkbox("Yellow Fingers", id="D", color_scheme="pink"),
                            rx.checkbox("Wheezing", id="E", color_scheme="pink"),
                            width="100%",
                            padding="0.5em"
                        ),
                        
                        rx.hstack(
                            rx.text("Any Additional Comments?"),
                            rx.input(
                                placeholder="Any Additional Comments?",
                                id="comments",
                                bg="white",
                            ),
                            width="100%",
                            padding="0.5em"
                        ),
                        rx.button("Submit", type_="submit", bg="#FF69B4", text_color="white"),
                        
                    ),
                    on_submit=TimmyAppointmentFormState.handle_submit_data,
                    width="100%"
                ),
            ),
        ),
        rx.divider(),
        rx.text(TimmyAppointmentFormState.results.to_string()),
        
        width="100%",
        padding="2em",
        border=styles.border,
        border_radius="3rem",
        bg="#FF69B412"
    )

#AppointmentFormState.form_data.to_string()