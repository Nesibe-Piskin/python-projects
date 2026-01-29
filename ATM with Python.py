#ATM with Python

xAccount = {
    "first name" : "User First Name",
    "last name" : "User Last Name",
    "phone number" : 5555555555,
    "balance" : 10000,
    "overdraft limit" : 5000
}

loop_Count= int(input("How many times do ypu want to loop to run : "))
for x in range (loop_Count):


    def withDraw (account):
        amount = float(input("Enter the amount to withdraw : "))

        if (account["balance"] >= amount):
            print("You have successfully withdrawn money from your account")
            newAmount = account["balance"] - amount
            account.update({"balance" : newAmount})
            print(f"Kalan bakiyeniz = {account['balance']}")
        
        else:
            toplam = account["balance"] + account["overdraft limit"]
            if toplam >= amount:
                overDraftLimit = input("Would you like to withdraw money from your overdraft? : y/n ")
                if overDraftLimit == "y":
                    print ("Para çekme işlemi tamamlanmıştı.")
                    lastAmount = amount - account["balance"]                
                    account.update({"balance":0})
                    print(f"kalan bakiyeniz = {account["balance"]}")
                    newOverDraftLimit =account["overdraft limit"] - lastAmount
                    account.update({"overdraft limit":newOverDraftLimit})
                    print(f"Your remaining = {account["overdraft limit"]}")

                elif ekHesap == "n":
                    print("Insufficient balance for the amount entered")

                else:
                    print("Invaild amount entered")

            else:
                print("The amount you want to withdraw is not available in your account")
                
    withDraw(xAccount)