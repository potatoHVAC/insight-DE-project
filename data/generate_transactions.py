from random import randint

file = open('hundred_thousand_transactions.txt', 'w')

def random_cc_number():
    return ''.join([ str(randint(0,9)) for i in range(16) ])

cc_numbers = [random_cc_number() for i in range(1000)]

for i in range(100000):
    transaction = str(randint(1,200))
    cc_number = cc_numbers[randint(0, len(cc_numbers) - 1)]
    file.write(''.join([cc_number, ',', transaction, '\n']))
    
