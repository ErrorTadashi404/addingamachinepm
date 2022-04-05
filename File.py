while True:
    try:
        first_number = int(input("What is the first number you want to add?"))
        second_number = int(input("What is the seconde number you want to add"))
        sum = first_number + second_number
        print("the sum of your two number is", sum)
        break
    except: 
        print("You are so silly. That is not an integer...")

    

