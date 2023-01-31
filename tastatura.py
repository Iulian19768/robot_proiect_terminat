USB_PORT = "/dev/ttyUSB0"  # Arduino Uno WiFi Rev2
# Imports
import serial
import getch
# Functions
def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  a - start motor")
   print("  l - off motor")
   print("  k - Turn off Arduino LED")
   print("  x - Exit program")
# Main
# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()
# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()
while True:
   command = getch.getch()

   if command == "w":  # turn on Arduino LED
          usb.write(b'1')  # send command to Arduino
          print("Arduino motor turned on.")
   elif command == "q":  # turn off Arduino LED
          usb.write(b'0')  # send command to Arduino
          print("Arduino motor turned off.")
   elif command == "s":  # turn off Arduino LED
          usb.write(b'2')  # send command to Arduino
          print("Arduino motor turned off.")
   elif command == "a":  # turn off Arduino LED
          usb.write(b'3')  # send command to Arduino
          print("Arduino motor turned off.")
   elif command == "d":  # turn off Arduino LED
          usb.write(b'4')  # send command to Arduino
          print("Arduino motor turned off.")
   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()