"""The home page of the app."""

from Cancer360 import styles
from Cancer360.templates import template
from Cancer360.components.appointment import appointment
from Cancer360.components.timmycomponent import timmy_component
from Cancer360.components.cnn_detect import cnn_detect
from Cancer360.components.zepp import zepp
import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        # appointment(),
        # zepp(),
        # timmy_component(),
        # cnn_detect(),
        #rx.text("Insert graphics here"),
        rx.square(
            rx.vstack(
                rx.text(
                    "CANCER360°", font_size="4em"
                        ),
                rx.text(
                    "An all-encompassing healthcare solution that harnesses the power of AI and innovative technology to revolutionize cancer patient care, ensuring a seamless journey from diagnosis to treatment while promoting effective communication and holistic support for patients and their families.", font_size="1.5em", align_items= "center"
                )
            ),
            text_align='center',
            text_color="black",
            text_decoration= "none",
            bg='white',
            padding="3em",

        ),
        background_image = "/background-graphic.png",
        border="none",
        outline="none",
        width="100%",
        height="110%",
        padding="7em",
        justify_content= "center",
        align_items= "center",
    )
