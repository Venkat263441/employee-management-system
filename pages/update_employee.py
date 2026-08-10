import streamlit as st

from api.employee_api import get_employees


st.title("Update employee")
st.caption("Select an employee to review their details.")

try:
    employees = get_employees()
except RuntimeError as exc:
    st.error(str(exc))
    employees = []

if not employees:
    st.info("No API employees are available to update.")
else:
    employee_options = {
        f"{employee.get('name', 'Unnamed')} (ID {employee.get('id', '')})": employee
        for employee in employees
    }
    selected_label = st.selectbox("Employee", list(employee_options))
    selected = employee_options[selected_label]

    with st.form("update_employee_form"):
        name = st.text_input("Full name", value=selected.get("name", ""))
        email = st.text_input("Email", value=selected.get("email", ""))
        phone = st.text_input("Phone", value=selected.get("phone", ""))
        st.form_submit_button("Save changes", disabled=True)

    st.info("Updating existing employees will be connected when the API supports PUT requests.")