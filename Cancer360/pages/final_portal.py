"""The portal page."""
from Cancer360.templates import template

import reflex as rx
from Cancer360.components.cnn_detect import cnn_detect
from Cancer360.components.steps_sidebar import sidebar
from Cancer360.components.zepp import zepp
from Cancer360.components.FinalPage import Result

@template(route="/final_portal", title="Final Portal")
def final_portal() -> rx.Component:
    """The portal page.

    Returns:
        The UI for the portal page.
    """
    
    return rx.vstack(
        rx.heading("The Final Lung Cancer Probability is " + Result.A),
        rx.heading(Result.B)
    )
