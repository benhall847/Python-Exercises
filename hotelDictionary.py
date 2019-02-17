hotel = {
    '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
},
    '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
},
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}
def ServiceApp(hotel_info):
    check_in_out = input('Would you like to check in or out? (in or out): ').lower()
    floor = input('floor number?: ')
    room = input('room number?: ')
    guests = []
    print(hotel_info[floor])
    if check_in_out == 'in':
        if room not in hotel_info[floor]:
            occupants = int(input('Number of occupants?: '))
            for each_person in range(occupants):
                guests.append(input('What is your name?: '))
                hotel_info[floor][room] = guests
        else:
            return("Sorry! Somebody is already checked in that room.")
    if check_in_out == 'out':
        if room in hotel_info[floor]:
            del hotel_info[floor][room]
        else:
            return "Sorry, nobody is checked into that room!"
    return hotel_info

print(ServiceApp(hotel))