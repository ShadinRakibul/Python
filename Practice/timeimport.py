import time
from datetime import datetime
timestamp = time.strftime("%d-%m-%y", time.localtime())
timestamp1 = time.strftime("%H:%M:%S", time.localtime())
time_12hour = time.strftime("%I:%M:%S %p", time.localtime())
print(f"Today: {timestamp}")
print(f"Current time:{time_12hour}")
print(f"International time:{timestamp1}")

# This code imports the time module, gets the current local time,
# formats it as a string, and prints it in the format "YYYY-MM-DD HH:MM:SS".
# It can be used to log the time of execution or for timestamping events.
# The formatted timestamp can be useful for tracking when certain actions were performed.
# The output will show the current date and time in a human-readable format.
# Example output: "Current timestamp: 2023-10-01 12:34:56"
# This code is useful for logging purposes in applications where time tracking is important.
# The code is simple and effective for generating a timestamp.
