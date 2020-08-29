
class Stock:

    def set_name(self,name):
        self.name = name

    def __init__(self,name='INIT'):
        self.currentPrice = 0
        self.direction = ''
        self.name = name
        


