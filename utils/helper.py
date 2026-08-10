import streamlit as st


def get_local_employees():
    """Return employees added during this browser session."""
    return st.session_state.setdefault("local_employees", [])


def add_local_employee(employee):
    get_local_employees().append(employee)