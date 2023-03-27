from datetime import datetime

current_dateTime = datetime.now()
print('The date and time are', current_dateTime)

weekno = datetime.today().weekday()
 
if weekno < 5:
    print("It is a Weekday")
else:
    print("It is a Weekend")
    
if weekno < 5:
    print("The store is closed")
else:
    print('The store is open')
