size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

'''
circle(width/2, height/2, 30)
circle(width/2, height/2, 60)
circle(width/2, height/2, 90)

i = 0

while i < 24:
    circle(width/2, height/2, 30 * i)
    #i = i + 1
    i += 1
'''

for i in range(10, 24):
    circle(width/2, height/2, 30 * i)
