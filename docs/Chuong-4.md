# Chương 4: Functions

## Gọi function

Trong chương trình ta có sử dụng rất nhiều function. Để sử dụng một function ta gọi ra tên của function ví dụ như sau:

```
>>> type(32)
<class 'int'>
```

Như ví dụ trên tên của function là `type`. Các ký tự bên trong dấu `()` được gọi là đối số. Đối số có thể là giá trị hoặc biến nó là giá trị input của function.

## Một số hàm có sẵn

max()

min()

len()

**Một số hàm chuyển đôi kiểu dữ liệu**

int()

float()

str()

**Hàm random**

Trước khi sử dụng hàm này ta phải `import` hàm này

Ví dụ có chương trình như sau:

```
import random
x = random.random()
print(x)
```

Khi chạy chương trình này sẽ trả về một số ngầũ nhiên nằm trong khoảng từ 0 đến 1.

`random.randint(5, 10)` câu lệnh này sẽ trả về một số nguyên ngẫu nhiên nằm trong khoảng từ từ `5 -> 10`


Chọn một thành phần bất kỳ trong một chuỗi

```
t = [1, 2, 3]
random.choice(t)
3
```

## Hàm math

Math cung cấp hầu hết các hàm tính toán. Trước khi sử dụng module này ta phải thực hiện import nó.

Để sử dụng một function ta chỉ ra tên của module và sau đó chỉ ra tên của function. Sử dụng dấu chấm để ngăn cách giữa tên module và tên function.

VD:

```
math.sin(0.7)
math.log10(100)
math.sqrt(2)
```

## Tạo một function mới

Chúng ta cũng có thể tự tạo các function. Ví dụ:

```
def print_info():
    print("Ho ten: Niemdt")
    print("Tuoi: 18")
```

`def` là một keyword để chỉ ra rằng đây là một định nghĩa hàm. `print_info` là tên của function. Quy tắc đặt tên hàm giống với quy tắc đặt tên biến.

Dấu ngoặc sau tên hàm sử dụng để khai báo đối số truyền vào cho hàm. Như ví dụ trên sẽ không có đối số nào được truyền vào cho hàm.

Dòng đầu tiên của hàm dùng để định nghĩa hàm gọi là `header` những dòng sau gọi là `body`-thân hàm. Thông thường thân hàm mỗi dòng lùi vào 4 dấu cách so với bình thường.

Một hàm sẽ thực thi khi hàm này được gọi. Ta có thể gọi một hàm trong một hàm khác. Ví dụ:

```
def repeat_lyrics():
    print_info()
    print_info()
```

## Tham số và đối số

Một vài function có yêu cầu đối số truyền vào. Một số funciton cần truyền vào nhiều đối số cùng một lúc.

Trong một hàm đối số truyền vào đươc gán cho biến thì nó được gọi là tham số. Ví dụ:

```
def print_twice(bruce):
    print(bruce)
    print(bruce)
```

## Fruitful function and void functions

Bạn gọi một hàm có giá trị trả về bạn có thể gán trực tiếp nó cho một biến để sử dụng. Nếu bạn gọi một hàm ở mode tương tác nó sẽ trả kết quả ra màn hình

```
>>> math.sqrt(5)
2.23606797749979
```

Nhưng nếu bạn đặt nó trong một script mà bạn không gán nó cho biến thì bạn sẽ không thấy đươc giá trị của nó.

Nếu hàm không có giá trị return mà bạn cố gán nó cho một biến thì biến này sẽ nhận một giá trị đặc biệt là `None`

```
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
```

Để trả về một giá trị bạn sử dụng câu lệnh `return` trong function của bạn.

```
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
```

Khi chạy chương trình thì chương trình sẽ in ra màn hình giá trị là `8`.

## Tại sao cần function

Có một vài lý do tại sao nên chia nhỏ chương trình thành các hàm:
 * Giúp bạn dễ đọc, hiểu và debug.
 * Có thể giúp chương trình của bạn ngắn hơn do loại bỏ được các đoạn code lặp. Nếu bạn muốn thay đổi code bạn chỉ cần sửa tại function.
 * Chia chương trình thành các hàm khi bị lỗi bạn có thể kiêm tra từng hàm và biết chính xác đang bị lỗi ở đâu và dễ dàng chỉnh sửa.
 * Nếu hàm của bạn tốt và không có lỗi bạn có thể sử dung nó cho nhiều chương trình.