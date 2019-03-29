
file = open('test_data.txt', 'w')

for i in xrange(1000):
    if i > 0:
        file.write("\n")
    file.write('0' * (16 - len(str(i))) + str(i))

file.close()
    
