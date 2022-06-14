import sys
from prettytable import PrettyTable
class Farmprice():
    def __init__(self,list_items):
        self.prices = {'CH1': 3.11, 'AP1': 6.00 , 'CF1': 11.23,'MK1': 4.75, 'OM1': 3.69}
        self.farm_list_items = list_items
        self.final_price = 0
        self.billing()
        #self.print_bill = PrettyTable()
        #self.print_bill.field_names = ["ITEM", "Discount" ,"Price"]
        #self.print_bill.add_row(['CF1', '-', self.prices['CF1'] ])
    def billing(self):

        def BOGO(prices,farm_list_items):
            
            count_CF1 = farm_list_items.count('CF1')
            CF1_price = self.prices['CF1']
            if count_CF1%2 ==0:
                self.final_price += self.prices['CF1']*count_CF1/2
                print(price_table)
                #for i in range(0,count_CF1):
                #    print(i)
                    #bill.add_row(['CF1', '-', CF1_price ])
                return self.final_price
            else:
                self.final_price += (self.prices['CF1']*int((count_CF1/2))) + self.prices['CF1']
                return self.final_price
        def APPL(prices,farm_list_items):
            if 'OM1' not in farm_list_items:
                if farm_list_items.count('AP1') < 3 and 'OM1' not in farm_list_items:
                    self.final_price += (self.prices['AP1'] * farm_list_items.count('AP1'))
                    return self.final_price
                else: 
                    self.final_price += (4.5*farm_list_items.count('AP1'))
                    return self.final_price
            else:   
                self.final_price += 0.5*(self.prices['AP1'] * farm_list_items.count('AP1'))

        def CHMK(prices,farm_list_items):
            count_CH1 = farm_list_items.count('CH1')
            if 'MK1' in self.farm_list_items:
                self.farm_list_items.remove('MK1')
                self.final_price += (count_CH1 * self.prices['CH1'])
                return self.final_price

            else:
                self.final_price += count_CH1 * self.prices['CH1'] 
                return self.final_price

        def OM(prices,farm_list_items):
            count_OM1 = farm_list_items.count('OM1')
            self.final_price += self.prices['OM1'] * count_OM1
            return self.final_price

        def MK(prices,farm_list_item):
            count_MK1 = farm_list_item.count('MK1')
            self.final_price += self.prices['MK1'] * count_MK1
            return self.final_price

        if 'CF1' in self.farm_list_items :
            self.final_price = BOGO(self.prices, self.farm_list_items)
    
        if 'AP1' in self.farm_list_items:
            self.final_price = APPL(self.prices, self.farm_list_items)
        
        if 'CH1' in self.farm_list_items:
            self.final_price = CHMK(self.prices, self.farm_list_items)

        if 'OM1' in self.farm_list_items:
            self.final_price = OM(self.prices, self.farm_list_items)
        
        if 'MK1' in self.farm_list_items:
            self.final_price = MK(self.prices, self.farm_list_items)



items_list = (sys.argv)
#items_list = input("Enter list of Items (eg: 'CH1,AP1' ...   ) : ")
#items_list.split(',')        
bill_generator = Farmprice(items_list)
print(bill_generator.final_price)
