'''
Meredith and Namitha
'''

class Rock:
    '''the characteristics and traits of rocks'''
    
    def __init__(self, rockType = 'unknown' , age=None):
        '''assumming user inputs either igneous, metamorphic or sedimentary'''
        self.type = rockType
        self.age = age

    def mayContainFossils(self):
        if self.type.casefold() == 'sedimentary':
            return True
        
        return False
    '''
    honestly don't know what I was tryna do, proabably talk about
    prehistoric periods, but eh delete it if you can't salvage it
    
    def period(self):
        if self.age
    '''
    def subType(self):
        if self.type.casefold() == 'igneous':
            print("Extrusive or Intrusive rocks")
                
        elif self.type.casefold() == 'sedimentary':
            print('Organic, Clastic, Chemical')
            
        elif self.type.casefold() == 'metamorphic':
            print('Foliated and Unfoliated')
        else:
            print('Unfortunately, there is no subtype found')

class Igneous(Rock):
    def __init__(self, age, subType):
        super.__init__('igneous', age)
        self.subTypes = ['Extrusive', 'Intrusive']

    
