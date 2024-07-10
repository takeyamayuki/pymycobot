from pymycobot.genre import Angle
from pymycobot.mycobot import MyCobot

mycobot = MyCobot("/dev/cu.usbmodemABC1234567892")
mycobot.send_angle(Angle.J2.value, 10, 50)
