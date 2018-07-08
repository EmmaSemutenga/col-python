class Tab:
    #menu is a class attribute
    menu = {
        'wine': 5,
        'beer': 3,
        'chicken':10,
        'beef':15,
        'veggie':12
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add_item(self, *itemname): #expects a turple
        for item in list(itemname): #turple is converted to list before looping
            self.items.append(item)
            self.total += Tab.menu[item]
        
       

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total

        total = self.total + tax + service

        for item in self.items:
            print(f'{item} UGX{Tab.menu[item]}')

        print(f'Total UGX{total}')

table1 = Tab()
table1.add_item('wine', 'chicken', 'beef', 'beer')
#table1.add_item('chicken')
table1.print_bill(10, 5)

