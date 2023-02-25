import base64

import adafruit_amg88xx
import board
from bell.avr.mqtt.module import MQTTModule
from bell.avr.mqtt.payloads import AVRThermalReading
from bell.avr.utils.decorators import run_forever
from loguru import logger


class ThermalModule(MQTTModule):
    def __init__(self):
        super().__init__()

        logger.debug("Connecting to thermal camera...")
        i2c = board.I2C()
        self.amg = adafruit_amg88xx.AMG88XX(i2c)
        logger.success("Connected to thermal camera!")

    @run_forever(period=0.2)
    def thermal_reading(self) -> None:
        reading = bytearray(64)
        i = 0

        for row in self.amg.pixels:
            for pix in row:
                pixasint = round(pix)
                bpix = pixasint.to_bytes(1, "big")
                reading[i] = bpix[0]
                i += 1

        base64_encoded = base64.b64encode(reading)
        base64_string = base64_encoded.decode("utf-8")

        self.send_message("avr/thermal/reading", AVRThermalReading(data=base64_string))

    def run(self) -> None:
        self.run_non_blocking()
        self.thermal_reading()


if __name__ == "__main__":
    thermal = ThermalModule()
    thermal.run()
