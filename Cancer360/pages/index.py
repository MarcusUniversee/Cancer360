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
        #cnn_detect(),
        #rx.text("Insert graphics here"),
        rx.link(
            rx.circle(
                rx.text("Get Started", font_size="2em", as_="b"),
                bg="#606060",
                text_color="white",
                padding="2em",
                box_shadow="rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;",
                _hover={"box_shadow" : 'None'}
            ),
            href="/portal", 
            text_decoration = "none",
            _hover={}
        ),
        background_image = "/background-graphic.png",
        border="none",
        outline="none",
        width="100%",
        height="100%",
        padding="0em",
        justify_content= "center",
        align_items= "center",
    )
