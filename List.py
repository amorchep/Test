# def add(a, b):
#     return a + b
 
# print( add(1, 2) )
print(1, 2, 3, sep='-')
# print(10, end="")

# pupil = "Ben"
# old = 16
# grade = 9.2
# print("It's %s, %d. Level: %f" % (pupil, old, grade)) # It's Ben, 16. Level: 9.200000


# n = "Stiv"
# y = 25
# l = 1.8
#  Sav = "Information Users: %s - Lvl: %d  \n  Exp: %f ---> next exp 3" % (n, y, l)
# f = open('new.txt', 'w+')
# f.write(Sav)
# f.close()
# print(Sav)

# Name = input()
# FName = input()
# print("What's you name? \n -{0} \nWhat's plan? \n -{1} \n" .format(Name, FName))

m = int(input('Exp - '))
g = float(input('Dubl exp - '))

x = m + g

Save = 'All exp: ', x, 'good job'
s = str(Save)
f = open('new.txt', 'w+')
f.write(s)
f.close()

print(s)
