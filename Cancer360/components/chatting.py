"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State
from Cancer360.chatbot import ChatBotState

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
        chat_bubble("Ameya:"),
        chat_bubble("Hi, My name is Ameya and I am going to be your nurse today. Can you describe some of the symptoms you're experiencing?"),
        rx.foreach(
            ChatBotState.data_formatted,
            chat_bubble,
        ),
        rx.cond(
            ChatBotState.end,
            rx.link(
                rx.circle(
                    rx.text("Next", font_size="2em"),
                    bg="#FF69B4",
                    text_color="white",
                    padding="2em"
                ),
                href="/info_portal"
            ),
            rx.form(
                rx.hstack(
                    rx.input(
                        placeholder="",
                        id="msg",
                    ),
                    rx.button(
                        "Send",
                        type_="submit",
                        on_click=ChatBotState.start_loading(),
                        is_loading=ChatBotState.loading,
                        loading_text="Sending..",
                        bg="#FF69B4",
                        text_color="white"
                    ),
                ),
                on_submit=ChatBotState.submit_data,
            ),
        ),
        rx.button("Refresh Conversation", on_click=ChatBotState.refresh(), bg="#FF69B4", text_color="white"),
        width="100%",
        padding="2em",
        border=styles.border,
        border_radius="2.5rem",
        bg="#FF69B412"
    )