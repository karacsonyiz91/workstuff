for i in range(1, 101):
    if i**0.5 % 1:
        state='closed'
    else:
        state='open'
        print("These doors are open :{}".format(i))   