"""The portal page."""
from Cancer360.templates import template

import reflex as rx

@template(route="/t_about_us", title="About Us")
def about_us() -> rx.Component:
    """The about_us page.

    Returns:
        The UI for the about_us page.
    """
    return rx.vstack(
        rx.image(src='/background-graphic-2.png'),
        rx.hstack(
            rx.heading("How it all started.", padding_top= "0.5em", font_size="3em", padding_bottom= "0.5em")
        ),
        rx.text("Cancer is a disease that has directly affected all our team members. Each of us has had a relative or loved one who has battled cancer. Therefore, this project means a lot to us, and we want to do what we can to improve cancer patient care. Through background research, we identified a common thread of roadblocks found in the processes of diagnosis, treatment, and follow-up. Cancer360 is our attempt at streamlining the process.", font_size="1.5em", padding_left="6em", padding_right="6em"),
        text_align="center"
        
    )
