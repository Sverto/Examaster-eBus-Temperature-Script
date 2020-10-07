import sys
import subprocess

ebus_target = "15" # Examaster
ebus_primary_command = "B5" # Bulex command
ebus_secundary_command = "09" # Get or set device configuration
ebus_read_command = "0D"
ebus_write_command = "0E"

# Examaster registers to write to
register_temp_setpoint_downstairs = "9700" 
register_temp_setpoint_upstairs = "FE00"


# method to convert value to EBUS 'D2C', returns 4 digit hex string (2 bytes)
def ConvertFloatToD2XHex(floatValue):
    hex = "%0.4X" % (floatValue * 16)
    return hex[2:4] + hex[0:2]


# process args
if len(sys.argv) < 3:
    print("Missing arguments")
    print(" 1: upstairs|downstairs")
    print(" 2: value devisible by 0.5, minimum 5.0 and maximum 30.0")
    sys.exit(1)


# process location arg
if sys.argv[1] == "upstairs":
    ebus_register = register_temp_setpoint_upstairs
elif sys.argv[1] == "downstairs":
    ebus_register = register_temp_setpoint_downstairs
else:
    print("Unknown second argument. Options are 'upstairs', 'downstairs'")
    sys.exit(2)


# process temperature arg 
value = float(sys.argv[2])

if value % 0.50 != 0 or value < 5.0 or value > 30.0:
    print("Value must be devisible by 0.5, minimum 5.0 and maximum 30.0")
    sys.exit(3)

ebus_value = ConvertFloatToD2XHex(value)


# SEND WRITE COMMAND
data = ebus_write_command + ebus_register + ebus_value
command = ebus_target + ebus_primary_command + ebus_secundary_command + ("%0.2X" % (len(data)/2)) + data

print("Sending command: " + command)
result = subprocess.check_output("/usr/bin/ebusctl hex %s" % command, shell=True).decode("utf-8").rstrip()
if result == "00":
    print("Command succeeded")
else:
    print("Command failed: " + result)
    sys.exit(4)