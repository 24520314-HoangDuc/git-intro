# Security Requirements - Function json_search()

1. **Role-Based Access Control (RBAC):**
   Hàm chỉ trả về trường dữ liệu cho các role nằm trong danh sách được phép truy cập (theo policy). Nếu role của người gọi không có đủ quyền truy cập, hàm bắt buộc trả về mảng rỗng `[]`.

2. **Safe Default (Mặc định an toàn):**
   Khi role không được chỉ định truyền vào hàm, mặc định gán quyền là `viewer`.

3. **Data Integrity (Toàn vẹn dữ liệu):**
   Hàm thực hiện tìm kiếm đệ quy nhưng không được làm thay đổi cấu trúc hoặc dữ liệu gốc ban đầu.
