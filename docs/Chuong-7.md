# Chương 7: Files

Trong chương này chúng ta sẽ làm việc với `Secondary Memory` (or files). Với bộ nhớ này thì dữ liệu của chúng ta sẽ không bị mất khi chúng ta tắt máy. Trong chương này chủ yếu tập trung vào đọc và viết các tệp văn bản. 

## Open files

Để thao tác với file (đọc và viết một file từ hard drive) đầu tiên chúng ta cần phải mở file. Khi mở một file, bạn đang hỏi hệ điều hành tìm kiếm file theo tên và bạn phải chắc chắn rằng file đã tồn tại.

```
In [1]: file=open('test.txt')

In [2]: print(file)
<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
```

Như ví dụ trên tôi mở file `test.txt`. Để mở được file bạn phải lưu file ở trong thư mục mà bạn đã start Python.

Nếu bạn mở file thành công HĐH sẽ trả lại cho chúng ta một file handle. File handle không phải là dữ liệu thực tế có trong tập tin, nhưng thay thế cho file nó là "handle" để giúp chúng ta có thể đọc dữ liệu. Bạn sẽ có một handle nếu file tồn tại và bạn có quyền đọc đối với file đó.

Nếu file không tồn tại open sẽ fail 

```
>>> fhand = open('stuff.txt')
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
```

Trong những trường hợp bạn không chắc chắn file có tồn tại hay không bạn có thể sử dụng `try...except`

## Text files and lines

Một file text có thể được coi là một chuỗi các dòng. Để xuống dòng ta sử dụng `\n`

```
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
```

Ta thấy ký tự xuống dòng cũng được tính là một ký tự.

## Đọc file

File handle không chứa dữ liệu của file nhưng chúng ta có thể sử dụng vòng lặp `for` để đọc và đếm số dòng trong một file

```
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
```

Hàm `open` không đọc toàn bộ dữ liệu trong file là bởi vì file có thể có dung lượng rất lớn đến cả gigabytes. Nếu như vậy chỉ mở file bạn cũng mất một thời gian khá lớn. Như vậy vòng lặp `for` sẽ giải quyết vấn đề này.

Vòng lặp `for` sẽ đọc mỗi dòng một lần. Nó có thể đọc và đếm các dòng trong một file lớn mà không cần sử dụng hết RAM để lưu trữ dữ liệu. 

Nếu bạn biết rằng file của bạn nó dung lượng nhỏ bạn có thể sử dụng method `read` trong phần xử lý tệp.

```
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
From stephen.marquar
```

## Tìm kiếm trong file

Khi bạn bạn chỉ muốn đọc những dòng thỏa mãn một điều kiện nào đó. Bạn có thể kết hợp cách đọc một file và thêm vào đó một vài điều kiện

```
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
```

Như ví dụ trên tôi tiến hành đọc file và chỉ in ra những dòng bắt đầu với `From:`. Ta có kết quả như sau:

```
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

...
```

Như bên trên khi in ra một dòng nó sẽ tự động xuống dòng để tạo ra một dòng trống. Nếu bạn không muôn các dòng trống này bạn có thể dùng thêm method `rstrip`

```
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
```

Khi bạn chạy bạn có thể thấy như sau

```
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
...
```

Bạn có thể sử dụng method `find` để tìm kiếm một chuỗi trong dòng. 

```
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
```

Như ví dụ trên tôi tiến hành tìm kiếm những dòng có chuỗi `@uct.ac.za` và in ra dòng này.

```
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
X-Authentication-Warning: set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan 4 07:02:32 2008
X-Authentication-Warning: set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
...
```

## Ghi dữ liệu vào file

Để ghi dữ liệu vào một file ta mở file và sử dụng thêm mode `w`

```
>>> fout = open('output.txt', 'w')
>>> print(fout)
<_io.TextIOWrapper name='output.txt' mode='w' encoding='cp1252'>
```

Khi mở file nếu file này đã tồn tại nó sẽ xóa toàn bộ dữ liệu cũ trong file để lưu dữ liệu mới nếu file chưa tồn tại nó sẽ tạo ra một file mới.

```
>>> line1 = "This here's the wattle,\n"
>>> fout.write(line1)
24
```

Khi bạn ghi một dòng nào đó vào file nó sẽ trả lại màn hình của bạn giá trị là số ký tự trong của dòng ghi vào. Bạn có vẫn có thể tiếp tục thao tác với file. Đến khi bạn thao tác xong với file này thì bạn cần đóng file lại

```
>>> fout.close()
```

Khi ta mở file để đọc thì chúng ta không cần đóng file vì chúng ta chỉ có thể đọc dữ liệu mà không thể thao tác gì tới nó nên không sợ việc mất mát dữ liệu. Còn khi mở file để ghi nếu thao tác xong bạn ko đóng file lại thì các thể một thao tác nhầm bạn có thể sẽ làm sai dữ liệu trong file.
