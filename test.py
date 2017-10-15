class Coffee:
    def __init__(self,syrup,coffee, milk, cream):
        self.syrup = syrup
        self.coffee = coffee
        self.cream = cream
        self.milk = milk

    def Show_Attr(self):
        print('Syrup : ' + str(self.syrup))
        print('Milk : ' + str(self.milk))
        print('Coffee : ' + str(self.coffee))
        print('Cream : ' + str(self.cream))

    def Question(self):
        variable = True
        Amount = 'How much would you like to add?\n'
        while variable == True:
            add = input("\nWould you like to add 'M'ilk, 'S'yrup', 'C'offee, or c'R'eam?\n")
            if add.upper() == 'M':
                adder = int(input(Amount))
                self.milk += adder
                print('Syrup is now at '+ str(self.milk))
            elif add.upper() =='S':
                adder = int(input(Amount))
                self.syrup += adder
                print('Syrup is now at '+ str(self.syrup))
            elif add.upper() =='C':
                adder = int(input(Amount))
                self.coffee += adder
                print('Syrup is now at '+ str(self.coffee))
            elif add.upper() =='R':
                adder = int(input(Amount))
                self.cream += adder
                print('Syrup is now at '+ str(self.cream))
            else:
                print('sir we do not accept jokes')
                break
            Option = input('Adding anything else? Y/N\n')
            if Option.upper() == 'Y':
                pass
            elif Option.upper() == 'N':
                variable = False
                print('Thank you!')
            else:
                print('sir we do not accept jokes')
                break

class GreenTeaLatte(Coffee):
    def __init__(self,syrup,coffee, milk, cream):
        super().__init__(syrup, coffee, milk, cream)
        self.syrup = 3
        self.coffee = 0
        self.cream = 0
        self.milk = 2
    def printname(self):
        print('Greentealatte')
class CaramelMacchiato(Coffee):
    def __init__(self,syrup,coffee, milk, cream):
        super().__init__(syrup, coffee, milk, cream)
        self.syrup = 1
        self.coffee = 3
        self.cream = 1
        self.milk = 2
    def printname(self):
        print('CaramelMacchiato')

class EspressoShot(Coffee):
    def __init__(self,syrup,coffee, milk, cream):
        super().__init__(syrup, coffee, milk, cream)
        self.syrup = 0
        self.coffee = 8
        self.cream = 0
        self.milk = 0
    def printname(self):
        print('EspressoShot')

print('---------------------------------')
print('------WELCOME TO STARBUCKS------')
print('---------------------------------')
Orders = [1,1,1,1,1,1,1,1]
x = input('How many drinks would you like to order?(max is 8)\n')
for i in range (0,int(x)):
    name = input('What is your order?\n'
                         '1. Caramel Macchiato\n'
                         '2. Green Tea Latte\n'
                         '3. Espresso Shot\n'
                         '4. Custom Coffee?\n')
    if name == '1':
        Orders[i] =  CaramelMacchiato(0,0,0,0)
    elif name == '2':
        Orders[i] = GreenTeaLatte(0,0,0,0)
    elif name == '3':
        Orders[i] = EspressoShot(0,0,0,0)
#    elif name =='4':
#        taste1 = input('Syrup amount?  ')
#        taste2 = input('Milk amount?  ')
#        taste3 = input ('Cream amount?  ')
#        taste4 = input ('Coffee amount?  ')
#        drink = input("what is the drink name?\n")
#        Orders[i] = Coffee(taste1,taste4,taste2,taste3)
#        print(drink+'\n')
for i in range (0,int(x)):
    Orders[i].printname()
    Orders[i].Show_Attr()
