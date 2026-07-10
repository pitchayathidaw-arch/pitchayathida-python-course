print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

#input
seconds = int(input("Enter secound: "))

#process
hours = seconds // 3600
remian = seconds % 3600

minutes = remian // 60
seconds = remian % 60

#output
print()
print("Result")
print("Hour :, hours")
print("Minute:" , minutes)
print("Seconds :", seconds)

