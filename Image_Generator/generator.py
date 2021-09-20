import classes
from classes import bodies, heads, hats, opening, closing

def getImage(code):
    image = {}
    image.update(body = bodies[code[0]])
    image.update(head = heads[code[1]])
    image.update(hat = hats[code[2]])
    f = open(f'SVGs/{code}.svg', 'w')
    f.write(opening)
    for k in image:
        f.write(image[k])
    
    f.write(closing)
    f.close()