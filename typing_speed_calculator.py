from time import *
import random as r

def mistake(strtest,inputtest):
    error = 0
    for i in range(len(strtest)):
        try:
            if(strtest[i] != inputtest[i] ):
                error = error + 1
        except:
            error = error+1
    return error

def speed_time(start_time,end_time,user_input):
        total_time = end_time - start_time
        time_r = round(total_time,2)
        speed = len(user_input)/ time_r
        return round(speed)

para = ["You’re braver than you believe, and stronger than you seem, and smarter than you think.", "In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact.","Optimism is a happiness magnet. If you stay positive good things and good people will be drawn to you.","Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same.",
"Once you replace negative thoughts with positive ones, you’ll start having positive results."]
choose_str = r.choice(para)
print()
print("-*-*-*-*-*-Typing Speed Calculator-*-*-*-*-*")
print()
print(choose_str)
print()
time1 = time()
testinput = input("Enter : ")
time2 = time()

print("Speed : ", speed_time(time1,time2,testinput),"w/sec")
print("Mistakes : ", mistake(choose_str,testinput))