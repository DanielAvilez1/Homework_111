import requests

URL = "http://127.0.0.1:5000/vehicle"


def create_user(year, make, model):
    user = {
        "year": year,
        "make": make,
        "model": model
    }
    response = requests.post(URL, json=vehicle)
    if response.status_code == 201:
        print(
            "Successfully created new record; Got: %s"
            % response.json().get("message")
        )
    else:
        print(
            "Something went wrong while trying to create a new user."
        )


if __name__ == "__main__":
    year = input("Type in the user's year: ")
    make = input("Type in the user's make: ")
    model = input("Type in the user's model: ")
    create_user(year, make, model)
