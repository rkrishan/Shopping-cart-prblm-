# -*- coding: utf-8 -*-
"""
Spyder Editor
@Ramkrishan Sharma
This is a cart prblm script file.
"""
RULES = {
  'A': {'price': 50, 'discount_threshold': 3, 'discount_price': 130},
  'B': {'price': 30, 'discount_threshold': 2, 'discount_price': 45},
  'C': {'price': 20},
  'D': {'price': 15}
}

class Checkout:
    current_price = 0
    rules         = None
    item_count    = {}
    
    def __init__(self,rules):
        self.rules = rules
        
        for key,value in rules.items():
            self.item_count[key] = 0    
     
    def scan(self,item):
        price = self._extract_price(item)
        
        if price:
            self.current_price +=price
            self.item_count[item]+=1
            self._apply_discount(item)
            
        
    def total(self):
        return self.current_price
        
    
    def _extract_price(self,item):
        item = self.rules.get(item)
        
        if item:
            return item.get('price')
        return None
    
    def _apply_discount(self,item):
       item_key = item
       count = self.item_count.get(item)
       item = self.rules.get(item)
       discount_threshold = item.get('discount_threshold')
       
       if discount_threshold and (count==discount_threshold):
           print("dictonary value now ",self.item_count)
           item_price = item.get('price')
           discount_price = item.get('discount_price')
           discount = (discount_threshold*item_price) - discount_price
           self.current_price-=discount    
           self.item_count[item_key] = 0  
       return   
   
def calc_price(items):
    co = Checkout(RULES)
    for item in items:
        co.scan(item)
    return co.total()
     
   
    """
    comment this portion for running test cases
    
    
if __name__ == "__main__":
    total = calc_price('AAABBB')
    print("total price",total)
"""    
    
        
           
    
    
    
        
