# Multithreading trong python

Khi lập trình chúng ta thường quan tâm làm sao để code của chúng ta có thể tận dụng được tối đa tài nguyên của máy để chương trình của chúng ta chạy nhanh nhất có thể. 

Trên máy tính chúng ta đều biết đến khái niệm `Thread` hay `luồng` của CPU. Trong python nó sử dụng thread để cho phép tận dụng được tài nguyên của hệ thống.

Tôi có một chương trình gồm 2 hàm như sau:

```
def function_1():
    i = 0
    while i < 5:
        print(i)
        i = i+1
        time.sleep(1)

def function_2():
    i = 10
    while i < 15:
        print(i)
        i = i+1
        time.sleep(1.5)
```

Nếu tôi chạy chương trình này một cách bình thường tôi phải mất `12.5s` để chạy xong 2 hàm này. Nhưng khi tôi cho mỗi `thread` chạy một hàm thì thời gian tôi mất chỉ là `7.5s`.

**Tạo một thread**

Để thực hiện tạo một thread trước tiên ta cần `import` module `threading`

Sử dụng lệnh sau để tạo một thread

```
a = threading.Thread(taget=function_name, args=(arr,))
```

Trong đó:
* Gán `a` cho thread mới khởi tạo
* `function_name` là tên của function mà ta muốn chạy trong thread này
* `args=(arr,)` ta thực hiện khai báo các tham số truyền vào function tại đây

Để chạy hàm khởi tạo trong thread ta dùng lệnh

```
a.start()
```

Các câu lệnh ta không khai báo trong thread nào thì ta có thể hiểu nó được chạy trong một thread chính. Vì vậy nếu muốn các hàm được chạy trong thread chạy xong trước khi chạy các câu lệnh tiếp theo trong thread chính ta dùng lệnh

```
a.join()
```

**Ví dụ**

Tôi chạy chương trình để thực hiện 2 hàm bên trên

Trong trường hợp không dùng thread

```
import time
import threading

def function_1():
    i = 0
    while i < 5:
        print(i)
        i = i+1
        time.sleep(1)

def function_2():
    i = 10
    while i < 15:
        print(i)
        i = i+1
        time.sleep(1.5)

t = time.time()
function_1()
function_2()
t2 = time.time()
print("Time: ",t2-t)

```

Kết quả trả về:

```
0
1
2
3
4
10
11
12
13
14
Time: 12.51435899734497
```

Khi dùng thread

Code
```
import time
import threading

def function_1():
    i = 0
    while i < 5:
        print(i)
        i = i+1
        time.sleep(1)

def function_2():
    i = 10
    while i < 15:
        print(i)
        i = i+1
        time.sleep(1.5)

t = time.time()
a1 = threading.Thread(target=function_1)
a2 = threading.Thread(target=function_2)
a1.start()
a2.start()
a1.join()
a2.join()
t2 = time.time()
print("Time: ",t2-t)
```

Kết quả trả về như sau:

```
0
10
1
11
2
12
3
4
13
14
Time:  7.506760835647583
```

## Đồng bộ hóa các Thread

Khi sử dụng multithread trong python đôi khi chúng ta có những dữ liệu dùng chung giữa các thread. Như vậy vấn đề xảy ra ở đây là có những thời gian có nhiều thread cùng truy cập  vào dữ liệu dùng chung. Như vậy thì có thể dữ liệu đầu vào của các thread có thể bị sai. Để giải quyết vần đề này ta chỉ cho phép một thread thao tác với dữ liệu dùng chung tại một thời điểm. Như vậy thì dữ liệu sẽ được đồng bộ giữa các thread.

Ta có một số module để thực hiện việc đồng bộ trong Python như `Locks`, `RLocks`, `Semaphores`, `Events`, `Conditions`,...

**Locks**

Lock là cơ chế đồng bộ cơ bản nhất trong python. Một lock có 2 trong thái là `locked` và `unlocked`. Có 2 method để thao tác với lock là `acquire()` và `release()`
* Nếu trạng thái đang là `unlocked` gọi `acquire()` thì trạng thái sẽ đổi sang `locked`
* Nếu trạng thái đang là `locked` gọi `release()` thì trạng thái sẽ chuyển sang `unlocked`

Tại một thời điểm chỉ có một thread sở hữu lock