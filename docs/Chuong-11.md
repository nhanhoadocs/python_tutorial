# Chương 11: Regular expressions

Chúng ta muốn đọc một file và lọc ra những thông tin phù hợp. Có nhiều cách để thực hiện việc này nhưng Python cũng cung cấp một thư viện có tên `regular expressions`. Để sử dụng được thư viện này ta phải tiến hành import nó. 

Ví dụ để hiển thị những dòng có chứa `From:`

```
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
```

Nếu bạn muốn search những dòng bắt đầu với `From:` ta sử dụng như sau

```
if re.search('^From:', line):
```

Ta sử dụng thêm ký tự `^`.

Nếu bạn muốn trích xuất ra một phần dữ liệu phừ hợp từ một chuỗi trong Python chúng ta có thể sử dụng method `findall()` để extract tất cả các substrings mà nó match với regular expression của ta.

```
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)
```

Như ví dụ trên khi chạy chương trình sẽ hiển thị ra các địa chỉ mail. 

```
['csev@umich.edu', 'cwen@iupui.edu']
```

Nếu bạn chỉ muốn hiển thị một giá trị mà nó thỏa mãn nhiều điều hiện cùng lúc thì bạn cho giá trị muốn hiển thị vào dấu `()`

Ví dụ file `mbox-short.txt` có chứa các thông tin sau

```
X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000
X-DSPAM-Confidence: 0.6178
X-DSPAM-Probability: 0.0000
Confidence:
DSPAM-Probability: 0.0000
```

```
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
```

Chương trình thực thi nó sẽ cho ra kết qủa như sau

```
['0.8475']
['0.0000']
['0.6178']
['0.0000']
```

## Một số toán tử để sử dụng trong regular expression

`^` match giá trị tính từ đầu dòng

`$` Match giá trị ở cuối dòng

`.` Match bất kỳ ký tự nào

`\s` Match với một ký tự khoảng trống

`\S` Match với một giá trị mà không chứa khoảng trống

`*` Match với các giá trị đứng ngay trước đó (bất kỳ gía trị nào)

`+` Giống `*` nhưng sau đó cần match với ít nhất một giá trị

`[a-z0-9]` Bạn có thể chỉ ra dải ký tự.

`()` chỉ để lấy ra substring trong chuỗi thỏa mãn regular expression

`\b` match với một chuỗi trống nhưng chỉ ở đầu hoặc cuối 1 từ

`\B` match với một chuỗi trống nhưng không phải ở đầu hoặc cuối 1 từ

`\d` match với các số thập phân. Tương đương với [0-9].

`\D` match với giá trị không phải số.