"""Welcome to Reflex!."""

from Cancer360 import styles

# Import all the pages.
from Cancer360.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
