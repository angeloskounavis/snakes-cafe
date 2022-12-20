from textwrap import dedent
def welcome_snakes():
    print("Welcome to the Snakes Cafe!")
    print("Please see our menu below.\n")
    print("To quit at any time, type quit")

def menu():
  """
  This will show menu
  """
  #print("What is your favorite color?")
  #fav_color = input("> ")
  #print(f"Your favorite color is {fav_color}")

  print(dedent("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
  """))

  order_cart = {
    # "key": "value",
  }

  print("What would you like to order?")
  ordering = input("> ")
  if ordering in order_cart:
    order_cart[ordering] += 1
  else:
    order_cart[ordering] = 1
  print(f"You have added {order_cart[ordering]} {ordering} to your cart")

  #order_cart = {
    #"key": "value",
  #}

  ask_again = True
  while ask_again:
    print("You like to order another item?")
    choice = input("> ")
    if choice == "y" or choice == "yes":
      print("What would you like to order?")
      ordering = input("> ")
      print(f"You have an order of {ordering}")
      #if color_dict.update()[fav_color]:
      if ordering in order_cart:
          order_cart[ordering] += 1
          print(f"You have added {order_cart[ordering]} {ordering} to your cart")
      else:
        order_cart[ordering] = 1
        print(f"You have added {order_cart[ordering]} {ordering} to your cart")
    else:
      break
  print(f"Your orders are {order_cart}")

if __name__ == "__main__":
  #hello_world()
  welcome_snakes()
  menu()


