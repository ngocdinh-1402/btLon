# Nhan Dan News - Tự động lấy tin tức lúc 6h sáng

Project Python này sẽ tự động lấy bài viết mới nhất từ trang chủ [Nhân Dân](https://nhandan.vn/)** vào **6h sáng mỗi ngày**, sau đó lưu nội dung bài viết (tiêu đề, tóm tắt, nội dung, ảnh và link) vào file Excel.

---

## Tính năng

- Tự động chạy lúc 6:00 sáng mỗi ngày.
- Lấy bài viết đầu tiên trên trang chủ Dân Trí.
- Trích xuất và lưu:
  - Tiêu đề bài viết
  - Tóm tắt
  - Nội dung HTML
  - Ảnh đầu tiên (nếu có)
  - Link gốc
- Lưu vào file Excel tên theo ngày (VD: `NewsAuto.xlsx`)

---

## Cài đặt

### 1. Clone project

```bash
git clone https://github.com/ngocdinh-1402/btLon_NgocDinh.git
cd NhanDanNews

## Thư viện
pip install -r requirements.txt