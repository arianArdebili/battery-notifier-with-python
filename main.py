
# Hi guys just keep in your mind, it works on mackbook

import subprocess
import os
from notifypy import Notify

def notify(message, title):
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.send()

try:
    result = subprocess.run(['pmset', '-g', 'ps'], capture_output=True, text=True, check=True)
    output = result.stdout
    print(output)
except subprocess.CalledProcessError as e:
    print(f'The command failed with return code {e.returncode}')
    print(f'Error message: {e.stderr}')
    exit(1)

lines = output.splitlines()

battery_source = None
battery_percentage = None
charging_status = None
remaining = None

for line in lines:
    if 'Now drawing from' in line:
        battery_source = line.split("'")[1]
    if 'InternalBattery' in line:
        battery_percentage = line.split()[2]
        charging_status = line.split()[3]
        remaining = line.split()[4]

print(f'Battery source: {battery_source}')
print(f'Battery percentage: {battery_percentage}')
print(f'Charging status: {charging_status}')
print(f'Time remaining: {remaining}')

