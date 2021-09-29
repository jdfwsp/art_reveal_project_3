import os.path
from os import path
import itertools
import logging
import datetime
from datetime import datetime
import eagleXML
from eagleXML import opening, closing, backgrounds, bodies, options

logging.basicConfig(
    filename = 'generated.log',
    encoding = 'utf-8',
    level = logging.DEBUG
)


def writeImage(code):
    code = str.lower(code)
    name = f'SVGs/Output/{code}.svg'
    
    
    if path.exists(name):
        logging.error(f'---->\t\t🚨 Someone tried to generate {code} again on {datetime.now()} 🚨')
        print('error')
    
    else:
        image = {}
        image.update(background = backgrounds[code[0]])
        image.update(body = bodies[code[1]])
        image.update(option = options[code[2]])
        f = open(name, 'w')
        f.write(opening)
        for k in image:
            f.write(image[k])
        f.write(closing)
        f.close()

        logging.info(f'---->\t\t🦅 {code} generated on {datetime.now()} ✅')
        print('success')
        
def generateSet(options, length):
    res = [''.join(item) for item in itertools.product(options, repeat=length)]

    items = []

    for r in res:
        if r[1] != 'x':
            items.append(r)
    return items