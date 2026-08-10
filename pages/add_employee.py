import streamlit as st

from api.employee_api import add_employee
from utils.helper import add_local_employee


st.title("Add employee")
st.caption("Create a new employee record.")

with st.form("add_employee_form", clear_on_submit=True):
    name = st.text_input("Full name", placeholder="Jane Doe")
    username = st.text_input("Username", placeholder="janedoe")
    email = st.text_input("Email", placeholder="jane.doe@example.com")
    phone = st.text_input("Phone", placeholder="+1 555 0100")
    company = st.text_input("Company", placeholder="Acme Inc.")
    submitted = st.form_submit_button("Add employee", type="primary")

if submitted:
    if not name.strip() or not email.strip():
        st.error("Full name and email are required.")
    else:
        employee_data = {
            "name": name.strip(),
            "username": username.strip(),
            "email": email.strip(),
            "phone": phone.strip(),
            "company": {"name": company.strip()},
        }
        try:
            created_employee = add_employee(employee_data)
        except RuntimeError as exc:
            st.error(str(exc))
        else:
            add_local_employee(created_employee)
            st.success(f"{created_employee['name']} was added successfully.")