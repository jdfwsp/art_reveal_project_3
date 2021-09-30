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
    name = f'Output/SVGs/{code}.svg'
    
    
    if path.exists(name):
        err = f'---->\t🚨 Someone tried to generate {code} again on {datetime.now()} 🚨'
        logging.error(err)
        print(f'🚨 {code} already exists 🚨')
    
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
        write_to=f'Output/PNGs/{code}.png')
            
        success = f'---->\t🦅 {code} generated on {datetime.now()} ✅'
        logging.info(success)
        print(f'🦅 {code} successfully generated ✅')
        
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
