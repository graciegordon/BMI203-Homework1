#run 

import numpy as np
import matplotlib.pyplot as plt
from .sorts import quickSort, bubble
import sys
#for the 1000 quick sort the recursion must be set to 1500
sys.setrecursionlimit(1500)

x = np.random.rand(10)
print("Unsorted input: ", x)
b1,bc,ba=bubble(x)
q1,qc,qa=quickSort(x,0,len(x)-1,0,0)
print("Bubble sort output: ", b1, bc, ba)
print("Quick sort output: ", q1,qc,qa)

#test time complexity

def test_time(vectlen,num_iters):
    bconditional=[]
    bassignment=[]
    qconditional=[]
    qassignment=[]
    for i in range(0,num_iters):
        a=np.random.rand(vectlen)
        #test bubble
        bsort,bcon,bass=bubble(a)
        bconditional.append(bcon)
        bassignment.append(bass)

        #test quick
        qsort,qcon,qass=quickSort(a,0,vectlen-1,0,0)
        qconditional.append(qcon)
        qassignment.append(qass)
    
    return bconditional, bassignment, qconditional, qassignment

print('start testing')
bass=[]
bcon=[]
qass=[]
qcon=[]
#test vector length 100
onebcon,onebass,oneqcon,oneqass=test_time(100, 100)
bass.append(np.mean(onebass))
bcon.append(np.mean(onebcon))
qass.append(np.mean(oneqass))
qcon.append(np.mean(oneqcon))

#test vector length 200
twobcon,twobass,twoqcon,twoqass=test_time(200, 100)
bass.append(np.mean(twobass))
bcon.append(np.mean(twobcon))
qass.append(np.mean(twoqass))
qcon.append(np.mean(twoqcon))

#test vector length 300
threebcon,threebass,threeqcon,threeqass=test_time(300, 100)
bass.append(np.mean(threebass))
bcon.append(np.mean(threebcon))
qass.append(np.mean(threeqass))
qcon.append(np.mean(threeqcon))

#test vector length 400
fourbcon,fourbass,fourqcon,fourqass=test_time(400, 100)
bass.append(np.mean(fourbass))
bcon.append(np.mean(fourbcon))
qass.append(np.mean(fourqass))
qcon.append(np.mean(fourqcon))

#test vector length 500
fivebcon,fivebass,fiveqcon,fiveqass=test_time(500, 100)
bass.append(np.mean(fivebass))
bcon.append(np.mean(fivebcon))
qass.append(np.mean(fiveqass))
qcon.append(np.mean(fiveqcon))

print('halfway done')
#test vector length 600
sixbcon,sixbass,sixqcon,sixqass=test_time(600, 100)
bass.append(np.mean(sixbass))
bcon.append(np.mean(sixbcon))
qass.append(np.mean(sixqass))
qcon.append(np.mean(sixqcon))

#test vector length 700
sevenbcon,sevenbass,sevenqcon,sevenqass=test_time(700, 100)
bass.append(np.mean(sevenbass))
bcon.append(np.mean(sevenbcon))
qass.append(np.mean(sevenqass))
qcon.append(np.mean(sevenqcon))

#test vector length 800
eightbcon,eightbass,eightqcon,eightqass=test_time(800, 100)
bass.append(np.mean(eightbass))
bcon.append(np.mean(eightbcon))
qass.append(np.mean(eightqass))
qcon.append(np.mean(eightqcon))

#test vector length 900
ninebcon,ninebass,nineqcon,nineqass=test_time(900, 100)
bass.append(np.mean(ninebass))
bcon.append(np.mean(ninebcon))
qass.append(np.mean(nineqass))
qcon.append(np.mean(nineqcon))

#test vector length 1000
tenbcon,tenbass,tenqcon,tenqass=test_time(1000, 100)
bass.append(np.mean(tenbass))
bcon.append(np.mean(tenbcon))
qass.append(np.mean(tenqass))
qcon.append(np.mean(tenqcon))

print('plot')
#plot bubble assignments
x=np.arange(0,1000,100)

fig1=plt.figure(1)
fig1.suptitle("Number of Assignments in Sorts")
ax1 = fig1.add_subplot(111)
ax1.set_xlabel("number of elements in list")
ax1.set_ylabel("number of assignments")
ax1.plot(x, bass, 'r', label='bubble sort assignments')
ax1.plot(x, qass, 'b', label='quick sort assignments')
legend = ax1.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.show()

fig2=plt.figure(2)
fig2.suptitle("Number of Conditionals in Sorts")
ax2 = fig2.add_subplot(111)
ax2.set_xlabel("number of elements in list")
ax2.set_ylabel("number of assignments")
ax2.plot(x, bass, 'r', label='bubble sort conditionals')
ax2.plot(x, qass, 'b', label='quick sort conditionals')
legend = ax2.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.show()
print('bubble assignments: ', bass)
print('bubble conditionals: ', bcon)
print('quicksort assignments: ', qass)
print('quicksort  assignments: ', qcon)

