# Biến, biểu thức và câu lệnh

## Biến

Khai báo biến trong dấu `''` thì python hiểu đó là `string`

```
>>> type('17')
<class 'str'>
```

Không có dấu nháy VD thì có mà là số thì là `int` hoặc `fload`

VD: 

```
>>> type('Hello, World!')
<class 'str'>
>>> type(17)
<class 'int'>
>>> type(3.2)
<class 'float'>
```

Với việc gán biến cũng tương tự như vậy.

```
>>> message = 'And now for something completely different'
>>> n = 17
```

```
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
```

Nên chọn tên biến phù hợp với giá trị để dễ dàng nhớ khi gọi. Biến có thể có cả chữ và số.

Lưu ý biến không nhận các ký tự đặc biệt ngoại trừ ký tự gạch dưới "_" 

VD: ten_bien

Biến có thể có cả số nhưng không được đặt số ở đầu.

Các key word không được sử dụng làm biến 

![](/images/1.png)

## Câu lệnh

Câu lệnh là đơn vị của code mà trình thông dịch Python có thể thực thi. Có kiểu câu lệnh câu lệnh print và câu lệnh biểu thức.

## Biểu thức tính toán

Sử dụng các tính toán bình thường. Có thể thực hiện phép toán với biến nếu đã gán giá trị cho biến.

Có một vài điểm khác biệt giữa Python2 và Python3
VD:

```
a = 5

a/2 = 2.5(Python3)
a/2 = 2 (Python2)
```

Để chia lấy phần nguyên trên Python3 ta sử dụng `//`

VD: `a//2 = 2`

Chia lấy dư sử dụng `%`

VD: `7%3 = 1`

Các biểu thức toán học trong Python được thực hiện đúng với các quy tăc thực hiện các phép toán bình thường.

Lưu ý:

Phép cộng cũng làm việc với dữ liệu kiểu `string` nhưng kết quả trả về của nó sẽ là ghép các chuỗi lại

VD:

```
>>> first = 10
>>> second = 15
>>> print(first+second)
25

>>> first = '100'
>>> second = '150'
>>> print(first + second)
100150
```

## Nhập input từ bàn phím

Sử dụng `input()` để nhập một giá trị đầu vào từ bàn phím.

Nên để một dấu hiệu gì  đó cho người nhập biết là họ cần phải nhập thông tin vào

```
nhap = input('Nhap gi di: \n')
```

Khi mà ta nhập giá trị đầu vào thì giá trị này sẽ được gán cho biến `nhap`

## Comments

Với một chương trình lớn khi đó nhìn những dòng code bạn sẽ thấy rối mắt hoặc khi bạn code một chương trình nào đó bạn muốn người khác đọc code của bạn và có thể hiểu bạn đang làm gì trong phần này ngay tại code của bạn. Bạn có thể thêm các comment vào code của bạn mà điều này sẽ không ảnh hưởng gì đến code của bạn.

Để bắt đầu một dòng comments ta sử dụng ký hiệu `#` ở đầu mỗi dòng comment.

