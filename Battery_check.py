from battery_popup import *
import wmi
w = wmi.WMI()
file = open("status.txt", "r+")
data = file.read()
data = int(data)
for battery in w.query('select * from Win32_Battery'):
    a = battery.EstimatedChargeRemaining
    b = battery.BatteryStatus
    if b == 2:
        if a > 94 and data == 0:
            balloon_tip("Battery Warning", "The device is charged. Please disconnect the charger.")
            data = 1
            file.write(str(data))
    elif b == 1:

        if a < 21 and data == 1:
            balloon_tip("Battery Warning", "The battery is running low. Please Connect the charger.")
            data = 0
            file.write(data)

