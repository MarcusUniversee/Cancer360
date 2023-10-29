"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State

import reflex as rx


def sidebar_item(text: str, link: str, color: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.text(text, font_size="1.5em"),
            padding="2em",
            bg=color,
            width="100%"
        ),
        href=link,
        width="100%",
        text_decoration="none",
        _hover={}
    )

def sidebar(color1, color2, color3, color4, prog) -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.

    return rx.box(
        rx.vstack(
            rx.text("Steps", font_size="2em", padding="0.2em"),
            rx.progress(value=prog, width="100%", padding="0.2em", color_scheme="pink"),
            rx.vstack(
                sidebar_item("Chatbot", "/portal", color1),
                sidebar_item("General Information", "/info_portal", color2),
                sidebar_item("Zepp Watch", "/zepp_portal", color3),
                sidebar_item("Xray Scans", "/scans_portal", color4),
                width="100%"
            ),
            rx.spacer(),
            height="100dvh",
            width="100%"
        ),
        display=["none", "none", "block"],
        min_width="15em",
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
