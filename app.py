import streamlit as st


st.set_page_config(
    page_title="Employee Management",
    page_icon="👨‍💼",
    layout="wide",
)


dashboard_page = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
    default=True,
)
employees_page = st.Page(
    "pages/employees.py",
    title="Employees",
    icon=":material/groups:",
)
add_employee_page = st.Page(
    "pages/add_employee.py",
    title="Add employee",
    icon=":material/person_add:",
)
update_employee_page = st.Page(
    "pages/update_employee.py",
    title="Update employee",
    icon=":material/edit:",
)

pg = st.navigation(
    {
        "Employee management": [
            dashboard_page,
            employees_page,
            add_employee_page,
            update_employee_page,
        ]
    }
)
pg.run()
