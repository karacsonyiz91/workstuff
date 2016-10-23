import sys

def Hello():
        print("Hello "+ sys.argv[1]+ "!")
        exit

def HelloWorld():
    print("Hello World!")
    exit

      if len(sys.argv) > 1 :
          Hello()
      else 
        HelloWorld()


