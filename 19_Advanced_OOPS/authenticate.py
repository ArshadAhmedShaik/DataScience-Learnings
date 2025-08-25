logged_in = False

def authenticate(func):
    def wrapper(*args, **kwargs):
       if not logged_in: 
          print("Access Denied")
       else:   
          func(*args, **kwargs)
    return wrapper  

@authenticate
def view_balance():
    print("Balance: 5000")

@authenticate
def transfer_money():
   print("Money transferred")


view_balance()
transfer_money()

logged_in = True

view_balance()
transfer_money()

