from unittest.mock import Mock
from src.utils import get_info


def test_get_info():
    mock_file_json = Mock(return_value=r"C:\Users\Денис\PycharmProjects\01\data\operations.json")
