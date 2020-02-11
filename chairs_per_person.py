f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError as error:
        print(error)
    except ZeroDivisionError:
        chairs_per_person = 0 / int(9)
    
    print("{} will get {} chairs per person".format(name, chairs_per_person))
