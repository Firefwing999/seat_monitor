import time
# import gpiozero
import socket
from datetime import datetime
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

socket_num = 5005

while True:
  time.sleep(1)
  if GPIO.input(10) == GPIO.HIGH:
    s = socket.socket()
    print("socket created")
    host = '192.168.5.198'
    port = int(input())
    s.bind((host, port))

    s.listen(5)
    print("socket is listening")
    c, addr = s.accept()
    print ("Got connection from",addr)


    unseated_counter = 0
    while True:
      if(GPIO.input(10) == GPIO.HIGH):
        unseated_counter = 0
        now = str(datetime.now())[:-10] + " : " + str(datetime.today().weekday())
        sent_text = (now + ': 1')
        sent_text_temp = sent_text.encode('utf-8')
        print('sitting')
        c.send(sent_text_temp)
        time.sleep(3)

      elif(GPIO.input(10) == GPIO.LOW):
        time.sleep(3)
        if(GPIO.input(10) == GPIO.LOW):
          unseated_counter += 1
          now = str(datetime.now())[:-10] + " : " + str(datetime.today().weekday())
          sent_text = (now + ': 0')
          sent_text_temp = sent_text.encode('utf-8')
          print('standing')
          c.send(sent_text_temp)
        else:
          unseated_counter = 0
          now = str(datetime.now())[:-10] + " : " + str(datetime.today().weekday())
          sent_text = (now + ': 1')
          sent_text_temp = sent_text.encode('utf-8')
          print('sitting')
          c.send(sent_text_temp)

      time.sleep(57)




s.close()



