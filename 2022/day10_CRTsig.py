def prRed(skk): print("\033[91m{}\033[00m" .format(skk),end='')
 
 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end='')

def createSprite():
    global x
    sprite_pos = []
    for r in range(-1,2,1):
        sprite_pos.append(x+r) 
    return sprite_pos

def evaluateSignal():
    if cycle in key_cycles:
        signal_strengths.append(x * cycle)

def evaluateSprite(cycle, sprite_pos):
    displayColumn  = (cycle-1) % 40
    if displayColumn in sprite_pos:
        return 1
    else:
        return 0

def executeInstruction():
        global cycle
        global x
        global sprite_pos
        instruction_set = instruction.split()
        if instruction_set[0] == 'noop':
            cycle += 1
            evaluateSignal()
            crt_display.append(evaluateSprite(cycle, sprite_pos))
        else:
            cycle += 1
            evaluateSignal()
            crt_display.append(evaluateSprite(cycle, sprite_pos))
            cycle += 1
            evaluateSignal()
            crt_display.append(evaluateSprite(cycle, sprite_pos))
            x += int(instruction_set[1])
            sprite_pos = createSprite()


with open('day10_input_file') as f:
    instructions = f.readlines()

cycle               = 0
x                   = 1
key_cycles          = [20, 60, 100, 140, 180, 220]
signal_strengths    = []
sprite_pos          = createSprite()
crt_display         = []


for instruction in instructions:
    executeInstruction()


print (f'The sum of key signals is {sum(signal_strengths)}')

for r in range (0, len(crt_display), 1):
    if r % 40 == 0:
        print()
    if crt_display[r] == 0:
         prRed('O')
    else:
         prGreen('O')