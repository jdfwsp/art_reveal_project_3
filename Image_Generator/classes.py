from paths import layers
from stats import statMap      
   
class Stats:
    
    def __init__(self, code):
        self.attack = statMap[code[0]]
        self.defent = statMap[code[1]]
        self.vitality = statMap[code[2]]
        
class Eagle:
    
    def __init__(self, code):
        self.code = code
        self.stats = Stats(code)
        self.image = {
            'Head': layers['Head'][code[0]],
            'Body': layers['Body'][code[1]],
            'Hat': layers['Hat'][code[2]]
        }
        