class Bank:
    account = 1000
    limit_for_loan = 500
    limit_for_withdraw = 100

    def withdraw_money(self, amount) :
        cnt = amount // self.limit_for_withdraw
        rest = amount % self.limit_for_withdraw
        for i in range(cnt):
            print(f'This is your money {self.limit_for_withdraw} dollar')
        print(f'This is your money {rest} dollar')

    def givememoney(self, amount): 
        if amount <= self.account:
            self.withdraw_money(amount)
        elif amount <= (self.account + self.limit_for_loan): 
            print('Wait!!')
        else : 
            print('Not enough money')

hana_bank = Bank()
sinhan_bank = Bank()

hana_bank.givememoney(450)