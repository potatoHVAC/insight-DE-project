
file = open('test_data.txt', 'w')

for i in range(10000):
    if i > 0:
        file.write("\n")
    file.write('0' * (16 - len(str(i))) + str(i))

file.close()

