import numpy as np
m, n = 4, 6
shape = (n + 1, m + 1)

probs = np.zeros(shape)
# probs[0,0] = 1
# probs[0,1:] = 1/2 ** ys[0,1:]
# probs[1:,0] = 1/2 ** xs[1:,0]

# probs[:,0]
# probs[0,:]

def calc_prob(array, axis=0):
    if axis == 1:
        array = array.T

    array[1] += array[0] / 2

    #print("len(array): {}".format(len(array)))
    #print("len(array) == 2: {}".format(len(array) == 2))

    if len(array) > 2:
        calc_prob(array[-len(array) + 1:])

    return array

probs[0,0] = 1
calc_prob(probs[0,:])
calc_prob(probs[:,0])



def calc_prob_step(array):
    # print("array:\n{}".format(array))

    # np.where(array.shape[1] > 2, calc_prob_step(array[:,1:]), array)
    if array.shape[1] > 2:
        array[1,1] = array[0,1] / 2 + array[1,0] / 2
        calc_prob_step(array[:,1:])
    elif array.shape[1] == 2:
        array[1,1] = array[0,1] + array[1,0] / 2

    # elif array.shape[1] = 3:
    else:
        return array

def calc_prob_axis(array):
    print(array)
    if array.shape[0] > 2:
        calc_prob_step(array)
        calc_prob_axis(array[1:,:])

    if array.shape[0] == 2:
        array[1,1] = array[0,1] / 2 + array[1,0]
        if array.shape[1] > 3:
            calc_prob_axis(array[:,1:])
        else:
            array[-1,-1] = array[-2,-1] + array[-1,-2]
            return array

calc_prob_axis(probs)

print(probs)


#def calc_prob_array(array):
#    print("array:\n{}".format(array))
#    calc_prob(probs[1:,0:2], axis=1)
#    calc_prob(probs[0:2,1:], axis=0)
#    print("array.shape: {}".format(array.shape))
#
#    if np.min(array.shape) > 0:
#        calc_prob_array(array[1:,1:])
#    else:
#        return array

#calc_prob_array(probs)
#print(probs)
#
# calc_prob(probs[1:,0:2], axis=1)
# print("calc_prob(probs[1,:]):\n{}".format(probs))
#
# calc_prob(probs[0:2,1:], axis=0)
# print("calc_prob(probs[:2,1:]):\n{}".format(probs))
#
# calc_prob(probs[2:,1:3], axis=1)
# print("calc_prob(probs[2:,1:3], axis=1):\n{}".format(probs))
#
# calc_prob(probs[1:3,2:], axis=0)
# print("calc_prob(probs[1:3,2:]):\n{}".format(probs))
#
# calc_prob(probs[3:,2:4], axis=1)
# print("calc_prob(probs[3:,2:4], axis=1):\n{}".format(probs))
#
# print("calc_prob(probs[3:,2:4], axis=1):\n{}".format(probs))
# calc_prob(probs[2:4,3:], axis=0)


# calc_prob(probs[:,1])
# print("calc_prob(probs[:,1]):\n{}".format(probs))
#
#
# calc_prob(probs[:,2])
# print("calc_prob(probs[:,2]):\n{}".format(probs))


# calc_prob(probs[1:,1:])
# calc_prob(probs[2:,2:])

# def arr_prob(array):
#     print("array.shape: {}".format(array.shape))
#     array[1,1:] += array[0,1:] / 2
#     # array[1:,1] += array[1:,0] / 2
#
#     if np.min(array.shape) > 3:
#         arr_prob(array[-array.shape[0] + 1:, -array.shape[1] + 1:])
#     else:
#         print("array:\n{}".format(array))
#         np.argmin(array.shape)
#
#     return array
#
#
# arr_prob(probs)

# print("probs:\n{}".format(probs))
