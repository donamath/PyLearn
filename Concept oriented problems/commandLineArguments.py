import sys                                                                                          #Library to use command line arguments

if(len(sys.argv)!=3):                                                                               #Checking if 3 command line arguments are given i.e the file and two numbers to be added
    print("SYNTAX: python commandLineArguments.py [Argument1] [Argument2]")               
    sys.exit()                                                                                      #exiting the program if arguments are less than 3
else:
    c=int(sys.argv[1]) + int(sys.argv[2])                                                        
    print("The sum of the command line arguments are : "+str(c))                                    #printing the sum of given command line arguments
