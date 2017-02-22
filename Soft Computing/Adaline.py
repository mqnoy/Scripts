''' Simple python script to train sets using Adaline '''

__author__ = "Abhishek J M (jmabhishek4@gmail.com)"


class Adaline :
    def __init__(self) :
        pass


#Adaline training with AND logic
    def AdalAND(self) :

        w1 = float(raw_input('Enter w1 :'))
        w2 = float(raw_input('Enter w2 :'))
        b = float(raw_input('Enter bias :'))
        eta = float(raw_input('Enter learning rate :'))

        iters = int(raw_input('Enter the number of iterations :'))

        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        y = [1, -1, -1, -1]


        w1n=0
        w2n=0
        w3n=0
        bn=0

        for i in range(0, iters) :
            print "\n Epoch "+str(i)
            for j in range(0, 4) :
                yin = x1[j]*w1 + x2[j]*w2 + b

                w1n = w1 + eta * x1[j] * (y[j] - yin)
                w2n = w2 + eta * x2[j] * (y[j] - yin)
                bn = b + eta * (y[j] - yin)

                print "\t[+] Weights and bias after iteration "+str(j)+" :"
                print "\n\t\tW1 :" +str(w1n)
                print "\t\tW2 :" +str(w2n)
                print "\t\tb  :" +str(bn)

                w1 = w1n
                w2 = w2n
                b = bn

            print "\n\n[+] After epoch " +str(i)+ " :"
            print w1, w2, b

        print "\n"
        print "Final Weights :"
        print w1, w2, b



#Adaline training with OR logic.
    def AdalOR(self) :
        w1 = float(raw_input('Enter w1 :'))
        w2 = float(raw_input('Enter w2 :'))
        b = float(raw_input('Enter bias :'))
        eta = float(raw_input('Enter learning rate :'))

        iters = int(raw_input('Enter the number of iterations :'))

        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        y = [1, 1, 1, 1]


        w1n=0
        w2n=0
        w3n=0
        bn=0

        for i in range(0, iters) :
            print "\n Epoch "+str(i)
            for j in range(0, 4) :
                yin = x1[j]*w1 + x2[j]*w2 + b

                w1n = w1 + eta * x1[j] * (y[j] - yin)
                w2n = w2 + eta * x2[j] * (y[j] - yin)
                bn = b + eta * (y[j] - yin)

                print "\t[+] Weights and bias after iteration "+str(j)+" :"
                print "\n\t\tW1 :" +str(w1n)
                print "\t\tW2 :" +str(w2n)
                print "\t\tb  :" +str(bn)

                w1 = w1n
                w2 = w2n
                b = bn

            print "\n\n[+] After epoch " +str(i)+ " :"
            print w1, w2, b

        print "\n"
        print "Final Weights :"
        print w1, w2, b



def main() :
    adal = Adaline()

    print "[+] Choose :"
    print "\t1. AND"
    print "\t2. OR"

    ch = int(raw_input())

    if ch == 1 :
        adal.AdalAND()

    if ch == 2 :
        adal.AdalOR()


if __name__ == '__main__' :
    main()
