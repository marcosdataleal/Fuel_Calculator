class Calculation:
    def __init__(self):
        self.__gasoline_price = 4.80
        self.__alcohol_price = 3.80
        self.__diesel_price = 3.90

    def calculate_expense(self, distance, consumption):
        if (distance <= 0 or consumption <= 0):
            raise Exception(
                'The received value cannot be less than or equal to zero')

        gasoline_expense = round(
            (distance / consumption) * self.__gasoline_price, 2)
        alcohol_expense = round(
            (distance / consumption) * self.__alcohol_price, 2)
        diesel_expense = round(
            (distance / consumption) * self.__diesel_price, 2)

        return """ 
        The total cost will be:

        Gasoline: $ {} 
        Alcohol:  $ {}
        Diesel:   $ {}
        """.format(
            gasoline_expense, alcohol_expense, diesel_expense
        )