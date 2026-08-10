import requests
from config import BASE_URL


def get_employees():
    try:
        response = requests.get(f"{BASE_URL}/users", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        raise RuntimeError("Unable to load employees from the API.") from exc


def add_employee(employee_data):
    try:
        response = requests.post(
            f"{BASE_URL}/users",
            json=employee_data,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        raise RuntimeError("Unable to add the employee.") from exc
