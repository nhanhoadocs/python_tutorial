# Chương 6: Strings

## String

String là một chuỗi ký tự liên tục. 

```
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
```

Trong ví dụ trên biến `fruit` được gán một chuỗi `banana`. Tiếp theo đó ta gán ký tự thứ nhất trong biến `fruit` cho biến `letter`. Ta thấy biến `letter` lúc này có giá trị là `a`. Nhưng chúng ta lại thấy `b` mới là ký tự thứ nhất chứ không phải là giá trị `a`. Điều này là bởi vì trong Python quy định nó đánh số thứ tự từ 0 chứ không phải 1 là thứ tự đầu tiên.

```
>>> letter = fruit[0]
>>> print(letter)
b
```

## Get độ dài của chuỗi

Để lấy độ dài của chuỗi ta sử dụng function `len`

```
>>> fruit = 'banana'
>>> len(fruit)
6
```

## String slices

```
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
```

```
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
```

Ta không thể gán một ký tự khác cho string bằng cách

```
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
```

Nếu muốn làm việc này bạn có thể tạo một biến mới

```
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
```

## Vòng lặp 

```
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
```

Như ví dụ trên sẽ tiến hành đếm số ký tự `a` trong chuỗi và in kết quả ra ngoài màn hình

**in**

Ta có thể sử dụng `in` để kiểm tra sự tồn tại của một chuỗi trong một chuỗi khác

```
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
```

## String methods

Strings là một ví dụ về objects trong Python. Một object bao gồm cả dữ liệu và methods. Method là function liệu quả được dựng sẵn cho object.

Python có function được gọi là `dir` function này sẽ liệt kê tất cả những methods có trong một object. Function `type` sẽ show ra kiểu của object còn function sẽ show ra những method.

```
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['capitalize', 'casefold', 'center', 'count', 'encode',
'endswith' , 'expandtabs', 'find', 'format', 'format_map',
'index' , 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier' , 'islower', 'isnumeric', 'isprintable',
'isspace' , 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip' , 'maketrans', 'partition', 'replace', 'rfind',
'rindex' , 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split' , 'splitlines', 'startswith', 'strip', 'swapcase',
'title' , 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str
    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.
>>>
```

Cách sử dụng method

```
>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA
```

```
>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1
```

Ví dụ bạn muốn lấy tên miền của một địa chỉ mail đây sẽ là một cách hay

```
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ',atpos)
>>> print(sppos)
31
>>> host = data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>>
```

## Toán tử định dạng

Để thực hiện việc truyền giá trị của biến vào một vị trí trong chuỗi ta sử dụng như sau

```
>>> camels = 42
>>> '%d' % camels
'42'
```

Hoặc với nhiều giá trị

```
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
```

