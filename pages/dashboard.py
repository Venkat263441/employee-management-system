import streamlit as st

from api.employee_api import get_employees
from utils.helper import get_local_employees
from datetime import datetime

st.title("Employee Management System")
st.caption("Manage and view your employees from one place.")

current_datetime = datetime.now().strftime("%d/%m/%Y %I:%M %p")
st.caption(f"🕒 {current_datetime}")

try:
    employees = get_employees() + get_local_employees()
except RuntimeError as exc:
    st.error(str(exc))
    employees = get_local_employees()

active_count = len(employees)
companies = {
    employee.get("company", {}).get("name", "").strip()
    for employee in employees
    if employee.get("company", {}).get("name", "").strip()
}

first, second, third = st.columns(3)
first.metric("Total employees", active_count)
second.metric("Companies", len(companies))
third.metric("Employees with email", sum(bool(employee.get("email")) for employee in employees))

st.subheader("Quick actions")
action_one, action_two = st.columns(2)
with action_one:
    if st.button("Add an employee", use_container_width=True, type="primary"):
        st.switch_page("pages/add_employee.py")
with action_two:
    if st.button("View employees", use_container_width=True):
        st.switch_page("pages/employees.py")