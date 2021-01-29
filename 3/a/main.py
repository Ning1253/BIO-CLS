display = []
next = ord("A")

def add():
    global next
    global display
    display.append(chr(next))
    next += 1

def swap():
    global display
    display[0], display[1] = display[1], display[0]

def rotate():
    global display
    display = display[1:] + [display[0]]


add()
add()
swap()
rotate()
add()
swap()
rotate()
add()
add()

print(display)