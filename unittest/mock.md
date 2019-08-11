# Mock

Mock được sử dụng để mock một giá trị trả về.

Như ví dụ dưới đây tôi sử dụng mock để để mock giá trị return định dạng json của khi query giá trị của bot telegram.

```
import unittest
from mock import Mock
from mock import patch
import requests
import unittest
import json


def get_text():
    response = requests.get('')
    a = response.json.load
    text = a["result"][0]["message"]["text"]
    return text


class TetsApi(unittest.TestCase):

    def test_api(self):
        js = {
            "result": [{"update_id": 998276345,
            "message": {"message_id": 146, "from": {"id": 659034096,
            "is_bot": 'false', "first_name": "\u0110inh Tr\u1ecdng",
            "last_name": "Ni\u1ec7m", "username": "niemdt",
            "language_code": "en"}, "chat": {"id": 659034096,
            "first_name": "\u0110inh Tr\u1ecdng", "last_name": "Ni\u1ec7m",
            "username": "niemdt", "type": "private"},
            "date": 1563180182, "text": "hello"}}]}
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.json.load = js
            assert get_text() == "hello"
```

Như ví dụ bên trên tôi sử dụng `unittest` để test hàm `get_text`. Đúng ra ta phải truyền vào url để lấy giá trị trả về. Nhưng tôi đã sử dụng `mock` để gán cho nó giá trị trả về là `js` để thực hiện việc test dễ dàng hơn.