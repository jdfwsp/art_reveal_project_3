from paths import layers
from stats import statMap      
        
class Eagle:
    
    def __init__(self, code):
        self.code = code
        self.stats = {
            'Attack': statMap[code[0]],
            'Defend': statMap[code[1]],
            'Vitality': statMap[code[2]]
        }
        self.image = {
            'Head': layers['Head'][code[0]],
            'Body': layers['Body'][code[1]],
            'Hat': layers['Hat'][code[2]]
        }
        