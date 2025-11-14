account = {
    'checking': 1500.00,
    'savings': 3000.00,
}
def add_funds(amount:float,name:str='checking')-> float:
    account[name] += amount
    return account[name]
print('Initial checking balance:', account['checking'])
new_balance = add_funds(500.00)
print('New checking balance after adding funds:', account['checking'] , '--',account['savings'])