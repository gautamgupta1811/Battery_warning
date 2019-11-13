
from battery_popup import *
import wmi
from getch.getch import getch

w = wmi.WMI()
for battery in w.query('select * from Win32_Battery'):
    print("Battery is : ", battery.EstimatedChargeRemaining, "%")

    a = battery.EstimatedChargeRemaining
    b = battery.BatteryStatus

    if b == 2:
        if a >= 95:
            balloon_tip("Battery Warning", "The device is charged. Please disconnect the charger.")
    else:
        if b == 1:
            if a <= 21:
                balloon_tip("Battery Warning", "The battery is running low. Please Connect the charger.")

print("Press any key to exit.")
getch()
