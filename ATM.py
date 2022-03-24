class atm(object):
    def __init__(self, card_no, pin_no):
        self.card_no = card_no
        self.pin_no = pin_no

    def CashWithdrawl(self):
        amount = input("Enter the amount: ")
        print("You withdrawed ₹" + amount + " from the bank!")

    def BalanceEnquiry(self):
        print("You have ₹___ in your bank account.")

atm_1 = atm(12345678, 4321)
atm_2 = atm(87654321, 1234)

print(atm_1.CashWithdrawl())
print(atm_2.BalanceEnquiry())