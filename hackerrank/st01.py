#import pandas as pd
#
#i1 = "10"
#i2 = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
#
#size = int(i1)
#numbers = pd.Series(map(int, i2.split()))
#
#print(numbers.mean())
#print(numbers.median())
#print(numbers.mode()[0])


input1 = "10"
input2 = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"

i1 = int(input1)
i2 = list(map(int, input2.split()))


# Mean
def countmean(numlist):
    numsum = 0
    for num in numlist:
        numsum += num
    mean = numsum / len(numlist)
    return mean

mean = countmean(i2)

# Median
def countmedian(numlist):
    sortedlist = sorted(numlist)

    if len(sortedlist) % 2 == 1:
        mididx = int(len(sortedlist) // 2)
        median = sortedlist[mididx]
    else:
        majidx = int(len(numlist) / 2)
        median = countmean([sortedlist[majidx], sortedlist[majidx - 1]])

    return median

median = countmedian(i2)

# Mode
def findmode(numlist):
    numfreqs = {}
    numfreq = 0

    for num in numlist:
        #print("num: {}".format(num))

        numfreq = numlist.count(num)

        if numfreq in numfreqs.keys():
            if num in numfreqs[numfreq]:
                pass
            else:
                numfreqs[numfreq].append(num)
                #print("numfreqs[{}]: {}".format(numfreq, numfreqs[numfreq]))
        else:
            numfreqs[numfreq] = []
            numfreqs[numfreq].append(num)
            #print("numfreqs[{}]: {}".format(numfreq, numfreqs[numfreq]))

    topfreq = max(numfreqs.keys())
    mode = sorted(numfreqs[topfreq])[0]
    return mode

mode = findmode(i2)

print(mean)
print(median)
print(mode)
