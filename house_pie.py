#Initial variable to track shopping status
shopping = 'y'
# List to track pie purchases
pie_purchases = []
# Pie List
pie_list = ["Cherry", "Apple ", "Peach", "Pumpkin", "Cheese",
            "Blueberry", "Banana", "Burek","Coconut", "Chocolate", "Strawberry"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("      --------- ***** ------------")
    print("(1) Cherry, (2) Apple , (3)Peach, (4) Pumpkin, " +
          " (5) Cheese, (6) Blueberry, (7) Banana, (8) Burek, " +
          " (9) Coconut, (10) Chocolate, (11) Strawberry")

    pie_choice = input("Which would you like? ")

    # Add pie to the pie list
    pie_purchases.append(pie_choice)

    print("      --------- ***** ------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete
print("      --------- ***** ------------")
print("You purchased a total of " + str(len(pie_purchases)) + ".")
