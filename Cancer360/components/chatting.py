"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State
from Cancer360.chatbot import ChatBotState

import reflex as rx

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="left"),
            bg="#FF69B4",
            text_color="white",
            padding="0.5em",
            overflow_wrap= "break-word",
            width="fit-content",
            border_radius="1rem",
            max_width="35em",
            margin_y="1em",
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            text_color="black",
            bg="white",
            padding="0.5em",
            overflow_wrap= "break-word",
            width="fit-content",
            border_radius="1rem",
            max_width="35em",
            margin_y="1em",
        ),
        min_width="40em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            ChatBotState.data,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def chat_bubble_left(text: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(text, text_align="left"),
            text_color="black",
            bg="white",
            padding="0.5em",
            overflow_wrap= "break-word",
            width="fit-content",
            border_radius="1rem",
            max_width="35em",
            margin_y="1em",
        ),
        min_width="40em",
    )

def chatting() -> rx.Component:
    """header at the top of the page

    Returns:
        The header component.
    """
    return rx.vstack(
        chat_bubble_left("Hi, My name is Ameya and I am going to be your nurse today. Can you describe some of the symptoms you're experiencing?"),
        #rx.foreach(
            #ChatBotState.data_formatted,
            #chat_bubble,
        #),
        chat(),
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
                        placeholder="Ask a question",
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
        min_width="40em",
        padding="2em",
        border=styles.border,
        border_radius="2.5rem",
        bg="#FF69B412"
    )