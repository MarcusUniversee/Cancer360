"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State

import reflex as rx


def sidebar(color1, color2, color3, color4) -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.

    return rx.box(
        rx.vstack(
            rx.text("Steps", font_size="3em"),
            rx.vstack(
                rx.box(
                    rx.text("Chatbot"),
                    padding="2em",
                    bg = color1
                ),
                rx.box(
                    rx.text("General information"),
                    padding="2em",
                    bg=color2
                ),
                rx.box(
                    rx.text("Zepp watch"),
                    padding="2em",
                    bg=color3
                ),
                rx.box(
                    rx.text("Xray Scan"),
                    padding="2em",
                    bg=color4
                ),
                width="100%"
            ),
            rx.spacer(),
            height="100dvh",
            width="100%"
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
