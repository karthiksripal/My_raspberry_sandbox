import datetime
import time
import os

def chimebell( iterations ) :
    initvar = 0
    iterations_init = int( iterations )
    #print ( iterations )   
    while ( initvar > iterations_init ):
        print ( initvar )
        initvar = initvar + 1
        return;

def main():
    sysday = time.strftime("%a")
    syshour = time.strftime("%H")

    chimebell( syshour )

main()

    
