# Create a Car class with brand, model, and a drive() method.

class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")


def main():
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    car = Car(brand, model)
    car.drive()


if __name__ == "__main__":
    main()
