"""The portal page."""
from Cancer360.templates import template

import reflex as rx
from Cancer360.components.cnn_detect import cnn_detect

@template(route="/scans_portal", title="Scan Portal")
def scans_portal() -> rx.Component:
    """The portal page.

    Returns:
        The UI for the portal page.
    """
    return rx.vstack(
        cnn_detect(),
    )
