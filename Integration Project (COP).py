""""My Sweet Integration Project"""
__author__ = "Mark Edwards"
"""For this program you will enter the name of a company
From there you will be given the open and close stock price"""
import math


def main():
    """The goal of this function is to find stock prices over time, and to
    calculate the value of certain stocks"""
    name = input("What is your first name?")
    name2 = input("What is your last name")
    full_name = name + " " + name2
    print("Hi,", full_name,
          "welcome to my integration project. Today we will learn about "
          "stocks,", end="")
    print("\nand how to calculate prices over time.")
    company = input("Choose a company from the list below \n"
                    "Amazon, Google, Apple, Tesla, Microsoft, and Paypal, :")
    # Now you will enter a company name, and learn about the starting
    # prices of 2021
    if company == 'Amazon':
        opening_price = 2562.00
        print("The opening price for ", company, " in 2020 was $",
              format(opening_price, ".2f"), sep='')
    elif company == 'Google':
        opening_price = 2067.00
        print("The opening price for ", company, " in 2020 was $",
              format(opening_price, ".2f"), sep='')
    elif company == 'Apple':
        opening_price = 132.03
        print("The opening price for ", company, " in 2020 was $",
              format(opening_price, ".2f"), sep='')
    elif company == 'Tesla':
        opening_price = 726.15
        print("The opening price for ", company, " in 2020 was $",
              format(opening_price, ".2f"), sep='')
    elif company == 'Microsoft':
        opening_price = 230.33
        print("The opening price for ", company, " in 2020 was $",
              format(opening_price, ".2f"), sep='')
    elif company == 'Paypal':
        opening_price = 268.89
        print("The opening price for ", company, " in 2020 was $",
              format(opening_price, ".2f"), sep='')
    else:
        print("Sorry, you did not enter one of the given names.")

    buy_type = input("Enter the ticker of the stock you would like to buy:")
    print("The price per share for", buy_type, "is $25.00")
    # Now you will enter how many shares you would like to buy
    while True:
        try:
            buy_amount = int(input(
                "Enter the number of shares you would like to buy as a whole"
                " positive number:"))
            if buy_amount >= 0:
                break
                # This shows that I know what a break statement is
        except ValueError:
            print("Error. Must be a positive whole number")
    # The following formula will give you the price of the stocks that you want
    # to buy

    calculate_total_cost(buy_amount)
    print("The total cost will be $",
          format(calculate_total_cost(buy_amount), '.2f'), sep='')
    # Now we will give a hypothetical for how much you can sell it for
    print("On average the monthly stock growth for", buy_type, "is 10.68%")
    while True:
        try:
            time_to_hold_stock = int(input(
                "Enter the number of months that you would like to own this "
                "stock"))
            if time_to_hold_stock >= 0:
                break
        except ValueError:
            print("Error. Must be a positive whole number of months")
    # Now we will calculate how much the stock is worth after x number of
    # months
    time_for_loop = 1
    total_end_price = calculate_total_cost(buy_amount)
    if time_to_hold_stock >= 0:
        while time_for_loop <= time_to_hold_stock:
            total_end_price *= 1.168
            # We can use shortcut operators to look fancy
            time_for_loop += 1
        print("The price of the stock after ", time_to_hold_stock, " months "
                                                                   "is $",
              format(total_end_price, '.2f'), sep='')
    else:
        print("You need to enter a positive number for months")

    # Hopefully you made lots of money!
    print(
        "Yay! You made lots of money, now let's see how much you could have "
        "made"
        " had you held onto the stock for even longer")
    # Now we will calculate the price for a new amount of time
    while True:
        try:
            time_new = int(
                input("Enter a new number of months to hold onto your stock"))
            if time_new >= 0:
                break
        except ValueError:
            print("Error. Must be a positive number of months")
    price_new = total_end_price + (
            1.168 * (time_new - time_to_hold_stock) * 25)
    print("You could have made upwards of $", format(price_new, '.2f'), sep='')
    # Calculate the difference in prices over the two time periods
    cost_over_time = price_new - total_end_price
    print("The amount of money that you missed out on was $",
          format(cost_over_time, '.2f'), sep='')
    # Now let's ask the uer a simple True or False question
    print("True or False, if you had held onto your money for more than ",
          time_for_loop, "months, you would have made more money.")
    print(price_new > total_end_price)
    # Let's say you want to put a down payment on a new car
    # We will test to see if you the amount of money you have made after "time"
    # months is enough for the down-payment
    car = input("What kind of car would you like to put a down payment on?")
    print("The down payment to buy a new", car, "is $650")
    print("Have you made enough money from your stocks to afford this car?")
    # See how much money you may have left
    amount_left = total_end_price - 650
    if total_end_price >= 650:
        print("Congrats! You have a new car.")
        print("Even better, you still have $", format(amount_left, '.2f'),
              sep='')
    else:
        print("Sorry, today was not your day, the car will have to wait.")
        print("You were only able to make $", format(total_end_price, '.2f', ),
              sep='')
        print("The amount you needed was $650")

    # Now we will do some simple math calculations
    print("Now we will do some math calculations")
    print(
        "Let's quickly find the price of a $100 stock after 4 days, that grows"
        " 15% per day")
    math_stock_price()
    print(
        "How many stocks can you buy if a stock costs $8 and you have $24 to "
        "spend? ")
    print("24 / 8")
    # Now we will see if you can correctly guess the output of the equation
    while True:
        try:
            guess = float(
                input("What do you think the following output will be?"))
            break
        except ValueError:
            print("Error. Must be a positive number")

    if guess != 3:
        print("Unfortunately that is not correct. The answer is", 3)
    else:
        print("Correct, the answer is", guess)
    print("How much money will be left over if instead you have $25 to spend?")
    print("25 % 8")
    print(25 % 8)
    print(
        "Let's now see another way in which you can see how many stocks you "
        "can"
        " buy with $25")
    print("25 // 8")
    print(25 // 8)

    # This is where I will use AND and OR
    print(
        "Now we are going to look at one user inputted stock price and "
        "display some information about it.")
    while True:
        try:
            user_stock_1 = int(
                input("Enter a stock price rounded to the nearest number: "))
            if user_stock_1 >= 0:
                break
        except ValueError:
            print("Error. Must be a positive, whole number.")
    if user_stock_1 >= 100 or user_stock_1 <= 0:
        print("This stock is either very expensive, or doesn't exist.")
    elif 100 >= user_stock_1 >= 50:
        # Another way of displaying this is:
        # elif user_stock_1 <= 100 and user_stock_1 >= 50:
        print("This stock is certainly affordable. ")
    elif user_stock_1 <= 50:
        print("Sounds like you picked a startup, good luck with it!")
    # This is where I will use NOT
    while True:
        try:
            ran_number = float(
                input("Give me a random number between 1 and 10"))
            break
        except ValueError:
            print("Error. Must be number")
    if not ran_number >= 1:
        print("You are not good at following directions.")
    elif not ran_number <= 10:
        print("You are not good at following directions.")
    else:
        print("Way to follow directions")
    # Now we will combine two string inputs in order to buy two stocks
    stock_name_1 = input("Enter a stock ticker")
    stock_name_2 = input("Enter another stock ticker")
    choose_stocks(stock_name_1, stock_name_2)

    print("Let's quickly find the price of a stock after 4 days")
    math_stock_price()
    print(
        "Stocks are fun, let's print this statement 3 times so we can "
        "remember it,\nthere are two ways we can do this."
        " We can use arithmetic or a for loop.")

    # WE can use a for loop to keep printing the statement for a certain
    # pre-determined range
    for x in range(3):
        print("Stocks are fun!", end="")
    print()
    print("Stocks are fun!" * 3)
    # This will be the closing for now
    print(
        "Please comeback and learn more and more about stocks, and how"
        " to calculate future prices.")
    # Here are my references
    print("This is my references section:")
    print(
        "???Alphabet Inc Growth Comparisons.??? Alphabet Inc (GOOG) Growth Rates "
        "Comparisons to Internet "
        "Services &amp; Social Media Industry, Sector, Market. Sales, "
        "Income, EPS, "
        "csimarket.com/stocks/growthrates.php?code=GOOG. ")
    print("Assistance by Rachel Matthews")


def calculate_total_cost(buy_amount):
    """This calculates the total cost assuming the number of shares is
    positive"""
    if buy_amount < 0:
        print("Error or you can not have a negative number")
    else:
        total = buy_amount * 25
        return total


def get_math(a):
    """This calculates how much a stock worth $100 grows over 4 days as a
    constant rate"""
    price_four_day_growth = 100
    for x in range(a):
        price_four_day_growth *= 1.15
    return price_four_day_growth


def math_stock_price():
    """This takes the answer for get_math() and will display it in a
    dollar format"""
    print("The price of the stock after 4 days with a constant growth rate "
          "of 15% per day is", format(get_math(5), '.2f'))


def choose_stocks(stock_name_1, stock_name_2):
    """This takes two stocks and just displays what they entered"""
    print("The stocks you choose were", stock_name_1, "and", stock_name_2)


def get_math_growth(a):
    """This takes a stock worth $100 and then shows what the end price
    is with a 15% growth"""
    price = 100
    for x in range(a):
        price *= 1.15
    return price


main()
