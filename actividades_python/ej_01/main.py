from gpiozero import LED, Button
from signal import pause

led = LED(26)
button = Button(18)

button.when_pressed = led.on
button.when_released = led.off

pause()from gpiozero import LED, Button
from signal import pause

led = LED(26)
button = Button(18)

button.when_pressed = led.on
button.when_released = led.off

pause()
