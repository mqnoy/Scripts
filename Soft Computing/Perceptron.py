'''Simple python script to get the final weights from Perceptron Rule.'''

__author__ = "Abhishek J M (jmabhishek4@gmail.com)"

import argparse


class Perceptron :

    def __init__(self) :
        pass

    def perceptAND(self) :

        print "\n"
        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        x3 = [1, 1, 1, 1]
        y = [1, -1, -1, -1]

        w1=0
        w2=0
        w3=0
        b=0
        eta=0.2

        w1n=0
        w2n=0
        w3n=0
        bn=0

        for i in range(0,4) :


        '''
        if (w1n != w1 or w2n != w2 or bn != b ) :
            print "weights not same. "

        if (w1n == w1 and w2n == w2 and bn == b ) :
        '''

            yin = x1[i]*w1 + x2[i]*w2 + b
            if y[i] != yin :
                w1n = w1+eta*x1[i]*y[i]
                w2n = w2+eta*x2[i]*y[i]
                bn = b+eta*y[i]
                print "[+] Weights and bias after iteration "+str(i)+" :"
                print "W1 :" +str(w1n)
                print "W2 :" +str(w2n)
                print "b  :" +str(bn)

                w1 = w1n
                w2 = w2n
                b = bn

            else :
                w1n = w1
                w2n = w2
                bn = b

        print "\n"
        print "Final Weights :"
        print w1, w2, b


    def perceptOR(self) :

        print "\n"
        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        x3 = [1, 1, 1, 1]
        y = [1, 1, 1, -1]

        w1=0
        w2=0
        w3=0
        b=0
        eta=0.2
        w1n=0
        w2n=0
        w3n=0
        bn=0

        for i in range(0,4) :
            yin = x1[i]*w1 + x2[i]*w2 + b
            if y[i] != yin :
                w1n = w1+eta*x1[i]*y[i]
                w2n = w2+eta*x2[i]*y[i]
                bn = b+eta*y[i]
                print "[+] Weights and bias after iteration "+str(i)+" :"
                print "W1 :" +str(w1n)
                print "W2 :" +str(w2n)
                print "b  :" +str(bn)

                w1 = w1n
                w2 = w2n
                b = bn

            else :
                w1n = w1
                w2n = w2
                bn = b

        print "\n"
        print "Final Weights :"
        print w1, w2, b



def main() :
    percept = Perceptron()

    print "[+] Choose :"
    print "\t1. AND"
    print "\t2. OR"

    ch = int(raw_input())

    if ch == 1 :
        percept.perceptAND()

    if ch == 2 :
        percept.perceptOR()



if __name__ == '__main__' :
    main()
