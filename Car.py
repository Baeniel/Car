from Class import car

while True:
    mycar = car(brand=None, model=None, year=None)
    mycar.status()
    if mycar.status == "driving":
        print(mycar.drive())
        break
    else:
        print(mycar.stop())
        break
