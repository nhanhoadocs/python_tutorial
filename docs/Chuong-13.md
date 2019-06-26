# Chương 13: Object-oriented programming

Trong chương này chúng ta sẽ băt đầu đề cập đến hướng đối tượng trong python. Lập trình hướng đối tượng (Object-oriented programming OOP) là một kỹ thuật hỗ trợ cho phép người lập trình trực tiếp làm việc với các đối tượng mà họ định nghiã lên. Kỹ thuật này giúp tăng năng suất, đơn giản hóa độ phức tạp khi bảo trì và mở rộng.

Một Object gồm có:
 * Thuộc tính (Attribute): Ví dụ như hình chữ nhật có 2 thuộc tính là chiều dài và chiều rộng
 * Phương thức (Method): Phương thức nó là một hàm nhưng nó là một hàm bên trong class. Để sử dụng được nó thì phải thông qua đối tượng.

## Tạo class

Để tạo một class trong python ta sử dụng keyword `class` sau đó chỉ ra tên của class.

```
class hinh_chu_nhat:
    """Class hinh chu nhat"""
    dai = 10
    def __init__(self,rong):
        self.rong=rong
    def chuvi(self):
        return 2*(self.dai + self.rong)

```

Như ví dụ trên dòng đầu tiên để khai báo class. Dòng thứ 2 là docstring của class(có thể có hoặc không). Dòng thứ 3 là biến của class. Như ví dụ trên tôi tạo một class có tên là `hinh_chu_nhat` và hình chữ nhật thì có 2 thuộc tính là chiều dài và chiều rộng. Nhưng trong ví dụ trên tôi đã khai báo luôn chiều dài bằng 10 cho nó. Như vậy trong class này thì chiều dài mặc định bằng 10 và ta chỉ cần truyền vào chiều rộng. Dòng thứ 4 sử dụng keyword `def` để khai báo một method. Nhưng ở đây khai báo method đặc biệt `__init__` đây là phương thức khởi tạo (contructor) của class. Hàm này sẽ được gọi khi chúng ta khởi tạo một đối tượng thuộc class này. Dòng thứ 6 tôi lại định nghĩa một method `chuvi` sẽ trả về giá trị là chu vi của hình chữ nhật.

Để thực hiện tạo một đối tượng của class và gọi các method trong class

```
class hinh_chu_nhat:
    """Class hinh chu nhat"""
    dai = 10
    def __init__(self,rong):
        self.rong=rong
    def chuvi(self):
        return 2*(self.dai + self.rong)

hcn_1 = hinh_chu_nhat(5)
chuvi_1 = hcn_1.chuvi()
print("Chu vi HCN là: ",chuvi_1)
```

Khi chạy chương trình kết quả trả về như sau

```
Chu vi HCN là:  30
```

Ta khởi tạo một object `hcn_1` bằng cách gọi class và truyền vào chiều rộng của HCN(vì chiều dài tôi đã khai báo giá trị mặc định là 10 nên ko cần truyền giá trị vào)

```
hcn_1 = hinh_chu_nhat(5)
```

Để gọi vào một method trong class ta chỉ cần sử dụng `object.method()` ví dụ

```
hcn_1.chuvi()
```

## Các tính chất của lập trình hướng đối tượng

* Tính kế thừa
* Tính đóng gói
* Tính đa hình
* Tính trừu tượng

**1 Tính kế thừa**

Python cho phép tạo ra một class bằng cách mở rộng từ một hoặc nhiều class có sẵn. Lớp con sẽ kế thừa các thuộc tính, phương thức và các thành phần khác từ class cha. Nó có thể ghi đè (override) các phương thức từ class cha. Nếu lớp con không tự định nghĩa một constructor nó sẽ được kế thừa lại constructor của lớp cha.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        print("Name: ", self.name)

    def getAge(self):
        print("Tuoi: ", self.age)
    
    def getGt(self):
        print("Gioi tinh: ", self.gt)

class gtNam(Person):
    gt = "Nam"
```

Như ví dụ trên class `gtNam` tôi kế thừa toàn bộ phương thức và thuộc tính của class `Person`.

Ta sẽ khởi tạo một object thuộc class `gtNam`

```
nam_1 = gtNam("Dinh Trong Niem", 18)
nam_1.getName()
nam_1.getAge()
nam_1.getGt()
```

Khi chạy chương trình các giá trị trả về như sau:

```
Name:  Dinh Trong Niem
Tuoi:  18
Gioi tinh:  Nam
```

Nếu trong trường hợp cả lớp cha và lớp con đều tồn tại các thuộc tính và phương thức cùng tên Python sẽ ưu tiên thực thi gọi các phương thức và thuộc tính khai báo trong class khởi tạo.

```
class Class_1:
    name = 'class_1'
    def getName(self):
        print("Class: class_1")
class Class_2(Class_1):
    name = 'Class_2'
    def getName(self):
        print("Class: class_2")

print(Class_1().name)
Class_1().getName()
print(Class_2().name)
Class_2().getName()
```

Kết quả trả về như sau:

```
class_1
Class: class_1
Class_2
Class: class_2
````

Trong trường hợp ở class con mà bạn muốn sử dụng một thành phần trong class cha thì bạn phải sử dụng hàm super.

```
class Class_1:
    name = 'class_1'
    def getName(self):
        print("Class: class_1")
class Class_2(Class_1):
    name = 'Class_2'
    def getName(self):
        print("Class: Class_2")
        super().getName()


Class_2().getName()
```

Khi chạy chương trình ta sẽ thấy ta gọi được cả vào method của class_1

```
Class: Class_2
Class: class_1
```

Đa kế thừa trong python

```
class First:
    def getFirst(self):
        print("Class Fist")
        
class Second:
    def getSecond(self):
        print("Class Second")

class Third(First, Second):
    def getThird(self):
        print("Class Third")

third = Third()
third.getFirst()
third.getSecond()
third.getThird()
```

Ở class `Third` được kế thừa từ 2 class `Frist` và class `Second`. Chương trình chạy sẽ trả về giá trị như sau:

```
Class Fist
Class Second
Class Third
```

**2. Tính đóng gói**

Ta có thể hạn chế truy cập vào trạng thái bên trong của đối tượng. Điều này ngăn chặn việc tác động trực tiếp đến dữ liệu của đối tượng, người ta gọi đây là tính đóng gói. Trong python chúng ta biểu thị thuộc tính private bằng cách thêm sử dụng dấu gạch dưới `__` ở đầu thuộc tính

```
class Person:
    def __init__(self):
        self.__name = "Niem"
        self.age = 18
    
    def getName(self):
        print("Name: ", self.__name)

    def getAge(self):
        print("Tuoi: ", self.age)
    
    def setName(self, name):
        self.__name = name
```

Kết quả 

```
p = Person()

p.getName()
Niem

p.getAge()
18
```

Ta set lại biến 

```
p.__name = "Dinh Trong Niem"
p.age = 20
```

Kết quả trả về

```
p.getName()
Name:  Niem

p.getAge()
Tuoi:  20
```

Như ta thấy `age` đã được thay đổi còn `Name` ta để private nên không thay đổi được. Nếu muốn thay đổi giá trị này tôi đã cung cấp một method `setName` để ta có thể set name. Để set lại Name ta thực hiện gọi method đó

```
p.setName("Dinh Trong Niem")

p.getName()
Name:  Dinh Trong Niem
```

Như vậỵ khi ta khai báo private nếu muốn thay đổi dữ liệu bên trong class ta cần phải cung cấp một method từ bên trong thì ta mới thay đổi được dữ liệu đó.

**3. Tính đa hình**

Tính đa hình là hai hay nhiều class có các method giống nhau nhưng nội dụng thực thi của các method đó là khác nhau.

```
class Person:
    def thucan(self):
        print("An com")
    def dichuyen(self):
        print("Di chuyen bang 2 chan")

class Dongvat:
    def thucan(self):
        print("Khong an com")
    def dichuyen(self):
        print("Di chuyen bang 4 chan")

def check_thucan(loai):
    loai.thucan()

check_thucan(Person())
check_thucan(Dongvat())
```

Như ví dụ trên ta tạo ra 2 class và `Person` và `Dongvat` cùng có method là `thucan` nhưng nội dung thực thi bên trong của các method này là khác nhau. Ta sử dụng tính đa hình để tạo hàm chung cho cả 2 class đó là `check_thucan()`. Khi đó ta chỉ cần truyền các đối tượng vào hàm vừa tạo. Kết quả trả về sẽ như sau:

```
Nguoi an com
Dong vat khong an com
```

**4. Tính trừu tượng**

Tính trừu tượng trong Python ta gom những hành vi và thuộc tính chung nhất vào một class chung và những class cụ thể sẽ được kế thừa từ class này. Ta chỉ khai báo những hành vi và thuộc tính đó chứ không trển khai code trong đó để thực thi. Khi một class được khai báo là trừu tượng thì ta không thể khởi tạo được mà chỉ có thể khởi tạo được thông qua class con của nó. Một class kế thừa lại class trừu tượng thì phải khai báo lại toàn bộ các method trừu tượng bên trong class trừu tượng mà nó kế thừa.

Để khai báo được một class trừu tượng thì class này phải được kế thừa từ Abtract Base Classes của Python

```
from abc import ABC, abstractmethod

class PersonAbstact(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    @abstractmethod
    def getFull(self):
        pass

class Person(PersonAbstact):
    name = 'Dinh Trong Niem'
    age = 18
    def getFull(self):
        self.getName()
        self.getAge()

Person().getFull()
```

Ta phải import các module cần thiết để có thể khai báo một lớp trừu tượng. Trước một method trừu tượng ta cần để `@abstractmethod`. Ta thấy method `getFull` trong class trừu tượng. Method này ta không để bất kỳ đoạn code nào để thực thi. Mà trong class `Person` khi kế thừa lại ta mới để code để thực thi.

Khi thực thi kết quả trả về như sau:

```
Dinh Trong Niem
18
```