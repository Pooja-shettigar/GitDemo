import pytest
from test_Logging import TestLog


def test_demo11(setup):
    print("Executes after fixture")


def test_parameter(parameterizef):
    print(parameterizef)

