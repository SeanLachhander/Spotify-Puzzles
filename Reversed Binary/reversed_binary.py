'''
@author: Sean Lachhander
@date: September 25, 2017
@story: Yi has moved to Sweden and now goes to school here. 
        The first years of schooling she got in China, and the curricula do not match completely in the two countries. 
        Yi likes mathematics, but now... The teacher explains the algorithm for subtraction on the board, and Yi is bored. 
        Maybe it is possible to perform the same calculations on the numbers corresponding to the reversed binary representations of the numbers on the board? 
        Yi dreams away and starts constructing a program that reverses the binary representation, in her mind. 
        As soon as the lecture ends, she will go home and write it on her computer.
@task: Your task will be to write a program for reversing numbers in binary. 
       For instance, the binary representation of 13 is 1101, and reversing it gives 1011, 
       which corresponds to number 11.
@description: This program will take the number in the first argument within the command line
              reverse the binary representation of that number, and then output the decimal number.
@URL: http://www.spotify.com/es/jobs/tech/reversed-binary/
'''

import sys
import time
if __name__ == "__main__":
    start_time = time.time()
    bin_str = bin(int(sys.argv[1]))[2:]
    print(int(bin_str[::-1], 2))
    print("This program took {} seconds to run.".format(time.time()-start_time))