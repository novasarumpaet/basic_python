x = int(input("Enter the coordinat X : "))
y = int(input("Enter the coordinat Y : "))

if (x>0):
    if (y>0):
        print("point is in quadrant I")
    elif (y<0):
        print("point is in quadrant IV")
    else:
        print("point is in x coordinat")
elif (x<0):
    if (y>0):
        print("point is in quadrant II")
    elif (y<0):
        print("point is in quadrant III")
    else:
        print("point is in x coordinat")
else:
    if (y==0):
        print("point is in (0,0)")
    else:
        print("point is in y coordinat")