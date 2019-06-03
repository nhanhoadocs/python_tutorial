# Thực thi có điều kiện

## Biểu thức boolean

Biểu thức boolean là một biểu thức trả về hai giá trị là true hoặc false. 
VD biểu thức so sánh.

```
>>> 5 == 5
True
>>> 5 == 6
False
```

Giá trị `True` hoặc `False` có kiểu giá trị là `bool` chứ không phải `string`

```
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

Các phép so sánh

```
x == y
x != y
x > y
x < y
x >= y
x <= y
x is y
x is not y
```

Lưu ý: Với một dấu `=` thì được sử dụng để gán giá trị. Còn sử dụng hai dấu `==` thì sẽ được sử dụng để so sánh.

## Toán tử logic

Có 3 toán tử logic là: and, or, not. 

VD:

`x > 0 and a < 10`  Kết qủa trả về là `True` nếú giá trị của nằm trong khoảng 0< x < 10

`n%2 == 0 or n%3 == 0` trả về giá trị `True` nếu giá trị của n là 2 hoặc 3.

`not (x>y)` trả về giá trị `True` nếu (x>y) là sai <=> x nhỏ hơn y.

## Điều kiện thực thi

Các biểu thức điều kiện giúp cho chương trình chạy theo một trình tự xác định từ trước để chương trình chạy đúng hướng. Câu lệnh `if` là câu lệnh đơn giản nhất.

```
if x > 0 :
    print('x is positive')
```

Câu lệnh `print` sẽ được thực thi nếu biểu thức kiểm tra `x > 0` trả về giá trị là `true`. Nếu biểu thức kiểm tra là đúng thì các câu lệnh phía sau sẽ được thực thi. Các câu lệnh này được tính từ sau dấu `:` và các câu lệnh này sẽ được thụt vào so với câu lệnh `if`.

Lưu ý: Nếu các câu lệnh muốn dùng thực thi nếu biểu thức điều kiện là đúng thì cần phải được thụt vào đều như nhau. Đến khi một câu lệnh được lùi về cùng lề với lệnh `if` thì sẽ được hiểu là nó nằm ngoài điều kiện bên trên.

Khi một biểu thức điều kiện được đưa ra thì sau đó cần phải có ít nhất một lệnh cần thực thi. Nếu trong trường hợp bạn chỉ muốn kiểm tra rằng nó đúng mà không cần thực hiện câu lệnh nào nếu biểu thức điều kiện là đúng. Ta có thể sử dụng lệnh `pass`

```
if x < 0 :
    pass
```

Tương tự như lệnh `if` thì vòng lặp `for` cũng có cách sử dụng tương tự.

Ta có thể sử dụng kết hợp `if...else...` hay kết hợp `if...elif...else...`

```
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
```

hay

```
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```

Hoặc có thể lồng `if...else` trong nhau

```
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```

## Câu lệnh try / except

Bạn có đoạn code như sau:

```
a = input('Nhap vao mot so: ')
b = float(a)
print(b)
```

Bạn cho người nhập nhập vào một số sau đó ép kiểu float cho nó. Nhưng nếu trong trong trường hợp người nhập nhập vào không phải là số thì khi chạy chương trình nó sẽ in ra lỗi.

```
nhap a: d
Traceback (most recent call last):
  File "./test1.py", line 3, in <module>
    b = float(a)
ValueError: could not convert string to float: 'd'
```

Trong những trường hợp như thế này ta sử dụng lệnh `try / except` 

```
a = input("nhap a: ")
try:
    b = float(a)
    print(b)
except:
    print('Hay nhap so')
```

Như vậy nếu khi tiến hành ép kiểu cho biến mà không xảy ra lỗi thì nó sẽ thực hiện tiếp việc in ra biến `b` còn nếu có lỗi thì nó sẽ không thực hiện lệnh tiếp theo mà chuyển sang lệnh `print('Hay nhap so')` bên dưới.

Khi nhập vào là số:

```
niemdt@niemdt:~$ ./test1.py 
nhap a: 2
2.0
```

Khi nhập vào không phải là một số:

```
niemdt@niemdt:~$ ./test1.py 
nhap a: d
Hay nhap so
```

