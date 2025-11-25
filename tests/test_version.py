# SPDX-FileCopyrightText: 2025-current Piotr P. Karwasz
# SPDX-License-Identifier: Apache-2.0
"""Test the asf_scripts package."""

from asf_scripts import __version__


def test_version():
    """Test that the version is set correctly."""
    assert __version__ == "0.1.0"
