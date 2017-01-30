import binascii

#MainKey = raw_input("\nEnter the 64-bit key : ")

#MainKey = '123456789abcdef'

'''binkey = binascii.hexlify(MainKey)
print len(binkey) '''

binarray = [0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1]

p1 = [None] * 56
left = [None] * 28
right = [None] * 28

leftshift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


pc1 = [57,  49,    41,   33,    25,    17,    9,
               1,  58,    50,   42,    34,    26,   18,
              10,    2,    59 ,  51,    43,    35,   27,
              19,   11,     3,   60,    52,    44,   36,
              63,   55,    47,   39,    31,    23,   15,
               7,   62,    54,   46,    38,    30,   22,
              14,    6,    61,   53,    45,    37,   29,
              21,   13,     5,   28,    20,    12,    4]


p = 0
for i in range(0,56) :
    perm = pc1[i]
    p1[i] = binarray[perm-1]


for i in range(0,28) :
    left[i] = p1[i]
    right[i] = p1[i+28]


leftsub = 17*[28*[0]]
rightsub = 17*[28*[0]]

for i in range(0, 28) :
    leftsub[0][i] = left[i]
    rightsub[0][i] = right[i]


shifts=0
for i in range(1, 16) :
    shifts = leftshift[i-1]
    last = leftsub[i-1][shifts-1]
    for k in range(0, shifts) :
        for j in range(0, 28) :
            leftsub[i][j] = leftsub[i-1][j+shifts]

    leftsub[i][27] = last
    if shifts == 2 :
        seclast = leftsub[i-1][0]
        leftsub[i][26] = seclast

    shifts = shifts-1
