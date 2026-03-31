# Object-Oriented Programming (OOP) in Python
# Class for car
class car:
    def __init__(self, brand, model, year, status):
        self.brand = input(f"Enter the brand of the car: ")
        self.model = input(f"Enter the model of the car: ")
        self.year = None
        while self.year != int:
            try:
                self.year = int(input(f"Enter the year of the car: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")
                break
        self.status = None
        while self.status != "driving" and self.status != "stopped":
            self.status = input(f"If the car is driving, enter 'driving' or if the car is stopped, enter 'stopped': ")
            if self.status in ["driving", "stopped"]:
                break
            else:    
                print(f"Invalid input. Please enter 'driving' or 'stopped'.")       
# Method to drive the car
    def drive(self):
        return f"The {self.year} {self.brand} {self.model} is driving."
# Method to stop the car  
    def stop(self):
        return f"The {self.year} {self.brand} {self.model} has stopped."