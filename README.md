# AVR-VMC-Thermal-Module

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Thermal Module](https://github.com/bellflight/AVR-VMC-Thermal-Module/actions/workflows/build.yml/badge.svg)](https://github.com/bellflight/AVR-VMC-Thermal-Module/actions/workflows/build.yml)

The Thermal module is responsible for capturing thermal images from the thermal
camera and publishing them over MQTT.

## Development

It's assumed you have a version of Python installed from
[python.org](https://python.org) that is the same or newer as
defined in the [`Dockerfile`](Dockerfile).

First, install [Poetry](https://python-poetry.org/) and
[VS Code Task Runner](https://pypi.org/project/vscode-task-runner/):

```bash
python -m pip install pipx --upgrade
pipx ensurepath
pipx install poetry
pipx install vscode-task-runner
# (Optionally) Add pre-commit plugin
poetry self add poetry-pre-commit-plugin
```

Now, you can clone the repo and install dependencies:

```bash
git clone https://github.com/bellflight/AVR-VMC-Thermal-Module
cd AVR-VMC-Thermal-Module
vtr install
```

Run

```bash
poetry shell
```

to activate the virtual environment.

### Developer Notes

The thermal camera is connected over SPI, so that must be enabled first on the host.
Some instructions on how to do so:
[https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano/initial-setup](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano/initial-setup)

Additionally, this container must be run as
[privileged](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities).
