import machine
import network
import time
import urllib
import urllib.urequest


url = "https://api.thingspeak.com/update"  
api_key = "API_KEY"
wireless= network.WLAN(network.STA_IF)
wireless.active(True)
wireless.connect("SSID","Password")
print(wireless.ifconfig())
print(wireless.isconnected())
import machine
import time
flow_freq = 0
l_hour = 0.0
ctime = 0
previous = 0
interval = 1000
calibration = 4.5
pulsecount = 0
pulse1s = 0
flowrate = 0.0
pin = 2
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

def pulseCallback(pin):
  global pulsecount
  pulsecount += 1

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=pulseCallback)

def timeInMillaseconds():
  timevalue =  time.ticks_ms()
  return timevalue


ctime = timeInMillaseconds()
loop_time = ctime

def calculate_flow():
  global ctime
  global loop_time
  global flow_freq
  global interval
  global pulsecount
  global previous
  global pulse1s
  global calibration
  ctime = timeInMillaseconds()
  if((ctime - previous)>interval):
    pulse1s = pulsecount
    pulsecount = 0
    flowrate = ((1000.0/(timeInMillaseconds() - previous))*pulse1s)/calibration
    previous = timeInMillaseconds()
    print(flowrate)
  distance = str(flowrate)
  f = urllib.urequest.urlopen("https://api.thingspeak.com/update?api_key=Y29U7WUUB0UTS8FZ&field1=" + distance)
 



while True:
  calculate_flow()
  time.sleep(3)
