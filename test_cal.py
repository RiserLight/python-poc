import pytest
from unittest.mock import AsyncMock, patch
from qwerty.cal import func

@pytest.mark.asyncio
@patch("qwerty.cal.Calculations")
async def test_func(mock_cal):
    # Create an instance of the mock
    mock_instance = AsyncMock()
    mock_instance.add.return_value = 9  # Set the return value for the add method
    mock_cal.return_value = mock_instance  # Return the mock instance when Calculations is called

    result = await func()  # Call the async function
    assert result == 9  # Check if the result matches the expected value