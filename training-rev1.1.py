#!usr/bin/env python

print 'Welcome to the ABS Gym Universal App'
print 'Please enter your first name'
fname = raw_input()
print 'Please enter your surname'
sname = raw_input()
print 'Please enter M for Male or F for female'
gender = raw_input()

if gender == 'M' or gender == 'm':
   gender = 'M'
   print 'You have chosen Male'
elif gender == 'F' or gender == 'f':
   gender = 'F'
   print 'You have chosen Female'
else:
   print 'Invalid entry'

print 'Please enter your current age in years'
age = raw_input()
print 'Please enter KG for Kilograms or LBS for Pounds'
unit = raw_input()

if unit == 'KG' or unit == 'Kg' or unit == 'kg' or unit == 'kG':
   unit = 'KG'
   print 'You have chosen ' + unit   
elif unit == 'LBS' or unit == 'Lbs' or unit == 'LBs' or unit == 'lbs' or unit == 'lBS' or unit == 'lbS':
   unit = 'LBS'
   print 'You have chosen ' + unit
else:
   print 'Invalid entry'

print 'Please enter your current bodyweight in your chose units'
bweight = input()

print 'Please enter CM for Centimeters or IN for Inches'
unit_h = raw_input()

if unit_h == 'CM' or unit_h == 'Cm' or unit_h == 'cm' or unit_h == 'cM':
   unit_h = 'CM'
   print 'You have chosen ' + unit_h   
elif unit_h == 'IN' or unit_h == 'In' or unit_h == 'in' or unit_h == 'iN':
   unit_h = 'IN'
   print 'You have chosen ' + unit_h
else:
   print 'Invalid entry'

print 'Please enter your current height in your chose units'
height = input()

print ''
print 'Thank you ' + fname + ' ' + sname + '. Your current weight is ' + str(bweight) + unit + ', your height is ' + str(height) + unit_h + ' and you are ' + str(age) + ' years of age'
print ''
print 'Please choose one of the following options'
print '1. Nutrition and Macro Calculator'
print ''
print '2. 5/3/1 Calculator'
print ''
print '3. Exit Program'

choice = input()

while choice != 3:

   if choice == 1:
   
      print 'Please choose which of the following most accurately describes your daily physical activity'
      print ''
      print '1. Sedentary (little or no exercise, desk job)'
      print ''
      print '2. Lightly Active (light exercise/sports 3-5 days/week)'
      print ''
      print '3. Moderately Active (moderate exercise/sports 3-5 days/week)'
      print ''
      print '4. Very Active (hard exercise/sports 6-7 days per week)'
      print ''
      print '5. Extremely Active (very hard daily exercise/sports and physical job or 2/day training)'
      activity_lvl = input()
      if activity_lvl == 1:
         activity_lvl = 1.2
      elif activity_lvl == 2:
         activity_lvl = 1.35
      elif activity_lvl == 3:
         activity_lvl = 1.55
      elif activity_lvl == 4:
         activity_lvl = 1.75
      elif activity_lvl == 5:
         activity_lvl = 1.95

   
      if unit == 'KG' and gender == 'M' and unit_h == 'CM':
         bmr = (int(bweight) * 10) + (6.25 * int(height)) - (4.92 * int(age)) + 5
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)

      elif unit == 'KG' and gender == 'M' and unit_h == 'IN':
         bmr = (int(bweight) * 10) + (6.25 * (int(height) / 0.39)) - (4.92 * int(age)) + 5
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)
   
      elif unit == 'KG' and gender == 'F' and unit_h == 'CM':
         bmr = (int(bweight) * 10) + (6.25 * int(height)) - (4.92 * int(age)) - 161
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)

      elif unit == 'KG' and gender == 'F' and unit_h == 'IN':
         bmr = (int(bweight) * 10) + (6.25 * (int(height) / 0.39)) - (4.92 * int(age)) - 161
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)
   
      elif unit == 'LBS' and gender == 'M' and unit_h == 'CM':
         bmr = ((int(bweight) / 2.2) * 10) + (6.25 * int(height)) - (4.92 * int(age)) + 5
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)

      elif unit == 'LBS' and gender == 'M' and unit_h == 'IN':
         bmr = ((int(bweight) / 2.2) * 10) + (6.25 * (int(height) / 0.39)) - (4.92 * int(age)) + 5
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)

      elif unit == 'LBS' and gender == 'F' and unit_h == 'CM':
         bmr = ((int(bweight) / 2.2) * 10) + (6.25 * int(height)) - (4.92 * int(age)) - 161
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)

      elif unit == 'LBS' and gender == 'F' and unit_h == 'IN':
         bmr = ((int(bweight) / 2.2) * 10) + (6.25 * (int(height) / 0.39)) - (4.92 * int(age)) - 161
         print 'Your Basal Metabolic Rate (BMR) is ' + str(bmr * activity_lvl)



   elif choice == 2:

# 5/3/1 CALCULATOR GOES HERE

      print 'Please enter your most recent overhead press one rep max'
      maxpress = input()
      tmaxpress = maxpress * 9 / 10
      print ''
      print 'Please enter your most recent bench press one rep max'
      maxbench = input()
      tmaxbench = maxbench * 9 / 10
      print ''
      print 'Please enter your most recent deadlift one rep max'
      maxdead = input()
      tmaxdead = maxdead * 9 / 10
      print ''
      print 'Please enter your most recent squat one rep max'
      maxsquat = input()
      tmaxsquat = maxsquat * 9 / 10

      print 'Here are your new training maxes'
      print ''
      print 'Overhead Press training max = ' + str(tmaxpress)
      print 'Bench Press training max = ' + str(tmaxbench)
      print 'Deadlift training max = ' + str(tmaxdead)
      print 'Squat training max = ' + str(tmaxsquat)
      print ''
      print 'WEEK 1 OF 5/3/1 CYCLE'
      print ''
      print 'DAY 1 - Overhead Press'
      print 'Set 1 - 5 x ' + str(tmaxpress * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxpress * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxpress * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxpress * 65 / 100)
      print 'Set 5 - 5 x ' + str(tmaxpress * 75 / 100)
      print 'Set 6 - 5+ x ' + str(tmaxpress * 85 / 100)
      print ''
      print 'DAY 2 - Squat'
      print 'Set 1 - 5 x ' + str(tmaxsquat * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxsquat * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxsquat * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxsquat * 65 / 100)
      print 'Set 5 - 5 x ' + str(tmaxsquat * 75 / 100)
      print 'Set 6 - 5+ x ' + str(tmaxsquat * 85 / 100)
      print ''
      print 'DAY 3 - Bench Press'
      print 'Set 1 - 5 x ' + str(tmaxbench * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxbench * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxbench * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxbench * 65 / 100)
      print 'Set 5 - 5 x ' + str(tmaxbench * 75 / 100)
      print 'Set 6 - 5+ x ' + str(tmaxbench * 85 / 100)
      print ''
      print 'DAY 4 - Deadlift'
      print 'Set 1 - 5 x ' + str(tmaxdead * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxdead * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxdead * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxdead * 65 / 100)
      print 'Set 5 - 5 x ' + str(tmaxdead * 75 / 100)
      print 'Set 6 - 5+ x ' + str(tmaxdead * 85 / 100)
      print ''
      print 'WEEK 2 OF 5/3/1 CYCLE'
      print ''
      print 'DAY 1 - Overhead Press'
      print 'Set 1 - 5 x ' + str(tmaxpress * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxpress * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxpress * 6 / 10)
      print 'Set 4 - 3 x ' + str(tmaxpress * 7 / 10)
      print 'Set 5 - 3 x ' + str(tmaxpress * 8 / 10)
      print 'Set 6 - 3+ x ' + str(tmaxpress * 9 / 10)
      print ''
      print 'DAY 2 - Squat'
      print 'Set 1 - 3 x ' + str(tmaxsquat * 4 / 10)
      print 'Set 2 - 3 x ' + str(tmaxsquat * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxsquat * 6 / 10)
      print 'Set 4 - 3 x ' + str(tmaxsquat * 7 / 10)
      print 'Set 5 - 3 x ' + str(tmaxsquat * 8 / 10)
      print 'Set 6 - 3+ x ' + str(tmaxsquat * 9 / 10)
      print ''
      print 'DAY 3 - Bench Press'
      print 'Set 1 - 5 x ' + str(tmaxbench * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxbench * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxbench * 6 / 10)
      print 'Set 4 - 3 x ' + str(tmaxbench * 7 / 10)
      print 'Set 5 - 3 x ' + str(tmaxbench * 8 / 10)
      print 'Set 6 - 3+ x ' + str(tmaxbench * 9 / 10)
      print ''
      print 'DAY 4 - Deadlift'
      print 'Set 1 - 5 x ' + str(tmaxdead * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxdead * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxdead * 6 / 10)
      print 'Set 4 - 3 x ' + str(tmaxdead * 7 / 10)
      print 'Set 5 - 3 x ' + str(tmaxdead * 8 / 10)
      print 'Set 6 - 3+ x ' + str(tmaxdead * 9 / 10)
      print ''
      print 'WEEK 3 OF 5/3/1 CYCLE'
      print ''
      print 'DAY 1 - Overhead Press'
      print 'Set 1 - 5 x ' + str(tmaxpress * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxpress * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxpress * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxpress * 75 / 100)
      print 'Set 5 - 3 x ' + str(tmaxpress * 85 / 100)
      print 'Set 6 - 1+ x ' + str(tmaxpress * 95 / 100)
      print ''
      print 'DAY 2 - Squat'
      print 'Set 1 - 5 x ' + str(tmaxsquat * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxsquat * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxsquat * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxsquat * 75 / 100)
      print 'Set 5 - 3 x ' + str(tmaxsquat * 85 / 100)
      print 'Set 6 - 1+ x ' + str(tmaxsquat * 95 / 100)
      print ''
      print 'DAY 3 - Bench Press'
      print 'Set 1 - 5 x ' + str(tmaxbench * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxbench * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxbench * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxbench * 75 / 100)
      print 'Set 5 - 3 x ' + str(tmaxbench * 85 / 100)
      print 'Set 6 - 1+ x ' + str(tmaxbench * 95 / 100)
      print ''
      print 'DAY 4 - Deadlift'
      print 'Set 1 - 5 x ' + str(tmaxdead * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxdead * 5 / 10)
      print 'Set 3 - 3 x ' + str(tmaxdead * 6 / 10)
      print 'Set 4 - 5 x ' + str(tmaxdead * 75 / 100)
      print 'Set 5 - 3 x ' + str(tmaxdead * 85 / 100)
      print 'Set 6 - 1+ x ' + str(tmaxdead * 95 / 100)
      print ''
      print 'WEEK 4/DELOAD OF 5/3/1 CYCLE'
      print ''
      print 'DAY 1 - Overhead Press'
      print 'Set 1 - 5 x ' + str(tmaxpress * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxpress * 5 / 10)
      print 'Set 3 - 5 x ' + str(tmaxpress * 6 / 10)
      print ''
      print 'DAY 2 - Squat'
      print 'Set 1 - 5 x ' + str(tmaxsquat * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxsquat * 5 / 10)
      print 'Set 3 - 5 x ' + str(tmaxsquat * 6 / 10)
      print ''
      print 'DAY 3 - Bench Press'
      print 'Set 1 - 5 x ' + str(tmaxbench * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxbench * 5 / 10)
      print 'Set 3 - 5 x ' + str(tmaxbench * 6 / 10)
      print ''
      print 'DAY 4 - Deadlift'
      print 'Set 1 - 5 x ' + str(tmaxdead * 4 / 10)
      print 'Set 2 - 5 x ' + str(tmaxdead * 5 / 10)
      print 'Set 3 - 5 x ' + str(tmaxdead * 6 / 10)

   print ''
   print 'Please choose one of the following options'
   print '1. Nutrition and Macro Calculator'
   print ''
   print '2. 5/3/1 Calculator'
   print ''
   print '3. Exit Program'

   choice = input()
