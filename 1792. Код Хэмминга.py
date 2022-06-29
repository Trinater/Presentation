a,b,c,d,e,f,g = map(int,input().split())

if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
    print (a, b, c, d, e, f, g)
else:
    a = (a+1)%2
    if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
        print (a, b, c, d, e, f, g)
    else:
        a = (a+1)%2
        b = (b+1)%2
        if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
            print (a, b, c, d, e, f, g)
        else:
            b = (b+1)%2
            c = (c+1)%2
            if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
                print (a, b, c, d, e, f, g)
            else:
                c = (c+1)%2
                d = (d+1)%2
                if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
                    print (a, b, c, d, e, f, g)
                else:
                    d = (d+1)%2
                    e = (e+1)%2
                    if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
                        print (a, b, c, d, e, f, g)
                    else:
                        e = (e+1)%2
                        f = (f+1)%2
                        if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
                            print (a, b, c, d, e, f, g)
                        else:
                            f = (f+1)%2
                            g = (g+1)%2
                            if (a+b+d)%2 == g and (a+c+d)%2 == f and (b+c+d)%2 == e:
                                print (a, b, c, d, e, f, g)
