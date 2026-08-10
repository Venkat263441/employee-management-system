import pandas as pd
import streamlit as st

from api.employee_api import get_employees
from utils.helper import get_local_employees


st.title("Employees")
st.caption("View all employees currently available in the system.")

if st.button("Refresh employees", icon=":material/refresh:"):
    st.rerun()

try:
    employees = get_employees() + get_local_employees()
except RuntimeError as exc:
    st.error(str(exc))
    employees = get_local_employees()

if not employees:
    st.info("No employees found. Use **Add employee** to create one.")
else:
    rows = [
        {
            "ID": employee.get("id", ""),
            "Name": employee.get("name", ""),
            "Email": employee.get("email", ""),
            "Phone": employee.get("phone", ""),
            "Company": employee.get("company", {}).get("name", ""),
        }
        for employee in employees
    ]
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)