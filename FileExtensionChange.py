import os

def fileTypeChange(dir_name,startType,endType):
    print(dir_name)
    print(startType)
    print(endType)
    folder = os.listdir(dir_name)
    for item in folder:
        if item.endswith(startType):
            newName = item[:-5] + endType
            os.rename(dir_name + item, dir_name + newName)

def fileRCU_Change(dir_name):
    print(dir_name)
    folder = os.listdir(dir_name)
    for item in folder:
        if item.startswith('RCU_'):
            newName = item[4:]
            os.rename(dir_name + item, dir_name + newName)


print('This programme will change all file extensions in a single folder')
dir_name = input('Please Copy/paste Folder location  ')
print(dir_name)
dir_name = dir_name + "\\"
print(dir_name)
startType = input('Please type the current file extension eg ".anon" / ".txt"')
print(startType)
endType = input('Please type the wanted output extension eg ".anon" / ".txt" (Without the quotation marks) ')
print(endType)
fileTypeChange(dir_name,startType,endType)
RCUCHECK = input('Would you like RCU_ removing from the start of all outputs? Y / N ')

if RCUCHECK == 'Y':
    fileRCU_Change(dir_name)
else:
    pass
