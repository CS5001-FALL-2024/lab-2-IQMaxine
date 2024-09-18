def main():
    month = input("Enter month: ")
    #determine the number of days
    if month == "Feb":
        days = 28
    elif month == "Sep" or month =="Apr" or month == "Jun" or month == "Nov":
        days = 30
    else:
        days = 31
    print(month, "has", days, "days")

main()
