"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyAppointmentFormState, CNNState, getPred, text_analysis
from Cancer360.state import State, FormErrorState, AppointmentFormState
from Cancer360.components.FinalPage import Result

import reflex as rx

color = "#799FC3"

def cnn_detect() -> rx.Component:
    """The main view."""
    return rx.vstack(
        rx.cond(
            CNNState.has_img,
            rx.vstack(
                rx.link(
                    rx.circle(
                        rx.text("Next", font_size="2em"),
                        bg="#FF69B4",
                        text_color="white",
                        padding="2em",
                        on_click=Result.getAverage()
                    ),
                    href="/final_portal"
                ),
                rx.button("Reload", on_click=CNNState.handle_clear(), bg="#FF69B4", text_color="white")
            ),
            rx.vstack(
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
            ),
        ),
        
        rx.foreach(
            CNNState.img, lambda img: rx.image(src=img)
        ),
        rx.text(CNNState.prediction_string, 
                background_image="linear-gradient(271.68deg, #4B0082 0%, #FF69B4 100%)",
                background_clip="text",
                font_weight="bold",
                font_size="2em",
            ),
        width="100%",
        padding="3em",
        border=styles.border,
        border_radius="2.5rem",
        bg="#FF69B412",
    )

#AppointmentFormState.form_data.to_string()


