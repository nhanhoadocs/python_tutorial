# Giới thiệu về Decorator trong python

Decorator được sử dụng để thay đổi hành vi của một hàm hay một class. Việc sử dụng `decorator` giúp hạn chế được việc lặp code. Bạn có thể thay đổi nội dụng của một hàm hay một class mà không cần tác động trực tiếp đến hàm hay class đó.

Ví dụ:

Chúng ta có một hàm sau:

```
def tinh(n):
    b=n*n
    return b
```

Như hàm trên tôi thực hiện việc truyền vào một số tính bình phương và sau đó return lại kết quả tính được. Nhưng nếu bây giờ tôi không muốn return lại kết quả mà muốn in một kết quả đó ra ta cần sửa lại hàm đó như sau:

```
def tinh(n):
    b=n*n
    print("Ket qua: ", b)
```

Như vâỵ ta phải copy lại hàm và sửa nó. Bây giờ nếu dùng `decorator` ta sẽ giải quyết được vấn đề này.

**Tạo Decorator**

Nếu muốn một hàm nào đó có thể thay đổi sau này ta cần xác định nó từ trước để tạo nó trong Decorator. Để tạo một `decorator` ta làm như sau:

```
def decorator_name(fun):
    def function_name(agrs):
        #do something
        return fun()
    return function_name
```

Ví dụ tôi tạo một decorator có tên `decorator_tinh` cho hàm `tinh` bên trên:

```
def decorator_tinh(f):
    def tinh(n):
        b = n*n
        return f(b)
    return tinh
```

**Sử dụng Decorator**

Để sử dụng decorator ta chỉ cần sử dụng dấu `@` sau đó chỉ ra tên của decorator.

Ví dụ tôi sẽ sử hàm tính sau đó return ra kết quả thành hàm tính nhưng in kết quả ra màn hình

```
@decorator_tinh
def ket_qua(m):
    print("Gia tri:", m)
```

Bây giờ để tính và in kết quả ta chỉ cần gọi hàm `ket_qua()`. Ví dụ tôi gọi hàm

```
ket_qua(5)
```

Giá trị trả về sẽ là:

```
Gia tri: 25
```
