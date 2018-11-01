fname=input('mbox.txt: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened',fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count=count + 1 
print('There were',count,'subject lines in',fname)


#2  meiginajums
'''
fhand=open('mbox.txt')
count=0
for line in fhand:
    count=count+18
    
print('Line Count:',count)
'''

#1 meiginajums
'''
xfile=open('mbox.txt')
for cheese in xfile:
    print(cheese)
''' 
