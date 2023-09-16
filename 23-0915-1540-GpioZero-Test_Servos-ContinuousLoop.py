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
 
###jwc o  print("Set value range -1.0 to +1.0")
###jwc o  for value in range(0,21):
###jwc o    value2=(float(value)-10)/10
###jwc o    servoMotor_Left_Object.value=value2
###jwc o    servoMotor_Right_Object.value=value2
###jwc o    print(value2)
###jwc o    sleep(3)
 
###jwc o   print("Set value range +1.0 to -1.0")
###jwc o   for value in range(20,-1,-1):
###jwc o     value2=(float(value)-10)/10
###jwc o     servoMotor_Left_Object.value=value2
###jwc o     servoMotor_Right_Object.value=value2
###jwc o     print(value2)
###jwc o     sleep(3)
      
###jwc y   duration_Sec_Int = 3.5 
    ###jwc n duration_Sec_Int = 1.1  
    ##jwc n duration_Sec_Int = 1.1 
    duration_Sec_Int = 0.25 
    duration_Rest_Sec_Int = 3 
    ###jwc n range_Max = 5
    range_Max = 3

    print("Continuous Loop for x Seconds and Reverse Direction")

    ###jwc yn for i in range(0,range_Max):
    ###jwc y value = 0.2
    value = -0.5
    servoMotor_Left_Object.value=value
    servoMotor_Right_Object.value=value
    print(value)
    sleep(duration_Sec_Int)
    servoMotor_Left_Object.value=0
    servoMotor_Right_Object.value=0
    sleep(duration_Rest_Sec_Int)

  
    ###jwc yn for i in range(0,range_Max):
    ###jwc yn     value = -0.5
    ###jwc yn     servoMotor_Left_Object.value=value
    ###jwc yn     servoMotor_Right_Object.value=value
    ###jwc yn     print(value)
    ###jwc yn     sleep(duration_Sec_Int)  
    ###jwc yn     servoMotor_Left_Object.value=0
    ###jwc yn     servoMotor_Right_Object.value=0
    ###jwc yn     sleep(duration_Rest_Sec_Int)

