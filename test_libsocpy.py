
import libsocpy

g = libsocpy.GPIO(20, libsocpy.LS_SHARED)

g.set_direction(libsocpy.OUTPUT)
while True:
  g.set_level(libsocpy.HIGH)
  g.set_level(libsocpy.LOW)
