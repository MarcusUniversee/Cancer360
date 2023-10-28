"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State, FormErrorState, AppointmentFormState

import reflex as rx

def appointment() -> rx.Component:
    """appointment form to fill out

    Returns:
        The header component.
    """
    return rx.vstack(
        rx.text("Make an Appointment", font_size="2em"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    id="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    id="last_name",
                ),
                rx.input(
                    placeholder="Email",
                    id="email",
                ),
                rx.input(
                    placeholder="Phone Number",
                    id="phone_number",
                ),
                rx.text(
                    "Enter a start and end date and a certified doctor will reach out to you to setup an appointment"
                ),
                rx.form_control(
                    rx.input(
                        placeholder="Start Date",
                        on_blur=FormErrorState.set_input,
                        id="start_date",
                    ),
                    rx.cond(
                        FormErrorState.is_date,
                        rx.form_error_message(
                            "Date should be in the format MM/DD/YYYY"
                        ),
                        rx.form_helper_text(
                            "MM/DD/YYYY"
                        ),
                    ),
                    is_invalid=FormErrorState.is_date,
                    is_required=True,
                ),
                rx.form_control(
                    rx.input(
                        placeholder="End Date",
                        on_blur=FormErrorState.set_input,
                        id="end_date"
                    ),
                    rx.cond(
                        FormErrorState.is_date,
                        rx.form_error_message(
                            "Date should be in the format MM/DD/YYYY"
                        ),
                        rx.form_helper_text(
                            "MM/DD/YYYY"
                        ),
                    ),
                    is_invalid=FormErrorState.is_date,
                    is_required=True,
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=AppointmentFormState.handle_submit_data,
        ),
        rx.divider(),
        rx.text(AppointmentFormState.form_data.to_string()),
        
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )