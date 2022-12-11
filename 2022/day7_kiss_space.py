def directoryExists(directory):
    if directory not in directories.keys():
        return False
    return True

def upOneDirectory(directory):
    temp_dir_list =[]
    directories = directory.split('/')
    for level in directories:
        if level != '':
            temp_dir_list.append(level)
    temp_dir_list.pop()
    if temp_dir_list:
        return '/'+'/'.join(temp_dir_list)+'/'
    else:
        return '/'

def getChildSize(parent):
    sum = 0
    for directory in directories:
        if directory.startswith(parent):
            sum += directories[directory]
    return (sum)

with open('day7_input_file') as f:
    terminal_outputs = f.readlines()

pwd = '/'

directories =  { 
    '/'        : 0
}



for terminal_output in terminal_outputs:
    output_list = terminal_output.split()
    if (output_list[0] == '$') and (output_list[1] == 'cd'):
        dir_arg = output_list[2]
        if dir_arg == '/':
            pwd = '/'
            continue
        if dir_arg == '..': 
            if  pwd == '/':
                continue
            pwd = upOneDirectory(pwd)
            continue
        if not directoryExists(dir_arg):
            new_directory = pwd + dir_arg + '/'
            directories[new_directory] = 0
            pwd = new_directory
    elif output_list[0].isdigit():
        directories[pwd] += int(output_list[0])

smallDirSum     = 0 
spaceNeeded     = 30000000
diskSize        = 70000000
childSizeDict   = {}

for dir in directories:
    childSize           = getChildSize(dir)
    childSizeDict[dir]  = childSize
    if childSize <= 100000:
        smallDirSum += childSize
print (f'The sum of directories no more than 100,000 in size is {smallDirSum:,}')

#part 2
usedSpace       = sum(directories.values())
freeSpace       = diskSize - usedSpace
needToClear     = spaceNeeded - freeSpace
clearCandidates = []

for child in childSizeDict:
    if childSizeDict[child] >= needToClear:
        clearCandidates.append(childSizeDict[child])

print (f'IF you delete the folder with size {min(clearCandidates):,} you win')

