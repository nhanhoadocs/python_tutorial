Tôi thực hiện test với function `get_port`. Ở đây tôi tạo 2 file:
* File `getport.py` chứa function cần test
* File `unittest_getport.py` chứa chương trình test.

Chạy chương trình test

```
(beautiful) niemdt@niemdt:~/virtualenv$ python -m unittest unittest_getport.py 
..
----------------------------------------------------------------------
Ran 2 tests in 2.417s

OK
```

Trong chương trình test tôi giả định ra 2 trường hợp để test. Sau khi chạy test ta thấy tôi đã dự đoán đúng được kết quả trả về.

Nêú trong trường hợp kết quả trả về không giống với kết quả dự kiến của ta khi truyền vào kết quả sẽ return lại như sau:

```
(beautiful) niemdt@niemdt:~/virtualenv$ python -m unittest unittest_getport.py 
F.
======================================================================
FAIL: test_error (unittest_getport.TestgetPort)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/niemdt/virtualenv/unittest_getport.py", line 16, in test_error
    self.assertEqual(result, "rror!!!")
AssertionError: 'Error!!!' != 'rror!!!'
- Error!!!
? -
+ rror!!!
```

Ta thấy trong trường hợp test thứ 2 kết quả trả về đã không giống với kết quả dự kiến. Kết quả trả về của trường hợp này là `Error!!!` trong khi kết quả dự kiến là `rror!!!`.

