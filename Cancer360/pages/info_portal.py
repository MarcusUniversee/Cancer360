"""The portal page."""
from Cancer360.templates import template

import reflex as rx
from Cancer360.components.cnn_detect import cnn_detect
from Cancer360.components.steps_sidebar import sidebar

@template(route="/info_portal", title="Info Portal")
def info_portal() -> rx.Component:
    """The portal page.

    Returns:
        The UI for the portal page.
    """
    return rx.hstack(
        sidebar("#FF69B470", "#FF69B4", "#FFFFFF", "#FFFFFF"),
    )
