"""The dashboard page."""
from Cancer360.templates import template

import reflex as rx
from Cancer360.components.chatting import chatting

@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        chatting(),
    )
