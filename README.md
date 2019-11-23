# Battery_warning

Not only a very low battery is bad, also you should not charge your device more than 95%  
This application will allow you to keep a check on your device's battery.  
A low battery message is common in your system settings, but to take care of your battery's health, it's a good practice to charge the device only upto 95%.  
So, this application runs in the background of your system and a message pop-ups to disconnect the charger when the charging completes upto 95%.  

## Files Information:  
  
1. Battery_check.py : This code is responsible to check the amount of battery available and hence, also checks whether a warning is needed or not based on two things: first, the battery percentage and second, the charging status of the device (the charger is connected or disconnected).  
2. battery_popup : In case a battery warning is raised by Battery_check.py, battery_popup creates a pop-up indicating the necessary action i.e either connect or disconnect the charger.    
3. main code.py : This file is used for creating .bat file based on user details and current working directory. It then pushes the .bat file to the startup folder so that the application runs itself as soon as your device starts.  
4. setup.py : It contains the code for freezing the application in executable format i.e to create a .exe file so that it can be used on any system.  
  
## :camera: ScreenShots:  
  
  
### ** If system is charged to 95%**  
  
![95%]()  
  
### ** If system is discharged to 20%**  
![20%]()  

## Technology Stack:    
  
  
Python 3  
Win32gui
