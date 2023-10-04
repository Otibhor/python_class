#try:
def file():
    import random
    import group1 as gp
    Account_name, Password = gp.reg()
    Account_num = random.randint(100000000, 999999999)
    Account_bal = 0.00
    process =True
    while process:

        transaction = input('Withdrawal or Deposit or Cancel? ')

        if transaction == 'Withdrawal':
            value = True
            while value:
                try:
                
                    Debit = float(input('Enter Amount: '))
                except:
                    if bool(Debit):
                        value = False
                    else:
                        value = True

            
            Account_bal = Account_bal - Debit
            print('Account Balance: '+ str(Account_bal))
            process = False

        elif transaction == 'Deposit':
            Credit = float(input('Enter Amount: '))
            Account_bal = Account_bal + Credit
            print('Account Balance: ' + str(Account_bal))
            process = False

        elif transaction == 'Cancel':
            print('No transaction at this time! Bye!')
            Account_bal = Account_bal
            print('Account Balance: '+ str(Account_bal))
            process = False

        else:
            print(EOFError)
            print('Select a Transaction')
            process = True
                
    # except EOFError:
        #print('No selection made')

    account_file = {
    'account_name': Account_name,
    'account_password': Password,
    'account_balance': Account_bal,
    'account_number': Account_num
    }
    #process = False
    return account_file
#except Exception as e:
   # print('The error is: ', e)
     