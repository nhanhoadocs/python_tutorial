## Một số khái niệm

**Lập trình hướng cấu trúc**

Lập trình hướng cấu trúc (Procedure Oriented Programming) là ngôn ngữ lập trình trong đó một chương trình sẽ được chia thành các hàm . Mỗi hàm cũng có thể có các hàm con khác. 

Ưu điểm:

 * Tư duy giải thuật rõ ràng
 * Đơn giản dễ hiểu

Nhược điểm:
 
 * Trong lập trình hướng cấu trúc ta thường quan tâm đến phát triển các hàm mà ít quan tâm đến dữ liệu.
 * Mỗi cấu trúc dữ liêụ chỉ phù hợp với một số giải thuật -> khi cấu trúc dữ liệu thay đổi thì dữ liệu cũng phải thay đổi theo -> không sử dụng lại được code.

Một số ngôn ngữ: C, pascal,..

**Lập trình hướng đối tượng**

Đối tượng (obiect) là những sự vật sự việc mà nó có những tính chất đặc tính và gom lại thành đối tượng.

Ta có thể tự định nghĩa những đối tượng không có thật để giải quyết bài toán của mình.

Một đôí tượng sẽ bao gồm 2 thành phần là đặc tính và hành vi.

Ví dụ như đối tượng động vật có đặc tính như chân, mắt, mũi,.. và các hành vi như: ăn, uống, đi, chạy,...

Lập trình hướng đối tượng (Object-oriented programming) là lập trình hỗ trợ công nghệ đối tượng cho phép người lập trình tập trung vào các đôí tượng giống như thực tế. Lập trình hướng đối tượng giúp tăng năng suất và đơn giản hóa độ phức tạp khi bảo trì cũng như mở rộng.

Một số ngôn ngữ hướng đối tượng: Java, C++, Python, PHP,...

Lập trình hướng đối tương có 4 tính chất sau:

 * Tính trừu tượng
 * Tính đóng gói
 * Tính đa hình
 * Tính kế thừa

**Ngôn ngữ thông dịch**

Ngôn ngữ thông dịch (interpreted) là khi một dòng code được thực thi đến đâu thì nó sẽ được chuyển dòng đó trực tiếp thành ngôn ngữ máy để thực thi.

Ưu điểm:

 * Hỗ trợ đa nền tảng
 * Kích thước chương trình thực thi nhỏ hơn.

Khuyết điểm:

 * Chương trình có độ tin cậy thấp hơn do bỏ qua bước kiểm tra loại bỏ một số lỗi thường thường thực hiện trong qúa trình biên dịch.
 * Source dễ bị dịch ngược
 * Tốc độ thực thi chậm hơn

Nhóm này gồm một số loại ngôn ngữ: Python, PHP,..

**Ngôn ngữ biên dịch**

Ngôn ngữ biên dịch (compiled): khác với thông dịch là đọc đến đâu dịch đến đó thì biên dịch sẽ dịch toàn bộ sang ngôn ngữ máy lưu lại thành một file rồi mới tiến hành thực thi.

Ưu điểm: 
 
 * Chương trình sau khi dịch sẽ được thực thi nhanh hơn
 * Độ tin cậy cao 
 * Khó bị dịch ngược source code

Khuyết điểm:

 * Khó xây dựng một ngôn ngữ biên dịch có tính chính xác cao để chuyển toàn bộ chương trình thành mã máy.
 * Mã máy của mỗi nền tảng là khác nhau, khó thực hiện đa nền tảng.

Nhóm này bao gồm một số ngôn ngữ như: C, C++, Java, Pascal,...

**Virtual Environments**

Virtual environment là một môi trường ảo. Nó được hiểu gần giống như máy ảo thay vì cài đặt các phần mềm có thể gây ra lỗi cho hệ thống lên host thì ta có thể tạo ra một VM là cài các ứng dụng lên đó mà sẽ ko gây ảnh hưởng gì đến host. Virtual Environment cũng có chức năng tương tự. Với mỗi chương trình có thể ta sẽ phải sử dụng các packages khác nhau. Các packages này có thể bị conflict. Như vậy ta có thể cài các package này trên các môi trường khác nhau điều đó sẽ không gây ảnh hưởng gì đến môi trường hiện tại.