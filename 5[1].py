n = int(input("Please enter n:"))
m = int(input("Please enter m:"))
cities = []
airlines = {}
for i in range(n):
    city = input("Please enter the city:")
    if not city in airlines.keys():
        airlines.update({city: []})
for i in range(m):
    flight = input("Please enter the origin & destination :")
    info = flight.split(" ")
    origin = info[0]
    destination = info[1]
    airlines[origin.title()].append(destination)
for i in airlines:
    l = len(airlines.get(i))
    print(l)
    if l:
        for j in airlines.get(i):
            print(j)
