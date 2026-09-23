drink = "tea" # defined the drink variable (type is string) and assigned the value "tea" to it.
sales = {"tea": 3, "coffee": 5} # defined the sales variable, but the coffee variable is not defined.
sold = sales[drink] # defined the sold variable. Type is string and assigned the value of the drink variable which is tea to it. The value of sold variable is 3 because the value of tea in the sales dictionary is 3.
sold = sold + 1 # defined the sold variable to add 1 to the sold variable which was defined in the line 3
print(drink) #Now its printing the drink variable which is tea
print(sold) #and the sold variable which is 4 because we added 1 to the sold variable which was 3 in the line 3
