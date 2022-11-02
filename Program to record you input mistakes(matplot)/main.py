import matplotlib.pyplot as plt
import time as t
times=[]
word=[]
mistakes=0
print("This program will help you faster")
input("please enter to continue")
word=input("enter your word")
check=[]

while len(times)<5:
    start = t.time()
    checks=input("Type the word:").lower()
    check.append(checks)
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    if(checks!=word[0]):
        mistakes += 1
print("You made " +str(mistakes)+ " mistakes(s).")
print("Now lets see your evolution")
t.sleep(3)
x=[1,2,3,4,5]
y=times
plt.plot(x,y)
em=["1", "2", "3", "4" ,"5"]
plt.xticks(x,em)
plt.ylabel('Time in seconds')
plt.xlabel('attempts')
plt.title('Your record')
plt.show()