from calculation import Calculation


def main():
    print(
        """
        This application aims to demonstrate the fuel costs for a trip based on your vehicle's consumption and the distance you specify!
        """
    )

    print("The available fuels for this calculation are:")
    print("\t° Alcohol")
    print("\t° Diesel")
    print("\t° Gasoline")

    print(" ")

    try:
        distance = float(input("Distance in kilometers to be traveled\n"))
        consumption = float(input("Vehicle fuel consumption (Km/l)\n"))
        calculation = Calculation()
        print(
            calculation.calculate_expense(distance, consumption)
        )
    except ValueError as error:
        print("The received value is not valid")


if __name__ == "__main__":
    main()
