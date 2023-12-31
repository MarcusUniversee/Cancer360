"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.state import State

import reflex as rx
color1 = "#FF69B4"

def header_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The header item component.
    """
    # Whether the item is active.

    return rx.link(
        rx.hstack(
            rx.text(
                text,
                font_size="1.5em",
                text_color = 'black'
            ),
            width="100%",
            padding_x="1em",
        ),
        href=url,
        width="100%",
    )



def header() -> rx.Component:
    """header at the top of the page

    Returns:
        The header component.
    """
    from reflex.page import get_decorated_pages
    return rx.hstack(
        # Link to Reflex GitHub repo.
        rx.center(
            rx.link(
                rx.center(
                    rx.image(src="/image2vector.svg", width="15em")
                ),
                href="/",
                border="none",
                outline="none",
                justify_content= "center",
                align_items= "center"
            ),
            #bg="blue",
            bg = "white",
            width="20%",
            height="100%",
        ),
        rx.spacer(),
        rx.hstack(
            *[
                header_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        url=page["route"],
                    )
                    for page in get_decorated_pages() if "_portal" not in page["route"]
            ],
            #rx.button('Start', bg=color1, color = "white", padding="1em", border_radius="8px", on_click=rx.redirect(
            #"/portal")),
            width="35%",
            overflow_y="auto",
            border="none",
            outline="none",
            text_align="left",
            height="100%",
            bg="white",
        ),
        rx.spacer(),
        rx.button('Get Started', bg=color1, color = "white", padding="1em", border_radius="8px", on_click=rx.redirect(
            "/portal")),
        width="100%",
        #border_bottom=styles.border,
        padding="0em",
        margin="0em",
        height="6em",
        bg="white", #black line separating the stacks
        padding_x="2em",
        
        
    )