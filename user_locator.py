import requests
from math import inf


class SpeedUser:
    def __init__(self, latitude, longitude, name, email):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.email = email

    def __str__(self):
        return f"User: name={self.name}, email={self.email}, latitude={self.latitude}, longitude={self.longitude}"


def find_user_by_latitude(latitude):
    response = requests.get("https://jsonplaceholder.typicode.com/users")  # Get users data from the API
    users_data = response.json()
    closest_user = None
    closest_difference = inf

    for user_data in users_data:  # Loop through the users data to find the user with the same latitude as the input, or the user with the closest latitude
        user_latitude = float(user_data["address"]["geo"]["lat"])
        if user_latitude == latitude:
            return SpeedUser(user_latitude, user_data["address"]["geo"]["lng"], user_data["name"], user_data["email"])
        else:
            difference = abs(user_latitude - latitude)
            if difference < closest_difference:
                closest_user = SpeedUser(user_latitude, user_data["address"]["geo"]["lng"], user_data["name"],
                                         user_data["email"])
                closest_difference = difference

    return closest_user


def print_random_users(num_of_users):
    for i in range(num_of_users):  # Loop for the number of requested users
        response = requests.get("https://randomuser.me/api/")  # Get a random user data from the API
        user_data = response.json()["results"][0]
        name = f"{user_data['name']['title']} {user_data['name']['first']} {user_data['name']['last']}"
        print(f"User {i + 1}: {name}")


# Example usage
user_latitude = float(input("Enter your latitude: "))
user = find_user_by_latitude(user_latitude)
print(user)

num_of_users = int(input("Enter the number of users to print: "))
print_random_users(num_of_users)
