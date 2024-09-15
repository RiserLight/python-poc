import pytest
from unittest.mock import AsyncMock, patch
from qwerty.x import MyClass

@pytest.mark.asyncio
@patch('qwerty.x.MyClass.f2', new_callable=AsyncMock)
async def test_my_class(mock_f2):
    # Define the behavior of the mock
    mock_f2.return_value = "mocked f2 result"
    
    # Create an instance of MyClass
    my_class_instance = MyClass()

    # Call the method f2
    result = await my_class_instance.f2()

    # Check that f2 was called
    mock_f2.assert_called_once()

    # Check the result
    print(result)  # Output will be "mocked f2 result"