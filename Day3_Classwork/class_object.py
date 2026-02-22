# Class and object practice

class Bank:
    bankname= "SBI"
    ifsc= "SBIN002026"
    loc= "Kolkata"
    timing= "9a.m - 6p.m"
    
    # def set_details(obj, name, age, phone, pan, balance):
    #     obj.name = name
    #     obj.age = age
    #     obj.phone = phone
    #     obj.pan = pan
    #     obj.balance = balance

    def __init__(self, name, age, phone, pan, balance):
        self.name = name
        self.age = age
        self.phone = phone
        self.pan = pan
        self.balance = balance


    def display(self):
        print(self.name, self.phone, self.balance)
    def change_phone(self, new_phone):
        self.phone = new_phone

    def withdraw_money(self,  wmoney):
        if(wmoney<self.balance):
            self.balance = self.balance-wmoney
            print(f"{wmoney} withdrawn \n Available balance: {self.balance}")
        

c1 = Bank("Rishu", 22, 9876543210, "ABCEFIIH", 50000)
c2 = Bank("Ankit", 20, 843987836, "HGGDGXIJ", 17000)
c3 = Bank("Manish", 22, 7634732348, "DYGWGGDW", 15000)


c1.display()
print(c1.change_phone("9999999999"))
c1.display()

# print( c1.bankname, c1.name, c1.balance, c1.pan, c1.phone)
# print( c2.bankname, c2.name, c2.balance, c2.pan, c2.phone)
# print( c3.bankname, c3.name, c3.balance, c3.pan, c3.phone)


# c1 = Bank()
# c1.set_details("Rishu", 22, 9876543210, "ABCEFIIH", 50000)

# c2 = Bank()
# c2.set_details("Ankit", 20, 843987836, "HGGDGXIJ", 17000)

# c3 = Bank()
# c3.set_details("Manish", 22, 7634732348, "DYGWGGDW", 15000)

# print(c1.name)
# print(c2.phone)
# print(c3.balance)
# print(c3.pan)



# e1 = Bank()
# e1.balance = 7000
# e1.address = "Abc"
# e1.age = 21

# e2 = Bank()
# e2.balance = 5000
# e2.address = "Xyz"
# e2.age = 25

# e3 = Bank()
# e3.balance = 1000
# e3.address = "123"
# e3.age = 27

# print(e1.bankname)
# print(e1.balance)
# print(e2.age)
# print(e2.loc)
# print(e3.age)