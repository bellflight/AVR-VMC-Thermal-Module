from __future__ import annotations

from typing import TYPE_CHECKING, List
from bell.avr.mqtt.payloads import AVRThermalReading

import pytest
from pytest_mock.plugin import MockerFixture

if TYPE_CHECKING:
    from src.thermal import ThermalModule


@pytest.mark.parametrize(
    "input_pixels, output_data",
    [
        (
            [[0.0] * 8] * 8,
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==",
        ),
        (
            [[20.0] * 8] * 8,
            "FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFA==",
        ),
    ],
)
def test_request_thermal_reading(
    mocker: MockerFixture,
    thermal_module: ThermalModule,
    input_pixels: List[List[float]],
    output_data: str,
) -> None:
    # patch the thermal camera reading
    mocker.patch(
        "adafruit_amg88xx.AMG88XX.pixels",
        new_callable=lambda: mocker.PropertyMock(return_value=input_pixels),
    )

    # run function and check output
    thermal_module.request_thermal_reading()
    thermal_module.send_message.assert_called_once_with(
        "avr/thermal/reading",
        AVRThermalReading(data=output_data),
    )
