"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State, ChatBotState

import reflex as rx


def chat_bubble(text: str) -> rx.Component:
    return rx.box(
        text,
        text_color="black",
        bg="white",
        padding="0.5em",
        overflow_wrap= "break-word",
        width="100%"
    )

def chatting() -> rx.Component:
    """header at the top of the page

    Returns:
        The header component.
    """
    return rx.vstack(
        rx.foreach(
            ChatBotState.data_formatted,
            chat_bubble,
        ),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="msg",
                    id="msg",
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=ChatBotState.submit_data,
        ),
    )