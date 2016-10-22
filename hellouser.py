import sys

def helloUser():
    if len(sys.argv) > 1 :
        print("Hello "+ sys.argv[1]+ "!")
        exit
    else:
        return True

def helloWorld():
    print("Hello World!")
    exit

if  helloUser():
    helloWorld()


