
import datetime
import time
counter = 0
if 1:
                #multiple attempts to click guest
                while counter < 5:
                    counter+=1
                    print('while loop for friend')
                    try:
                        print('sending keys')

                        counter = 5

                    except:
                        print('cant find guest')
if 1:
                print('counter :',  counter)
                while counter  > 0:
                    counter-=1
                    try:
                        print('clicking guest')
                        x_guest_radio=' // *[ @ id = "players[2][guest]"]'
                        counter = 0
                    except:
                        print('cant find guest button')
print(counter)
ct = datetime.datetime.now().time()

print(ct<datetime.datetime.now().time())
print(ct>datetime.datetime.now().time())
print(ct,datetime.datetime.now().time())

    
print('break')
x = 0

while  x < 3:
       print(datetime.datetime.now().time())
       time.sleep(0.75)
       print(datetime.datetime.now().time())
  
       x+=1
x = time.time()
print(x)
print('h')
time.sleep(1)
y = time.time()
print(y)
x = datetime.datetime.now().time()

y = datetime.datetime.now().time()
print('time : ',y-x)

