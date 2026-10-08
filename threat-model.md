# Threat Model - Function json_search()

## 1. Actors / Roles & Mục đích
* **Admin:** Được phép gọi hàm để tìm bất kỳ thông tin nào cần thiết, trả về toàn bộ thông tin.
* **Operator:** Được phép gọi hàm để truy cập managementIpAddress, trả về các thông tin cần thiết để làm việc.
* **Viewer:** Được phép gọi hàm để xem thông tin tóm tắt về sự cố (issueSummary), chỉ trả về thông tin trên.
* **Other:** Không được gọi hàm.

## 2. Sensitive Assets (Tài sản nhạy cảm)
* **API Keys:** Tài sản quan trọng nhất (tối mật), chỉ có Admin được truy cập.
* **Management IP Address:** Tài sản quan trọng cao, chỉ Admin và Operator được quyền truy cập.
* **Issue Summary:** Tài sản quan trọng thấp, cả Admin, Operator và Viewer đều có quyền truy cập.
* **Các trường còn lại:** Có mức quan trọng trung bình.

## 3. Trust Boundaries (Ranh giới tin cậy bị bỏ qua)
* **Bỏ qua hệ thống phân quyền:** Không kiểm tra quyền khi trả kết quả => toàn bộ hệ thống phân quyền truy cập bị bỏ qua, bỏ qua hoàn toàn mọi trust boundary.
* **Bỏ qua ranh giới xác thực:** Tin tưởng người gọi hàm dùng đúng role mà không đối chiếu chính sách.
* **Thiếu mặc định an toàn:** Có thể gán role mặc định rộng hơn mong muốn => bỏ qua ranh giới xác thực.
* **Mất toàn vẹn dữ liệu:** Hàm có thể làm thay đổi dữ liệu đầu vào trong quá trình đệ quy.

## 4. Threats (Mối đe dọa)
* **Information Disclosure:** Người dùng khai thác việc thiếu kiểm tra quyền để lấy `apiKey` => lấy được toàn quyền truy cập hệ thống mạng.
* **Elevation of Privilege:** Người dùng giả mạo `role=admin` => có quyền ngang Admin dù thực tế không được cấp.
* **Elevation of Privilege:** Người dùng gọi hàm không truyền `role` => có khả năng nhận được `apiKey` / `managementIpAddress`.
