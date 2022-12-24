# AVR-VMC-Thermal-Module

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Thermal Module](https://github.com/bellflight/AVR-VMC-Thermal-Module/actions/workflows/build.yml/badge.svg)](https://github.com/bellflight/AVR-VMC-Thermal-Module/actions/workflows/build.yml)

The Thermal module is responsible for capturing thermal images from the thermal
camera and publishing them over MQTT.

## Developer Notes

The thermal camera is connected over SPI, so that must be enabled first on the host.
Some instructions on how to do so:
[https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano/initial-setup](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano/initial-setup)

Additionally, this container must be run as
[privileged](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities).