### Create a bank account class with two attributes : owner and balances and two methods deposit and withdraw
class Bank():
    def __init__(self, name, ID):
        self.Bname = name
        self.BID = ID
    
    def print_info_Bank(self):
        print('Your Bank information:')
        print ('\tName of Bank: ' + self.Bname)
        print ('\tID of Bank' + self.BID)
        
    
class Bank_Account(Bank):
    def __init__(self, bank_name, bank_ID, owner, balances = 0):
        super().__init__(bank_name, bank_ID)
        self.owner = owner
        self.balances = balances
        
    def print_Account_info(self):
        self.print_info_Bank()
        print('Your Account information:')
        print('\tAccount Name: ' + self.owner)
        print('\tAccount Balance: {}'.format(self.balances)) 

    def deposit(self, money):
        print('You deposited {} to your account '.format(money) + self.owner)
        print('Your total balances  after deposit is: {}'.format (self.balances + money))
        confirm = '' #check to confirm condition
        
        while confirm != 'Y' and confirm !='N':
            confirm = input('Do you sure you want to deposit( enter Y or N): ')
            
        if confirm == 'Y': #decide base on confirm
            self.balances = self.balances + money
            print('DEPOSIT SUCCESSFULLY')
            return True
        else:
            print('DEPOSIT DECINED')
            return False
        
    def withdraw(self,money):
        if money > self.balances:
            print('You dont have enough money to withdraw')
            print('Please choose amount smaller than {}'.format(self.balances))
            print('WITHDRAW DECINED')
            return False
        else:
            print('you withdraw {} from your account'.format(money))
            print('you new balance is {}'.format(self.balances - money))
            confirm = '' #check to confirm condition
            while confirm != 'Y' and confirm !='N':
                confirm = input('Do you sure you want to withdraw( enter Y or N): ')
            if confirm == 'Y': #decide base on confirm
                self.balances = self.balances - money
                print('WITHDRAW SUCCESSFULLY')
                return True
            else:
                print('WITHDRAW DECINED')
                return False
        
    
    
################Main#################
BANK_NAME = 'Norea'
BANK_ID = 'NO_SE12345'

ACCOUNT_NAME = input('Insert your bank account name to create your account: ')
My_Account = Bank_Account(BANK_NAME,BANK_ID, ACCOUNT_NAME,0)
My_Account.print_Account_info()

total_D = 0
total_W = 0

choice = True
while choice == True:
    service = ''
    while service!='D' and service !='d' and service !='W' and service !='w': # D is for deposit and W for withdraw
        service = input('Choose your service D/d for Deposit or W/w for withdraw: ')
        
    if service =='D' or service == 'd':
        money = ''
        while money.isdigit() == False:
            money = input('Insert your money you want to deposit: ')
        deposit = My_Account.deposit(int(money))
        if deposit == True:
            total_D += 1
    else:
        money = ''
        while money.isdigit() == False:
            money = input('Insert your money you want to withdraw: ')
        withdraw = My_Account.withdraw(int(money))
        if withdraw == True:
            total_W += 1
            
    cont_service = ''
    while cont_service !='Y' and cont_service !='N':
        cont_service = input('Do you want to continue with our services (deposit and withdraw). Please choose Y or N: ')
        
    if cont_service == 'N':
        choice = False
        print ('Total {} successful deposit times and {} successful withdraw times'.format(total_D, total_W))
        My_Account.print_Account_info()
        print ('Thanks for using our service. GOODBYE!')    
    
