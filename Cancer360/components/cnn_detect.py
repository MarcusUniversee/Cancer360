"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyAppointmentFormState, CNNState, getPred, text_analysis
from Cancer360.state import State, FormErrorState, AppointmentFormState

import reflex as rx

color = "#799FC3"

def cnn_detect() -> rx.Component:
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg=color,
                    text_color="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            border=f"1px dotted {color}",
            padding="6em",
        ),
        rx.hstack(rx.foreach(rx.selected_files, rx.text)),
        rx.button(
            "Upload",
            on_click=lambda: CNNState.handle_upload(
                rx.upload_files()
            ),
            bg="#FF69B4",
            text_color="white"
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files,
            bg="#FF69B4",
            text_color="white"
        ),
        rx.foreach(
            CNNState.img, lambda img: rx.image(src=img)
        ),
        rx.text(CNNState.prediction_string),
        width="100%",
        padding="3em",
        border=styles.border,
        border_radius="2.5rem",
        bg="#FF69B412",
    )

#AppointmentFormState.form_data.to_string()


