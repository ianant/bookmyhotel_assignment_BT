import requests
from logger import logger

class BookMyHotelClient:
    def __init__(self, base_url,user_name,password):
        self.base_url = base_url
        self.user_name=user_name
        self.password=password
        self.token = self.create_token(base_url, user_name, password)

    def check_health(self,base_url):
        url = f"{base_url}/ping"
        response = requests.get(url)
        logger.info(f"Health status is OK: {response.status_code}")
        return response

    def create_token(self, url, username, password):
        try:
            url = f"{url}/auth"
            payload = {
                'username': username,
                'password': password
            }
            headers={
                "Content-Type" : 'application/json'
            }
            response = requests.post(url, json=payload,headers=headers)
            self.token = response.json().get('token')
            return self.token
        except Exception as exe:
            raise exe

    def get_booking_ids(self):
        try:
            url = f"{self.base_url}/booking"
            response = requests.get(url)
            logger.info(f"All available booking Ids are: {response.json()}")
            return response.json()
        except Exception as exe:
            raise exe

    def create_booking(self, booking_data):
        try:
            url = f"{self.base_url}/booking"
            headers={
                "Content-Type": "application/json"
            }
            response = requests.post(url, json=booking_data, headers=headers)
            logger.info(f"Booking Details for newly created bookings are: {response.json()}")
            return response.json()
        except Exception as exe:
            raise exe


    def partial_update_booking(self, id, booked_data):
        try:
            url = f"{self.base_url}/booking/{id}"
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f'token={self.token}'

            }
            response = requests.patch(url, json=booked_data, headers=headers)
            logger.info(f"Updated booking with ID: {response.json()}")
            return response.json()
        except Exception as exe:
            raise exe

    def delete_booking(self, booking_id):
        try:
            url = f"{self.base_url}/booking/{booking_id}"
            headers = {
                "Content-Type": "application/json",
                "Cookie": f'token={self.token}'
            }
            response = requests.delete(url, headers=headers)
            logger.info(f"booking deleted with the Id: {booking_id}")
            return response
        except Exception as exe:
            raise exe


