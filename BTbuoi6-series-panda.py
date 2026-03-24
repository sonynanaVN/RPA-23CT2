import pandas as pd
#khái niệm panda:
#Pandas là một thư viện mã nguồn mở trong Python được sử dụng để xử lý và phân tích dữ liệu. Nó cung cấp các cấu trúc dữ liệu mạnh mẽ như DataFrame và Series, giúp người dùng dễ dàng thao tác với dữ liệu có cấu trúc như bảng. Pandas hỗ trợ nhiều chức năng như lọc, nhóm, tổng hợp, và trực quan hóa dữ liệu, làm cho nó trở thành một công cụ phổ biến trong lĩnh vực khoa học dữ liệu và phân tích dữ liệu.
#DataFrame là một cấu trúc dữ liệu hai chiều trong Pandas, tương tự như một bảng dữ liệu. Nó có thể chứa nhiều cột với các loại dữ liệu khác nhau (số, chuỗi, ngày tháng, v.v.) và có chỉ số hàng để truy cập dữ liệu. DataFrame cung cấp nhiều phương thức để thao tác với dữ liệu, bao gồm lọc, nhóm, tổng hợp, và trực quan hóa.
#Series là một cấu trúc dữ liệu một chiều trong Pandas, tương tự như một
#mảng hoặc một cột trong DataFrame. Nó có thể chứa các giá trị của cùng một loại dữ liệu và có chỉ số để truy cập dữ liệu. Series cung cấp nhiều phương thức để thao tác với dữ liệu, bao gồm lọc, nhóm, tổng hợp, và trực quan hóa.
#Tạo DataFrame từ dictionary

sinh_vien = pd.Series({
    "Tên": "An",
    "Lớp": "23CT2",
    "Điểm TB": 8.5,
    "Tuổi": 20
})

print(sinh_vien)