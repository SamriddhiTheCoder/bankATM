class atm(object):
    def __init__(self, card_no, pin_no, bal):
        self.card_no = card_no
        self.pin_no = pin_no
        self.bal = bal
        self.newamt = 0

    def CashWithdrawl(self):
        amount = int(input("Enter the amount: "))
        self.newamt = self.bal - amount
        print("You have ₹" + str(self.newamt) + " left in your account!")

    def BalanceEnquiry(self):
        if(self.newamt == 0):
            print("You have ₹" + str(self.bal) + " in your bank account.")
        else: 
            print("You have ₹" + str(self.newamt) + " in your bank account.")

def main():
    user = atm(12345678, 4321, 20000)
    print("Choose an activity") 
    print("1) Balance Enquiry. 2) Cash Withdrawl.")
    act = int(input("Enter activity number: "))

    if(act == 1):
        user.BalanceEnquiry()
    elif(act == 2):
        user.CashWithdrawl()
    else:
        print("Invalid.")
main()