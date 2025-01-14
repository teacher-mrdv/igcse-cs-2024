def clearScreen():
    for i in range(24):
        print()

def drawHangman():
    print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___

    """)

def drawHangmanHead():
    print("""
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___

    """)

drawHangman()
clearScreen()
drawHangmanHead()
