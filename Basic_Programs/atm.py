print("SYNDICATE BANK\nMANAKAPUR\n591216\nA Govt. Of India Undertaking\n\n\n")
pin = ""
amt = 19800.00
n = ""
while pin != 8079: 
    pin = int(input("Enter The Pin\n")) 
    if pin != 8079:
        print('Invalid Password\n')
        
print("\n\t\t\tATM Menus\n")
print("\t1.Fast Cash \t\t\t 5.Deposit\n")
print("\t2.Found Transfer \t\t 6.Withdrawal\n")
print("\t3.PIN Change \t\t\t 7.Balance Enquiry\n")
print("\t4.Other Services \t\t 8.Mini Statement\n\n")


while n <= 8:
    n = int(input("\nPlease select your transaction\n"))
    if n == 1:
        print("Your Balance is "+str(amt))
        break
    # elif n == 2:
    #     print("Your Balance is "+str(amt))
    #     break
    # elif n == 3:
    #     print("Your Balance is "+str(amt))
    #     break
    # elif n == 4:
    #     print("Your Balance is "+str(amt))
    #     break
    # elif n == 5:
    #     print("Your Balance is "+str(amt))
    #     break
    # elif n == 6:
    #     print("Your Balance is "+str(amt))
    #     break
    # elif n == 7:
    #     print("Your Balance is "+str(amt))
    #     break
    # elif n == 8:
    #     print("Your Balance is "+str(amt))
    #     break
    
    
print("Invalid Choice\n")
