import pytest
from unittest.mock import AsyncMock, patch
from qwerty.cal import func

@pytest.mark.asyncio
@patch("qwerty.cal.Evaluate")
async def test_func(mock_cal):
    # Create an instance of the mock
    mock_instance = AsyncMock()
    mock_instance.add.return_value = 7
    
    # Set the return value of the find method
    mock_cal.return_value.find.return_value = mock_instance

    result = await func()  
    assert result == mock_instance.add.return_value 