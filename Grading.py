#-----------------Step:1 – Define Variable, set data type and create input function-------------------------

N = float (input ("Enter your mark: "))

#------------------Step:2 – Introduce IF…ELSEIF…. ELSE conditional statement-----------------------

if N>=80:
  print ("Congratulations! Your grade is: A+")
elif N<80 and N>=75:
  print (" Your grade is: A")
elif N<75 and N>=70:
  print (" Your grade is: A-")
elif N<70 and N>=65:
  print (" Your grade is: B+")
elif N<65 and N>=60:
  print (" Your grade is: B")
elif N<60 and N>=55:
  print (" Your grade is: B-")
elif N<55 and N>=50:
  print (" Your grade is: C+")
elif N<50 and N>=45:
  print (" Your grade is: C")
elif N<45 and N>=40:
  print (" Your grade is: D")
elif N<40:
  print ("Alas! Your grade is : F")
