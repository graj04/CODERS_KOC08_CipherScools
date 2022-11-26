dd,mm,yyyy=input('Enter Starting Date: ').split('/')
dd2,mm2,yyyy2=input('Enter Ending date: ').split('/')
print('Leap years are:')
for i in range(int(yyyy),int(yyyy2)+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i,end=' ')
print('\n')
print('Non leap years are:')
for j in range(int(yyyy),int(yyyy2)+1):
   if j%4!=0 or j%100==0 and j%400!=0:
       print(j,end=' ')