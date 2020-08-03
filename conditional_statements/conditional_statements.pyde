size(600,400)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

'''
ball_is_red = 3 > 2
ball_is_blue = False
print(ball_is_red)
print(3 != 3)
'''

mark = 200

if mark < 0 or mark > 100:
    print('INVALID MARK')
elif mark >= 80:
    print('A')
elif mark >= 65:
    print('B')
elif mark >= 50:
    print('C')
elif mark >= 45 and mark < 50:
    print('RESUBMIT')
else:
    print('FAIL')
    
