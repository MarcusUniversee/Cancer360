"""Sidebar component for the app."""

from Cancer360 import styles
from Cancer360.timmystates import State, TimmyState

import reflex as rx

def timmy_state() -> rx.Component:
    
    return rx.text("hello world")