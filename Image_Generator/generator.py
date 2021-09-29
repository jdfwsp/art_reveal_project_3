import cairosvg
import datetime
from datetime import datetime
import eagleXML
from eagleXML import opening, closing, backgrounds, bodies, options
import itertools
import logging
import os.path
from os import path

logging.basicConfig(
    filename = 'generated.log',
    encoding = 'utf-8',
    level = logging.DEBUG
)


def writeImage(code):
    code = str.lower(code)
    name = f'SVGs/Output/{code}.svg'
    
    
    if path.exists(name):
        err = f'🚨 Someone tried to generate {code} again on {datetime.now()} 🚨'
        logging.error(f'---->\t{err}')
        print(err)
    
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
        
        cairosvg.svg2png(
        url=name,
        write_to=f'SVGs/Output/PNGs/{code}.png')
            
        success = f'🦅 {code} generated on {datetime.now()} ✅'
        logging.info(f'---->\t\t{success}')
        print(success)
        
def generateSet(options, length):
    res = [''.join(item) for item in itertools.product(options, repeat=length)]

    items = []

    for r in res:
        if r[1] != 'x' and r[0] != 'x':
            items.append(r)
    return items

import random

def generateRandomSet(options, length):
    res = [''.join(item) for item in itertools.product(options, repeat=length)]

    items = []

    for r in res:
        if r[1] != 'x' and r[0] != 'x':
            items.append(r)
    random.shuffle(items)
    return items