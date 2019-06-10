# Chương 9: Dictionaries

Dictionary cũng giống như list. Trong danh sách index phải là kiểu integer còn trong dictionary thì index có thể là bất kỳ kiểu dữ liệu nào. Ta có thể hình dung trong dictionary thực hiện set index (key) và giá trị. Mỗi key sẽ map đến một giá trị.

Sử dụng `dict` để tạo một dictionary ban đầu

```
>>> eng2sp = dict()
>>> print(eng2sp)
{}
```

Để add một item vào dictionary ta có thể sử dụng 

```
>>> eng2sp['one'] = 'uno'
```

Bây giờ ta có thể thấy key đã map tới được value

```
>>> print(eng2sp)
{'one': 'uno'}
```

Ta cũng có thể gán giá trị như sau

```
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp)
{'one': 'uno', 'three': 'tres', 'two': 'dos'}
```

Có thể thấy được giá trị nếu ta biết key 

```
>>> print(eng2sp['two'])
'dos'
```

Như ví dụ trên key `two` được map tới giá trị `dos`. Ta có thể sử dụng function `len` nó sẽ return lại số key-value

```
>>> len(eng2sp)
3
```

Ta có thể kiểm tra một key có trong dectionary bằng cách sử dụng `in`

```
>>> 'one' in eng2sp
True
```

Nhưng ta không dùng được cách này để kiểm tra một giá trị có trong dectionary

```
>>> 'uno' in eng2sp
False
```

Để kiểm tra một giá trị có trong dectionary hay không ta sử dụng

```
>>> vals = list(eng2sp.values())
>>> 'uno' in vals
True
```

Ta có thể tạo một dictionary để thực hiện đếm các ký tự có trong một chuỗi

```
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
```

Như ví dụ trên ta thực hiện lấy ký tự trong chuỗi làm key. Sau đó tiến hành kiểm tra nếu key chưa có trong dictionary thì sẽ được gán giá trị là 1. Nếu key đã tồn tại trong dictionary thì giá trị của key sẽ tăng lên 1.

Khi chạy chương trình ta sẽ thấy output như sau:

```
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
```

Ta có thể sử đụng method `get` để hiển thị giá trị của một key và cũng có thể trả về một giá trị mặc định nếu key đó chưa tồn tại.

```
>>> counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
>>> print(counts.get('jan', 0))
100
>>> print(counts.get('tim', 0))
0
```

Ta có thể sử dụng cách này để làm lại ví dụ trên như sau

```
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
```

Ta có thể sử dụng vòng lặp để hiển thị mỗi giá trị tương ứng với mỗi key

```
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
```

