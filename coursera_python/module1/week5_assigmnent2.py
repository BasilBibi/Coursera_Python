score = input("Enter Score: ")
s = float( score )

if s > 1.0:
    print("Score", s, "is out of range. Must be <= 1.0")
elif s >= 0.9:
    print( "A" )
elif s >= 0.8:
    print( "B" )
elif s >= 0.7:
    print( "C" )
elif s >= 0.6:
    print( "D" )
elif s < 0.6:
    print( "F" )