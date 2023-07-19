# @Author Oluwapelumi
#first method
import datetime
current_time = datetime.datetime.now()
print("Your current time is ", current_time, "\n")

#second method
print ("Current date and time : ")
print (current_time.strftime("%Y-%m-%d %H:%M:%S"))