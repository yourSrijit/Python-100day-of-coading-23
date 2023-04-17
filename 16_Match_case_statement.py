x =int(input("Enter the x "))
match x:
    case 0:
        print("This is ",x)
    case 1:
        print("This is ",x)
    case 3:
         print("This is ", x)

    # we can also ude if with default cases
    case _ if(x ==10):
        print("This is x=10")
    case _:
        print("Acts like default")