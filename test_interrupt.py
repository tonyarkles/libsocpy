import libsocpy
import time

g = libsocpy.GPIO(20, libsocpy.LS_SHARED)

state = { 'last_one': time.time() }

def callback(gpio):
  global state
  if gpio.get_level() == 1:
    now = time.time()
    delta = now - state['last_one']
    state['last_one'] = now
    if delta > 0:
      print "Freq:", 1/delta
g.set_direction(libsocpy.INPUT)
g.set_edge(libsocpy.BOTH)
g.set_callback_interrupt(callback)

time.sleep(60)
