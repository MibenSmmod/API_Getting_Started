from colored import fg, bg, attr
from pyfiglet import Figlet

color1 = fg('purple_1b') + bg(0)
color2 = fg('purple_1b')
reset = attr('reset')
f = Figlet(font='standard', width=80)

print (color1 + ('                                                                   '))
print (color1 + (f.renderText(f'Welcome to ExtremeCloud APIs')) + reset)
print (color1 + ('   __   _        __   _        __   _        __   _'))
print (color1 + (' _(  )_( )_    _(  )_( )_    _(  )_( )_    _(  )_( )_'))
print (color1 + ('(_   _    _)  (_   _    _)  (_   _    _)  (_   _    _)'))
print (color1 + ('  (_) (__)      (_) (__)      (_) (__)      (_) (__)'))
