try:
   inp = raw_input('Enter Hours: ')
   hours = float(inp)
   inp = raw_input('Enter Rate: ')
   rate = float(inp)
   if hours > 40:
       pay = hours * rate + (40 - hours) * rate * 1.5
   else:
       pay = hours * rate
   print 'Pay:', pay
except:
   print 'Error, please enter numeric input'
