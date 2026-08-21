# You are building a smart thermostat system.
# if the device status is active
#and if temperature > 35 = warn: "high temperature"
#else = temperature online
# if device is off= "device is offline"

device_status = "Active"
temperature = int(input("Enter value of temperature:"))

if device_status == "Active":
    if temperature > 35:
        print("Warning: high temperature")
    else:
        print("temperature normal")
else:
    print("device is offline")