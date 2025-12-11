import pprint
try:
    with open('input.txt', 'r') as file:
        print ("found file")
        manual = file.read().splitlines()
except FileNotFoundError:
        print ("file not found, using hardcoded ranges")
        manual = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".strip().splitlines()
        
class FactoryMachine:
    def __init__(self, lights, buttons, joltages ):
        self.lights = lights
        self.buttons = buttons
        self.joltages = joltages
        self.FoundSolution = False
        self.allButtonPressCombos = []

    def pressButton (self, button, new_lights):
        result = new_lights.copy()
        for button_pointer in button:
            if new_lights[button_pointer] == '#':
                result[button_pointer] = '.'
            elif new_lights[button_pointer] == '.':
                result[button_pointer] = '#'
        if '#' in result:
            return result
        else:
            self.FoundSolution = True
            return result
    
    def combineButtonResults (self, list_of_results):
        self.allButtonPressCombos.append(list_of_results)

for page in manual:
    button_schemes = []
    manual_dict = {}
    page_split = page.split(' ')
    for ps in page_split:
        if ps[0] == '[':
                lights = ps.replace('[', '')
                lights = lights.replace (']', '')
                lights = list(lights)
        elif ps[0] == '(':
                bs = ps.replace('(', '')
                bs = bs.replace (')', '')
                bs = bs.split(",")
                bs = [int(x) for x in bs]
                button_schemes.append(bs)
        else:
            joltages = ps

    new_machine = FactoryMachine(lights, button_schemes, joltages)

    push_one_button = []
    for button in new_machine.buttons:
        if new_machine.FoundSolution == False:
            push_one_button.append(new_machine.pressButton(button, new_machine.lights))
    new_machine.combineButtonResults(push_one_button)

    push_two_button = []
    for light_config in push_one_button:
        for button in new_machine.buttons:
             if new_machine.FoundSolution == False:
                push_two_button.append(new_machine.pressButton(button, light_config))
    new_machine.combineButtonResults(push_two_button)

    push_three_button = []
    if not new_machine.FoundSolution:
        for light_config in push_two_button:
            for button in new_machine.buttons:
                if new_machine.FoundSolution == False:
                    push_three_button.append(new_machine.pressButton(button, light_config))
        new_machine.combineButtonResults(push_three_button)
    if new_machine.FoundSolution:
        print (f'found solution in {len(new_machine.allButtonPressCombos)} button presses')


