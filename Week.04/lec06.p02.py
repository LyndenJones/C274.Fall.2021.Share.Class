def myassert( boo ):
    if not boo:
        print( "Assert failed: ", str(boo) )

def hypotenuse( a, o ):
    h = (float(a)**2 + float(o)**2) ** 0.5
    return h

def pythago( a=-1, o=-1, h=-1 ):
    # h**2 = a**2 + o**2
    if a == -1:
        myassert( o != -1 and h != -1 )
        a = ( h**2 - o**2 ) ** 0.5
        return(a)
    if o == -1:
        myassert( a != -1 and h != -1 )
        o = ( h**2 - a**2 ) ** 0.5
        return(o)
    if h == -1:
        myassert( a != -1 and o != -1 )
        h = (float(a)**2 + float(o)**2) ** 0.5
        return(h)


if __name__ == "__main__":
    print( hypotenuse( 3, 4 ) )
    print( hypotenuse( 8, 7 ) )
    print( pythago( a=3, o=4 ) )
    print( pythago( h=5, o=4 ) )
    print( pythago( a=3, h=5 ) )
    print( pythago( a=8, o=7 ) )
    myassert( abs( hypotenuse( 8, 7 ) - pythago( a=8, o=7 ) < 0.01 ) )
    print( "Test: ", ( abs( hypotenuse( 8, 7 ) - pythago( a=8, o=7 ) < 0.01 ) ) )
