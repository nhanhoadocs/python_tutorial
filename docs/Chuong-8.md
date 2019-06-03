# Chương 8: Lists

Một list bao gồm nhiều giá trị. Giá trị có thể thuộc bất kỳ kiểu dữ liệu nào. Giá trị trong danh sách được gọi là `elements` hoặc `items`

```
[10, 20, 30, 40]

['crunchy frog', 'ram bladder', 'lark vomit']
```

Hoặc một danh sách có thể bao gồm nhiều kiểu dữ liệu và nó còn có thể bao gồm cả một danh sách khác

```
['spam', 2.0, 5, [10, 20]]
```

Bạn cũng có thể tạo một danh sách mà không chứa bất kỳ giá trị nào

```
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
```

Cũng giống như các ký tự trong string, trong danh sách một elements trong danh sách cũng giống như một ký tự trong string.

```
>>> print(cheeses[0])
Cheddar
```

Nhưng nó không giống như string vì trong list bạn có thể thay giá trị của một items 

```
>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]
```

Như ví dụ trên giá trị `123` đã được thay thế bằng giá trị `5`.

Bạn cũng có thể sử dụng `in` để kiểm tra một items có tồn tại trong list hay không

```
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False
```

Bạn có thể duyệt qua toàn bộ items trong list nó cũng giống với string

```
for cheese in cheeses:
    print(cheese)
```

Ghép 2 list

```
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```

Lặp một items

```
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

Ta có thể list ra các slice giống như trong string

```
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
```

Ta có thể thay đổi giá trị của list theo cách này

```
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']
```

## List methods

Python cung cấp một vài method được sử dụng trên lists. Ví dụ method `append` được sử dụng để add thêm một giá trị mới vào cuối của danh sách

```
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print(t)
['a', 'b', 'c', 'd']
```

hay như `extend`

```
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
```

`sort` dùng để sắp xếp giá trị từ thấp đến cao

```
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']
```

## Deleting elements

Có một vài cách để xóa element từ một danh sách. 

```
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b
```

`pop` sẽ tiến hành xóa và nó return lại giá trị nó đã xóa. Nếu bạn không chỉ ra index của items nó mặc định sẽ xóa giá items cuối cùng.

Nếu bạn ko cần return lại giá trị đã xóa bạn có thể sử dụng `del`

```
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print(t)
['a', 'c']
```

Để remove nhiều hơn 1 giá trị

```
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> print(t)
['a', 'f']
```

Nó sẽ tiến hành xóa từ index đầu tiên đến index thứ 2 nhưng không xóa giá trị ở index có giá trị thứ 2.

## Lists and functions

Có một số function có sẵn có thể sử dụng trong list 

```
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums))
6
>>> print(max(nums))
74
>>> print(min(nums))
3
>>> print(sum(nums))
154
>>> print(sum(nums)/len(nums))
25
```

Để tính tổng hoặc giá trị trung bình ta có thể áp dụng các hàm này

```
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)
```

## Lists and strings

Chúng ta có thể convert một string thành một list các ký tự

```
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
```

`list` sẽ ngắt một string ra thành các chữ cái riêng lẻ nếu bạn muốn ngắt string thành các từ bạn có thể dùng `split`

```
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']
>>> print(t[2])
the
```

Như ví dụ trên nó sẽ ngắt các từ dựa vào dấu cách. Trong một số trường hợp bạn không dùng dấu cách để phân cách giữa các từ mà bạn dùng một ký tự khác. Trong trường hợp như vậy bạn có thể khai báo ký tự phân cách giữa các từ để ngắt các từ

```
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
```

Chúng ta cũng có thể join các từ trong một list lại thành chuỗi

```
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```

## Objects and values

Nếu chúng ta thực hiện việc gán giá trị như sau:

```
a = 'banana'
b = 'banana'
```

Chúng ta thấy rằng cả 2 biến a và b đều có cùng một giá trị nhưng chúng ta không biết liệu nó có cùng trỏ đến một chuỗi. Có 2 trạng thái có thể xảy ra

![](/images/5.png)

Trong trường hợp thứ nhất a và b chúng là 2 object khác nhau nhưng có gía trị giông nhau. CÒn trong trường hợp thứ 2 cả a và b cùng đề cập đến một object.

```
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
```

Như ví dụ trên nó, Python chỉ tạo ra một đối tượng string và cả a và b đề trỏ đến nó.

Nhưng khi bạn tạo 2 lists nó sẽ là 2 đôi tượng khác nhau

```
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
```

```
>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
```

Như ví dụ trên ta thực hiện gán `a = b` lúc này cả a và b đều trỏ đến cùng một object. Nên khi thay đôỉ có sẽ có thay đổi trên cả 2 biến

```
>>> b[0] = 17
>>> print(a)
[17, 2, 3]
```

