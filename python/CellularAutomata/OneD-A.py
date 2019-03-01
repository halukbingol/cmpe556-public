# 1-D Cellular Automata
# bingol 2019

def localRule(states, present, next):
    #  rule 195
    # print(states, present, next)
    size = len(states[0])
    for i in range(size - 1):
        #  exor
        # states[next][i] = states[present][i] + states[present][i + 1]
        # if states[next][i] > 1:
        #     states[next][i] = 0
        states[next][i] = states[present][i] ^ states[present][i + 1]
    # the right-most-one
    states[next][size - 1] = 0


def rule160(states, present, next):
    i = 0


P_ZERO = "."
P_ONE = "*"


def printNice(s):
    if s == 0:
        print(P_ZERO, end="")
    else:
        print(P_ONE, end="")


# main
TIME = 50
SIZE = 20
LOC_ZERO = SIZE - 2
QUIESCENT = 0

#
indexPresent = 0
indexNext = 1

# init
# states = [[0 for x in range(SIZE)] for y in range(2)]
states = [[QUIESCENT] * SIZE for i in range(2)]
states[indexPresent][LOC_ZERO] = 1
# print(states)


# time loop
for t in range(TIME):
    print(t, end=":\t")
    for s in states[indexPresent]:
        printNice(s)
        # print(s, end=" ")
    print("\\\\")

    # apply local rule
    localRule(states, indexPresent, indexNext)

    # switch: present and next
    indexPresent, indexNext = indexNext, indexPresent
    # tmp = indexPresent
    # indexPresent = indexNext
    # indexNext = tmp
    # print('a:',indexPresent,indexNext)

#  end
