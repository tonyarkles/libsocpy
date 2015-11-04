
import ctypes

# details from the example program gpio_test.c
# constants GPIO_OUTPUT, GPIO_INPUT, LS_SHARED, OUTPUT, HIGH, LOW, RISING, FALLING, BOTH, NONE
# functions:
#  libsoc_set_debug
#  libsoc_gpio_request
#  libsoc_gpio_set_direction
#  libsoc_gpio_get_direction
#  libsoc_gpio_set_level
#  libsoc_gpio_get_level
#  libsoc_gpio_set_edge
#  libsoc_gpio_get_edge
#  libsoc_gpio_wait_interrupt
#  libsoc_gpio_callback_interrupt
#  libsoc_gpio_callback_interrupt_cancel
#  libsoc_gpio_free

# probably want to wrap the whole thing in an object...

DIRECTION_ERROR = -1
INPUT = 0
OUTPUT = 1

LEVEL_ERROR = -1
LOW = 0
HIGH = 1

EDGE_ERROR = -1
RISING = 0
FALLING = 1
NONE = 2
BOTH = 3

LS_SHARED = 0
LS_GREEDY = 1
LS_WEAK = 2

libsoc = ctypes.CDLL('libsoc.so')
libsoc.libsoc_gpio_request.restype = ctypes.c_void_p
libsoc_gpio_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

libsoc.libsoc_gpio_get_level.restype = ctypes.c_int

class GPIO(object):
  def __init__(self, pin, mode):
    self._gpio = libsoc.libsoc_gpio_request(pin, mode)

  def __del__(self):
    libsoc.libsoc_gpio_free(self._gpio)
    self._callback = None
    self._gpio = None

  def set_direction(self, direction):
    libsoc.libsoc_gpio_set_direction(self._gpio, direction)

  def set_level(self, level):
    libsoc.libsoc_gpio_set_level(self._gpio, level)

  def get_level(self):
    return libsoc.libsoc_gpio_get_level(self._gpio)

  def set_edge(self, edge):
    libsoc.libsoc_gpio_set_edge(self._gpio, edge)

  def set_callback_interrupt(self, callback):
    # callback will be called with the GPIO object passed as the only param
    def cbk(_):
      callback(self)
      return 0
    self._callback = libsoc_gpio_callback(cbk)
    libsoc.libsoc_gpio_callback_interrupt(self._gpio, self._callback, None)
    

  
