# x = 9 + 6
# y = 9 + 5
# a = x - y
# sms = 'Connecting Users'
# Location = "Usa"
# print ("New Users", x)
# print ('Location', Location)
# print (sms, a)
# print (x, y)


f = open('new.txt', 'w+')
f.write('_____________________''\n'' ------- >  Bangs 7''\n''_____________________')
f.close()
try:
    f = open('new.txt')
    for line in f:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
# data = f.readlines() # Вывод в одну линию
# print(data)
    f.close()
