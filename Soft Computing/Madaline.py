''' Simple python script to train sets using Madaline '''

__author__ = "Abhishek J M (jmabhishek4@gmail.com)"


class Madaline :
    def __init__(self) :
        pass


#Adaline training with AND logic
    def MadalXOR(self) :

        w11 = float(raw_input('Enter w11 :'))
        w12 = float(raw_input('Enter w12 :'))
        w21 = float(raw_input('Enter w21 :'))
        w22 = float(raw_input('Enter w22 :'))
        b1 = float(raw_input('Enter b1 :'))
        b2 = float(raw_input('Enter b2 :'))
        v1 = float(raw_input('Enter v1 :'))
        v2 = float(raw_input('Enter v2 :'))
        v3 = float(raw_input('Enter v3 :'))
        eta = float(raw_input('Enter learning rate :'))

        x1 = [1, 1, -1, -1]
        x2 = [1, -1, 1, -1]
        t = [-1, 1, 1, -1]

        iters = 2

        w11n=0
        w12n=0
        w21n=0
        w22n=0
        b1n=0
        b2n=0

        for i in range(0, iters) :
            print "\n Epoch "+str(i)
            for j in range(0, 4) :
                z1 = x1[j]*w11 + x2[j]*w21 + b1
                z2 = x1[j]*w12 + x2[j]*w22 + b2

                w11n = w11 + eta * x1[j] * (1 - z1)
                w12n = w12 + eta * x1[j] * (1 - z2)
                w21n = w21 + eta * x2[j] * (1 - z1)
                w22n = w22 + eta * x2[j] * (1 - z2)



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
    def MadalOR(self) :
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
    madal = Madaline()

    print "[+] Choose :"
    print "\t1. AND"
    print "\t2. OR"

    ch = int(raw_input())

    if ch == 1 :
        madal.MadalAND()

    if ch == 2 :
        madal.MadalOR()


if __name__ == '__main__' :
    main()
