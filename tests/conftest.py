from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import pytest
from pytest_mock.plugin import MockerFixture

if TYPE_CHECKING:
    from src.thermal import ThermalModule


@pytest.fixture
def thermal_module(mocker: MockerFixture) -> ThermalModule:
    # first, mock the board module
    sys.modules["board"] = mocker.MagicMock()

    # patch the send message function
    mocker.patch("src.thermal.ThermalModule.send_message")

    # create module object
    from src.thermal import ThermalModule

    return ThermalModule()
