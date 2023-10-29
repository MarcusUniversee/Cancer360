"""The portal page."""
from Cancer360.templates import template

import reflex as rx

@template(route="/solutions", title="Solutions")
def solutions() -> rx.Component:
    """The solutions page.

    Returns:
        The UI for the solutions page.
    """
    return rx.vstack(
        rx.hstack(
            rx.heading("How it all started.", font_size="3em")
        ),
        rx.text("Cancer is a disease that has affected our team quite directly. All of our team members know a relative or loved one that has endured or lost their life due to cancer. This makes us incredibly passionate about wanting to improve cancer patient care. We identified a common thread of roadblocks that our loved ones went through during their journey.", font_size="1.5em"),
        text_align="center",
        padding="6em"
        
    )
