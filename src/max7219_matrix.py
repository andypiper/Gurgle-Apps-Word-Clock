import machine

# DIN -> TX pico uses TX as MOSI on ESP32-C3 its GPIO 7
# CS -> CSn chip select any pin
# CLK -> SCK on ESP32-C3 it's GPIO 6 

class max7219_matrix:
    
    _NOOP = const(0)
    _DIGIT0 = const(1)
    _DECODEMODE = const(9)
    _INTENSITY = const(10)
    _SCANLIMIT = const(11)
    _SHUTDOWN = const(12)
    _DISPLAYTEST = const(15)
    
    
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.setup()
        self.char = [0x3c,0x56,0x93,0xdb,0xff,0xff,0xdd,0x89]
        self.brightness = 7
        self.set_brightness(self.brightness)
        
    def setup(self):
        self.write(_SHUTDOWN,0)
        self.write(_DISPLAYTEST,0)
        self.write(_SCANLIMIT,7)
        self.write(_DECODEMODE,0)
        self.write(_SHUTDOWN,1)

    def write(self, command, data):
        self.cs.value(0)
        self.spi.write(bytearray([command, data]))
        self.cs.value(1)

    def show_char(self, char):
        for i in range(8):
            self.write(i+1, char[i])
        return True
            
    
    def set_brightness(self, brightness):
        self.write(_INTENSITY, brightness)
                