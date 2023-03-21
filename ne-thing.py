# import PySimpleGUI as sg
#
# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('first name'), sg.InputText()],
#             [sg.Text('last name'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Exit')]]
#
# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('ID:', '<', values[0], '>', ', ', '<', values[1], '>', sep="")
#     # print(event)
#     # print(values)
#
# window.close()

import random
import sys

val = random.randrange(sys.maxsize)
print('a seed: ', val)

list = []

for i in range(0,random.randrange(1,4)):
    list.append(val)
    break

val = random.randrange(sys.maxsize)

for i in range(0,random.randrange(1,4)):
    list.append(val)
    break

val = random.randrange(sys.maxsize)

for i in range(0,random.randrange(1,4)):
    list.append(val)
    break

print('this is a list of seeds: ', list, end = 2 * "\n")

print('i\'m picking one: ', random.choice(list))

x = random.sample(list, 2)

print('nvm, i want two, just incase (doesn\'t have to be the one i just chose): ', x, end = 2 * "\n")

def whatis(z):
    zed = 0
    random.seed(val)
    # y needs a new seed, val is already assigned to rr(sys.maxsize)
    y = random.uniform(1,1000)
    # b/c floats are the scary ones
    print('"a thick number": ', y, end = 2 * "\n")
    print('those two, from earlier, added together: ', sum(x))
    print('that summation, multiplied by, "a thick number": ', sum(x) * y)
    zed = int(sum(x) * y)
    return int(zed)

zed = whatis(0)

trundle = str(zed)
print('this is the seed, as a result of 3 seeds, summate 2 at random, multiply by a uniform, turned into a string: ',
      trundle)

maokai = {}
for i in trundle:
    sh = int(i)
    maokai.setdefault('_', [])
    maokai['_'].append(sh)

def nicki(hi):
    print('next up, recursions... here\'s my password: ', end = "")
    for j in maokai.values():
        for k in j:
            if k == 0:
                print('h', end = "")
            elif k == 1:
                print('e', end = "")
            elif k == 2:
                print('a', end = "")
            elif k == 3:
                print('t', end = "")
            elif k == 4:
                print('i', end = "")
            elif k == 5:
                print('n', end = "")
            elif k == 6:
                print('d', end = "")
            elif k == 7:
                print('x', end = "")
            elif k == 8:
                print('o', end = "")
            elif k == 9:
                print('s', end = "")
            else:
                None
nicki(1)