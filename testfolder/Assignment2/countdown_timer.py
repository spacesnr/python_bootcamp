#A countdown timer
import time

user_time = int(input("Enter time in seconds : "))

for i in reversed(range(0, user_time)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i/3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

"""
#creating same timer using a while loop
i = 0
while i < user_time:
    seconds = (user_time-1) % 60
    minutes = int(user_time / 60) % 60
    hours = int(user_time/3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    user_time -= 1

"""