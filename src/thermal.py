import adafruit_amg88xx
import board
import numpy as np
from bell.avr.mqtt.module import MQTTModule
from bell.avr.mqtt.payloads import AVRThermalReading
from bell.avr.utils.decorators import run_forever
from bell.avr.utils.images import serialize_image
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
        image_data = serialize_image(np.array(self.amg.pixels))
        self.send_message("avr/thermal/reading", AVRThermalReading(**image_data))

    def run(self) -> None:
        self.run_non_blocking()
        self.thermal_reading()


if __name__ == "__main__":
    thermal = ThermalModule()
    thermal.run()
