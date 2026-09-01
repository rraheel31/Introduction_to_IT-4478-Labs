#Welcome Message
print("Welcome to the Python Coffee Shop!")
#Asking for the customer's name
Customer_name = input("Please enter your name: ")
print(f"Hello, {Customer_name}! Let's get you a coffee.")
#Coffee Menu And Prices
price_late = 3.50
price_espresso = 2.50
price_mocha = 4.00
decision = "yes"
print("Latte: $" + str(price_late))
print("Espresso: $" + str(price_espresso))
print("Mocha: $" + str(price_mocha))
#Asking for the customer's coffee choice and decision to order
while decision == "yes" and decision != "no":
    decision = input("Would you like to order a coffee? (yes/no): ")
    if decision == "no":
        break
    choice = input("What type of coffee would you like to order? (Latte/Espresso/Mocha): ")
    if choice == "Latte":
        print(f"You have ordered a Latte. That will be ${price_late}.")
        cost = price_late
    elif choice == "Espresso":
        print(f"You have ordered an Espresso. That will be ${price_espresso}.")
        cost = price_espresso
    elif choice == "Mocha":
        print(f"You have ordered a Mocha. That will be ${price_mocha}.")
        cost = price_mocha 
    else:
        print("Sorry, we don't have that option. Please choose either Latte, Espresso, or Mocha.")
        continue
    #Ask for the quantity of coffee

    quantity = int(input("How many cups would you like to order? "))
    #Calculating the total cost
    total_cost = cost * quantity
    if quantity > 1:
        print("You get a discount of $0.10 for ordering more than one cup!")
        total_cost = total_cost - 0.10

    another_order = "yes" 
    while another_order == "yes" and another_order != "no":
        another_order = input("Would you like to order another coffee? (yes/no): ")
        if another_order == "no":
            break
        choice = input("What type of coffee would you like to order? (Latte/Espresso/Mocha): ")
        if choice == "Latte":
            print(f"You have ordered a Latte. That will be ${price_late}.")
            cost = price_late
        elif choice == "Espresso":
            print(f"You have ordered an Espresso. That will be ${price_espresso}.")
            cost = price_espresso
        elif choice == "Mocha":
            print(f"You have ordered a Mocha. That will be ${price_mocha}.")
            cost = price_mocha 
        else:
            print("Sorry, we don't have that option. Please choose either Latte, Espresso, or Mocha.")
            continue
        quantity = int(input("How many cups would you like to order? "))
        total_cost += cost * quantity
        ultimate_cost = total_cost + cost
        
    ultimate_cost = total_cost


    #Asking if the customer is a student
    input_student = input("Are you a student? (yes/no): ")
    if input_student == "yes":
        print("You get a student discount of $10%!")
        ultimate_cost = ultimate_cost - (ultimate_cost * 0.1)
        print(f"Your total cost is ${ultimate_cost}.")
        print(f"Thank you, {Customer_name}! For your order! Your coffee will be ready shortly.")
        break
    elif input_student == "no":
        print("No student discount applied.")
        print(f"Your total cost is ${ultimate_cost}.")
        print(f"Thank you, {Customer_name}! For your order! Your coffee will be ready shortly.")
        break



print("Thank you for visiting the Python Coffee Shop! Have a great day!")