import requests

def create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 201:
        data = response.json()
        user_id = data.get("id")
        print(f"User created successfully. User ID: {user_id}")
    else:
        print(f"Failed to create user. Status Code: {response.status_code}")
        print(response.json())

def login_unsuccessful():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "test@example.com",
        "password": "invalidpassword"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 400:
        data = response.json()
        error_message = data.get("error")
        print(f"Login unsuccessful. Error Message: {error_message}")
    else:
        print(f"Failed to perform login. Status Code: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    create_user()
    login_unsuccessful()
