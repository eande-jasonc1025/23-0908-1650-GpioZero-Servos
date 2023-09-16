# 23-0908-1700 -.4 to .4 > weak range, not reliable

from gpiozero import Servo
from time import sleep
 
servoMotor_Left_GpioPinNum_Int=17
servoMotor_Right_GpioPinNum_Int=18

 
##23-0908 jwc y: servoMotor_Left_Object = Servo(servoMotor_Left_GpioPinNum_Int)
##23-0908 jwc y:  
##23-0908 jwc y: while True:
##23-0908 jwc y:     servoMotor_Left_Object.mid()
##23-0908 jwc y:     print("mid")
##23-0908 jwc y:     sleep(3.0)
##23-0908 jwc y:     servoMotor_Left_Object.min()
##23-0908 jwc y:     print("min")
##23-0908 jwc y:     sleep(3.0)
##23-0908 jwc y:     servoMotor_Left_Object.mid()
##23-0908 jwc y:     print("mid")
##23-0908 jwc y:     sleep(3.0)
##23-0908 jwc y:     servoMotor_Left_Object.max()
##23-0908 jwc y:     print("max")
##23-0908 jwc y:     sleep(3.0)


myCorrection=0
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servoMotor_Left_Object = Servo(servoMotor_Left_GpioPinNum_Int,min_pulse_width=minPW,max_pulse_width=maxPW)
servoMotor_Right_Object = Servo(servoMotor_Right_GpioPinNum_Int,min_pulse_width=minPW,max_pulse_width=maxPW)
 
while True:
 
  print("Set value range -1.0 to +1.0")
  for value in range(0,21):
    value2=(float(value)-10)/10
    servoMotor_Left_Object.value=value2
    servoMotor_Right_Object.value=value2
    print(value2)
    sleep(3)
 
  print("Set value range +1.0 to -1.0")
  for value in range(20,-1,-1):
    value2=(float(value)-10)/10
    servoMotor_Left_Object.value=value2
    servoMotor_Right_Object.value=value2
    print(value2)
    sleep(3)