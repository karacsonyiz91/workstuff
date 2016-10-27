todolist=['sajt', 'disznó']
n=input("Please specify a command [list,add,mark,archive]: ")

if (n=="list"):
    print("You saved the following to-do items: "+ "\n")
    for i in range(0,len(todolist)-1,1):
        print(str(i)+"x"+str(todolist[i]))
    #még nem jó init and str hiba

elif (n=="add"):
    add=input("Add an item: ")
    todolist.append(add)
    #new line és bevinni az új arrayt
    print("Item added.")
elif (n=="mark"):
    print("You saved the following to-do items:")
    for i in range(0,len(todolist)-1,1):
        print(str(i)+"x"+str(todolist[i]))
        add=input("Add an item: ")
    #kiirja tartalmazott dolgokat
    print("Which one you want to mark as completed: ")
    #choose var kell és beállitani ha egyiket beűti mit csináljon
    print("""varname""","is completed")
elif (n=="archive"):
    todolist=[]
    print("All completed tasks got deleted.")
else:
    print("Chose again, please")