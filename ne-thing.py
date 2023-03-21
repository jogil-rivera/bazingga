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
print(val)

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

print('this is a list of seeds: ', list)

print('i\'m picking one: ', random.choice(list))

x = random.sample(list, 2)

print('nvm, i want two, just incase (doesn\'t have to be the one i just chose): ', x)

def whatis(z):
    zed = 0
    random.seed(val)
    # y needs a new seed, val is already assigned to rr(sys.maxsize)
    y = random.uniform(1,1000)
    # b/c floats are the scary ones
    print('"a thick number": ', y)
    print('those two, from earlier, added together: ', x[0] + x[1])
    print('that summation, multiplied by, "a thick number": ', (x[0] + x[1]) * y)
    zed = int(((x[0]+ x[1]) * y))
    return int(zed)

zed = whatis(0)

trundle = str(zed)

print(trundle)

for i in trundle:
    sh = int(i)
    maokai = []
    maokai.append(trundle[sh])
    # 0 = 's'
    # 1 = 'r'
    # 2 ='t'
    # 3 = 'g'
    # 4 = 'a'
    # 5 = 'e'
    # 6 = 'y'
    # 7 = 'i'
    # 8 = 'c'
    # 9 = 'm'
print(sh, end= ",")
print(maokai)


ergo = {}

# def until(here):
#     for i in trundle:
#         for count in range(len(trundle)):
#             ergo[count] = i
#     print(ergo)
# #     else:
# #         print ('where to, from here?: ', ergo)
#
# until(1)