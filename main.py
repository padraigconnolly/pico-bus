import time

import busgraphics

CIRCLE_CENTER_X = 118
LINE_LENGTH = 148

display1 = busgraphics.Screen(CIRCLE_CENTER_X, LINE_LENGTH)

# Draw initial graphic
display1.draw()

# Wait 5 seconds
time.sleep(5)

# Add test times for bus routes (Future: fill with live times)
display1.update_time("20 mins", "400 mins")

# Wait 5 Seconds
time.sleep(5)

# Add test times for bus routes (Future: fill with live times)
display1.update_time("5 mins", "20 mins")
