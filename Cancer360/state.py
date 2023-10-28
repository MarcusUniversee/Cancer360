"""Base state for the app."""

import reflex as rx
import re


class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """

    pass

class AppointmentFormState(State):
    form_data: dict = {}
    data_filled: bool = False
    def handle_submit_data(self, form_data: dict):
        self.form_data = form_data
        self.data_filled = True
    def handle_clear_data(self):
        self.form_data.clear()
        self.data_filled = False

class FormErrorState(State):
    input: str

    @rx.var
    def is_date(self) -> bool:
        return re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', self.input)

