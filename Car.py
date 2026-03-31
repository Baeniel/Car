from Class import car


while True:
    if "driving":
        mycar = car(brand=None, model=None, year=None, status=None)
        print(mycar.drive())
        break
    else:
        mycar = car(brand=None, model=None, year=None, status=None)
        print(mycar.stop())
        break