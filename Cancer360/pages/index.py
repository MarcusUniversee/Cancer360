"""The home page of the app."""

from Cancer360 import styles
from Cancer360.templates import template
from Cancer360.components.appointment import appointment
import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        appointment(),
        rx.text("Insert graphics here"),
        rx.link(
            rx.circle(
                rx.text("Get Started", font_size="2em"),
                bg="blue",
                text_color="white",
                padding="2em"
            ),
            href="/dashboard"
        ),
        border="none",
        outline="none",
        width="100%",
        padding="1em",
        justify_content= "center",
        align_items= "center",
    )
