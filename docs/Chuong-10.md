# Chương 10: Tuples

Tuple là một chuỗi các giá trị giống như danh sách. Giá trị được lưu trong một tuple có thể là bất kỳ loại gía trị nào. Điểm khác biệt quan trọng là tuple là bất biến. Các bộ dữ liệu này cũng có thể so sánh và sắp xếp các giá trị trong một tuple. Và ta sử dụng tuple như key values trong thư dictionary của Python.

Trong một tuple các giá trị được phân cách nhau bởi dấu phẩy. Ta có 2 cách viết

```
>>> t = 'a', 'b', 'c', 'd', 'e'
```

Hoặc có thể để chúng trong ngoặc

```
>>> t = ('a', 'b', 'c', 'd', 'e')
```

Để tạo một tuple ta phải cho thêm dấu phẩy

```
>>> t1 = ('a',)
>>> type(t1)
<type 'tuple'>
```

Nếu không có dấu phẩy nó sẽ hiểu đây kiểu dữ liệu string

```
>>> t2 = ('a')
>>> type(t2)
<type 'str'>
```

Hoặc để ta có thể sử dụng cách khác để tạo một tuple

```
>>> t = tuple()
>>> print(t)
()
```

Hoặc 

```
>>> t = tuple('lupins')
>>> print(t)
('l', 'u', 'p', 'i', 'n', 's')
```

Ta cũng có thể thao tác với tuple giống như ta thao tác với string

```
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])
'a'

>>> print(t[1:3])
('b', 'c')
```

Ta cũng không thể thay đổi giá trị bằng cách

```
>>> t[0] = 'A'
TypeError: object doesn't support item assignment
```

Nếu muốn ta phải sử dụng cách sau

```
>>> t = ('A',) + t[1:]
>>> print(t)
('A', 'b', 'c', 'd', 'e')
```

Ta có thể so sánh giữa 2 tuple. Nó sẽ so sánh giống như ta so sánh 2 số tự nhiên nếu giá trị hành chục lớn hơn thì số đó sẽ lớn hơn mà không quan tâm đến giá trị của hành đơn vị

```
>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
```

Ta có thể thực hiện việc gán một tuple với một chuỗi như sau

```
>>> m = [ 'have', 'fun' ]
>>> x, y = m
>>> x
'have'
>>> y
'fun'
>>>
```

Hoặc ta có thể

```
>>> m = [ 'have', 'fun' ]
>>> x = m[0]
>>> y = m[1]
>>> x
'have'
>>> y
'fun'
>>>
```

Hoặc

```
>>> m = [ 'have', 'fun' ]
>>> (x, y) = m
>>> x
'have'
>>> y
'fun'
>>>
```

Ta cũng có thể

```
>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
>>> print(uname)
monty
>>> print(domain)
python.org
```

Việc gán này số biến ở bên phải và bên traí phải như nhau. Nếu khác nhau nó sẽ báo lỗi và không thể gán.

## Dictionary và tuple

Dictionary có method `items` để chuyển một dictionary thành một danh sách các tuple. Mỗi tuple là một key và một value

```
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> print(t)
[('b', 1), ('a', 10), ('c', 22)]
```

Ta có thể sắp xếp lại list này

```
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> t
[('b', 1), ('a', 10), ('c', 22)]
>>> t.sort()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
```

Như ví dụ trên là key xếp trước value khi chuyển từ dictionary sang list. Nếu muốn để value đứng trước key ta có thể thực hiện như sau

```
>>> d = {'a':10, 'b':1, 'c':22}
>>> l = list()
>>> for key, val in d.items() :
...     l.append( (val, key) )  
...
>>> l
[(10, 'a'), (22, 'c'), (1, 'b')]
>>> l.sort(reverse=True)
>>> l
[(22, 'c'), (10, 'a'), (1, 'b')]
>>>
```
