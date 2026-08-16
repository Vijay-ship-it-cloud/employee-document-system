import pytest
from rest_framework.test import APIClient
from employees.models import Employee


@pytest.mark.django_db
def test_create_employee():

    client = APIClient()

    data = {
        "name": "Test Employee",
        "email": "test@example.com",
        "department": "IT",
        "designation": "Developer"
    }

    response = client.post(
        "/api/employees/",
        data,
        format="json"
    )

    assert response.status_code == 201
    assert Employee.objects.count() == 1
    assert response.data["name"] == "Test Employee"