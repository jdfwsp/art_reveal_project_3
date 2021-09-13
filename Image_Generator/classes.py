from paths import layers
from stats import statMap      
   
class Stats:
    
    def __init__(self, code):
        self.attack = statMap[code[0]]
        self.defend = statMap[code[1]]
        self.vitality = statMap[code[2]]
        
class Image:
    
    def __init__(self, code):
        self.head = layers['Head'][code[0]]
        self.body = layers['Body'][code[1]]
        self.hat = layers['Hat'][code[2]]
        
class Eagle:
    
    def __init__(self, code):
        self.code = code
        self.stats = Stats(code)
        self.image = Image(code)
        
        