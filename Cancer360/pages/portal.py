"""The portal page."""
from Cancer360.templates import template

import reflex as rx
from Cancer360.components.chatting import chatting
from Cancer360.components.steps_sidebar import sidebar

@template(route="/portal", title="Portal")
def portal() -> rx.Component:
    """The portal page.

    Returns:
        The UI for the portal page.
    """
    return rx.hstack(
        sidebar("#FF69B4", "#FFFFFF", "#FFFFFF", "#FFFFFF"),
        chatting(),
    )
