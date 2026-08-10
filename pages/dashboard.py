import streamlit as st
from api.employee_api import get_employees
from utils.helper import get_local_employees
from datetime import datetime

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 85% 80%,
                rgba(93, 132, 160, 0.35),
                transparent 30%
            ),
            #f5f6f1;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #263747 0%,
            #34495e 100%
        );
        min-width: 270px;
        max-width: 270px;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 25px;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .sidebar-title {
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 18px;
        color: #eeeeee;
    }

    [data-testid="stSidebar"] .stButton button {
        width: 100%;
        border: none;
        border-radius: 7px;
        background: transparent;
        color: #ffffff;
        text-align: left;
        padding: 10px 14px;
        font-size: 14px;
        transition: all 0.2s ease;
    }

    [data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.10);
    }

    [data-testid="stSidebar"] .dashboard-btn button {
        background: linear-gradient(
            90deg,
            #5ba5bd,
            #679eb3
        );
        box-shadow:
            0 3px 10px rgba(0,0,0,0.15);
    }

    .main-title {
        font-size: 40px;
        font-weight: 800;
        color: #2d201b;
        margin-top: 35px;
        margin-bottom: 8px;
    }

    .main-description {
        font-size: 14px;
        color: #5d5d5d;
        margin-bottom: 8px;
    }

    .date-time {
        font-size: 13px;
        color: #777;
        margin-bottom: 25px;
    }

    .metric-card {
        background: linear-gradient(
            135deg,
            #f3ffff,
            #e8f8fa
        );
        border-radius: 12px;
        padding: 17px 15px;
        height: 105px;
        box-shadow:
            0 3px 8px rgba(0,0,0,0.12);
        border: 1px solid rgba(180,220,225,0.5);
    }

    .metric-title {
        font-size: 13px;
        color: #333;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 500;
        color: #111;
    }

    .quick-title {
        font-size: 28px;
        font-weight: 700;
        color: #33241e;
        margin-top: 25px;
        margin-bottom: 12px;
    }

    .add-button button {
        background: #ff6868 !important;
        color: white !important;
        border: none !important;
        border-radius: 9px !important;
        height: 42px;
        font-size: 14px;
        box-shadow:
            0 3px 7px rgba(0,0,0,0.15);
    }

    .add-button button:hover {
        background: #f45b5b !important;
    }

    .view-button button {
        background: #edf1f2 !important;
        color: #333 !important;
        border: none !important;
        border-radius: 9px !important;
        height: 42px;
        font-size: 14px;
        box-shadow:
            0 3px 7px rgba(0,0,0,0.10);
    }

    .view-button button:hover {
        background: #e0e5e7 !important;
    }

    .block-container {
        padding-top: 1rem;
        padding-left: 5rem;
        padding-right: 4rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


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

email_count = sum(
    bool(employee.get("email"))
    for employee in employees
)

st.markdown(
    '<div class="main-title">Employee Management System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-description">'
    'Manage and view your employees from one place.'
    '</div>',
    unsafe_allow_html=True
)

current_datetime = datetime.now().strftime(
    "%d/%m/%Y %I:%M %p"
)

st.markdown(
    f'<div class="date-time">◷ &nbsp; {current_datetime}</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">
                Total employees
            </div>
            <div class="metric-value">
                {active_count}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">
                Companies
            </div>
            <div class="metric-value">
                {len(companies)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">
                Employees with email
            </div>
            <div class="metric-value">
                {email_count}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="quick-title">Quick actions</div>',
    unsafe_allow_html=True
)

action_one, action_two = st.columns(2)

with action_one:

    st.markdown(
        '<div class="add-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "Add an employee",
        use_container_width=True
    ):
        st.switch_page("pages/add_employee.py")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

with action_two:

    st.markdown(
        '<div class="view-button">',
        unsafe_allow_html=True
    )

    if st.button(
        f"View employees     {active_count}",
        use_container_width=True
    ):
        st.switch_page("pages/employees.py")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )