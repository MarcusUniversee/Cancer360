"""The portal page."""
from Cancer360.templates import template

import reflex as rx
from Cancer360.components.chatting import chatting

@template(route="/portal", title="Portal")
def portal() -> rx.Component:
    """The portal page.

    Returns:
        The UI for the portal page.
    """
    return rx.vstack(
        chatting(),
        rx.heading("Portal", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/portal.py"),
        ),
    )
