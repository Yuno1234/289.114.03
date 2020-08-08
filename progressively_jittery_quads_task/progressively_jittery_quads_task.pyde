size(600, 600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(1)

x = 50
y = 50

n = 1

for i in range(64):
    
    fill('#FFFFFF')
    beginShape()
    vertex(x-random(n),y-random(n))
    vertex(x+45+random(n),y-random(n))
    vertex(x+45+random(n),y+45+random(n))
    vertex(x-random(n),y+45+random(n))
    endShape(CLOSE)
    
    fill('#FFFFFF')
    
    x += 65

    
    if x >= 550:
        x = 50
        y += 65
        n += 1
        
    fill('#FFFFFF')
