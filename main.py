import json
from hotel_booking import BookMyHotelClient

def main():

    with open('config_file.json', 'r') as file:
        config_data = json.load(file)

    with open('booking_data.json', 'r') as file:
        booking_data = json.load(file)

    base_url = config_data['base_url']
    user_name= config_data['username']
    password = config_data['password']

    client= BookMyHotelClient(base_url,user_name,password)

    health= client.check_health(base_url)

    if health.status_code != 201 or health.status_code == 200:
        raise Exception(f"Health is not OK: {health.status_code}")

    store_ids=[]
    for create_booking in booking_data:
        bookings= client.create_booking(create_booking)
        store_ids.append(bookings['bookingid'])

    booking_ids= client.get_booking_ids()


    with open('test1_update.json', 'r') as file:
        update_test1 = json.load(file)

    updatedBooking1= client.partial_update_booking(store_ids[0],update_test1)

    with open('test2_update.json', 'r') as file:
        update_test2 = json.load(file)

    updatedBooking2= client.partial_update_booking(store_ids[1],update_test2)


    client.delete_booking(store_ids[0])

if __name__ == "__main__":
    main()
