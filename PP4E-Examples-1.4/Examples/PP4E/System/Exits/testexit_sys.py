def later():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')

    #Escrito por Mat
    #try:
    #    sys.exit(42)
    #except SystemExit:
    #    print('Now it is reached')
    #print('Never reached')

if __name__ == '__main__': later() 
    #try:
    #    later()
    #except SystemExit:
    #    print('There was a system exit')
