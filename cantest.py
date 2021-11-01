import can
import time

bus = can.interface.Bus(bustype='slcan', channel='COM3', bitrate=500000)
notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])

t_end = time.time() + 60 * 1

while time.time() < t_end:
    if ( int(time.time())%10 == 0): 
        print(f"time is {int(time.time())}")




