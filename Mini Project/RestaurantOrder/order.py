class Order:

    orderMenu = {
        "Tandoori Paneer Tikka":	220,
        "Malai Paneer Tikka":	220,
        "Soya Tandoori Tikka": 	175,
        "Tandoori Aloo":	179,
        "Punjabi Soya Chap":	179,
        "Hare-Bhare Kabab":	162,
        "Dahi ke Kabab":	179,
        "Platter":	325
    }    
    items = []
    total = 0
    def __int__(self):
        self.total = 0
        self.items = []

    def AddToOrder(self):
        
        for key in self.orderMenu.keys():
            print(key)
             
        while True:
            item = input("Enter your item to order :")
            self.items.append(item)
            self.total += self.orderMenu[item]
            ordermore = input("do you want to order more ? ( y / n ):")
            if ordermore == 'y':                
                continue
            else:
                break

    
    def PrintReciept(self):
        # gst = float(input("Enter GST :"))
        # sgst = float(input("Enter SGST :"))

        print(f'{"Items":20}{"Qty":10}{"Price":10} {"Unit Total"}')
        for item in set(self.items):
            print(f'{item:20}{self.items.count(item)}        {self.orderMenu[item]}             {self.orderMenu[item] * self.items.count(item)}  ')
        

        print(f'{"Total":30}{self.total}')


    
            

