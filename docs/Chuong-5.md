# Chương 5: Iteration

## Update giá trị của biến

```
x = x + 1
```

Mỗi lần thực hiện câu lệnh thì x lại có một giá trị mới(tăng lên 1 so với giá trị cũ của x). Trước khi update một gía trị mới cho một biến thì biến này phải được gán cho một giá trị trước đó. Nếu không biến không có một giá trị trước đó thì khi thực hiện update chương trình sẽ báo lỗi

```
>>> x = x + 1
NameError: name 'x' is not defined
```

```
>>> x = 0
>>> x = x + 1
```

## While

Máy tính thường được sử dụng để thực hiện các công việc lặp đi lặp lại. Việc thực hiện những công việc lặp đi lặp lại một việc tương đối dễ dàng với máy tính nhưng nó khó thực hiện hơn với chúng ta. Vì vậy Python cũng cung cấp một vài lệnh để thực hiện những công việc này một cách dễ dàng.

```
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```

Bên trên là một ví dụ đơn giản. Khi nào x còn lớn hơn 0 thì vòng lặp vẫn được thực hiện. Mỗi lần thực hiện vòng lặp nó sẽ in ra giá trị của n sau đó giảm n đi 1 đơn vị. Tiếp theo đó nó sẽ kiểm tra điều kiện nếu n còn lớn hơn 0 thì nó sẽ tiếp tục in n và giản giá trị của n đi 1. Nó thực hiện việc này cho đến khi n = 0. Khi n bằng 0 vòng lặp sẽ kết thúc và chương trình sẽ in ra chuỗi ký tự `Blastoff!`

Thông thường trong thân của vòng lặp thường có một hoặc nhiều giá trị biến thay đổi sau mỗi vòng lặp để đến khi điều kiện kiểm tra là `False` thì vòng lặp sẽ kết thúc.  Người ta gọi biến đó là biến lặp. Nếu không có biến lặp trong thân của vòng lặp vòng lặp sẽ lặp mãi mãi, người ta gọi đó là vòng lặp vô hạn.

## Vòng lặp vô hạn và break

Đôi khi bạn không biết khi nào sẽ kết thúc vòng lặp cho đến khi bạn đã thực hiện vào thân của vòng lặp. Trong trường hợp như vậy bạn có thể viết một vòng lặp vô hạn và sau đó sử dụng lệnh `break` để thoát ra khỏi vòng lặp

```
n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')
```

Bạn có thể thấy như ví dụ trên đây là một vòng lặp vô hạn vì nó không có một giá trị nào để kiêm tra để thoát khỏi vòng lặp. Giá trị của nó luôn là `True` nên vòng lặp vô hạn.

Với điều kiện là `True` này cũng rất hữu ích nếu ta biết cách sử dụng nó. Ta có thể thêm các đoạn code phù hợp vào trong thân của vòng lặp để đến khi có một giá trị phù hợp ta sẽ thoát khỏi vòng lặp bằng cách dùng câu lệnh `break`.

```
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
```

Như ví dụ trên ta thấy giá trị luôn là `True` nên vòng lặp là vòng lặp vô hạn. Vòng lặp cho phép nhập vào một dòng và thực hiện in dòng này ra màn hình. Vòng lặp sẽ không kết thúc vì biểu thức điều kiện là `True`. Nhưng ta để ý thấy trong thân vòng lặp có lệnh `if`. Lệnh này được dùng để kiểm tra nếu người nhập nhập vào giá trị là `done` thì lệnh `break` sẽ được thực thi. Khi lệnh `break` thực thi thì ngay lập tức nó sẽ bỏ qua các lệnh bên dưới và thoát ra khỏi vòng lặp ngay lập tức. Như ví dụ trên khi người nhập nhập vào giá trị là `done` thì dòng `print(line)` sẽ bị bỏ qua, vòng lặp kết thúc và lệnh `print('Done!')` được thực thi sau đó kết thúc chương trình.

## Continue

Đôi khi bạn đang ở trong thân của vòng lặp nhưng bạn muốn kết thúc vòng lặp hiện tại để thực hiện lần lặp tiếp theo. Trong trường hợp như vậy bạn có thể sử dụng câu lệnh `continue` để sang lần lặp tiếp theo mà không cần kết thúc các câu lệnh còn lại trong thân của vòng lặp.

```
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```

Như ví dụ trên vòng lặp cũng là vòng lặp vô hạn. Chương trình cho phép người nhập nhập vào một chuỗi và tiến hành in chuỗi đó ra màn hình. Trong thân của vòng lặp có 2 câu lệnh kiểm tra `if`. Với dòng `if` đầu tiên nếu ký tự đầu tiên nhập vào là dấu `#` thì nó sẽ bỏ qua tất cả các lệnh bên dưới như lệnh `if` thứ 2 và lệnh `print(line)` và nó sẽ thực hiện một vòng lặp mới cho phép người nhập nhập vào một chuỗi. Với lệnh `if` thứ 2 nếu người nhập nhập vào lf `done` thì nó cũng bỏ qua dòng lệnh bên dưới là `print(line)` và thoát khỏi vòng lặp để thực hiện lệnh `print('Done!')` trước khi kết thúc chương trình

```
> hello there
hello there
> # don't print this
> print this!
print this!
> done
Done!
```

## Vòng lặp for

Vòng lặp `for` thường được sử dụng để lấy các giá trị trong một sanh sách.

```
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```

Như trong ví dụ trên ta có một danh sách. Ta sử dụng vòng lặp `for` cho biến `friend` gán lần lượt các giá trị trong danh sách `friends`. Mỗi lần được gán giá trị này sau đó thực hiện lệnh `print('Happy New Year:', friend)`. Khi biến `friend` được gán đến giá trị cuối cùng là `Sally` thì vòng lặp sẽ kết thúc.

```
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```
