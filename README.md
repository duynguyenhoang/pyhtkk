CÔNG CỤ HỖ TRỢ QUYẾT TOÁN THUẾ TNCN
----------------------------

Hiện tại thao tác khai thuế TNCN đòi hỏi các phần mềm chạy trên nền Windows gây ra không ít phiền toái cho cho anh em làm nghề code - chủ yếu dùng Linux và Macos. Mục đích công cụ ra đời để giải quyết việc đơn giản đó.

> Công cụ này tạo ra nhằm mục đích cho cá nhân sử dụng, không có bất liên quan gì đến cơ quan quản lý thuế.

# Yêu cầu và cài đặt

Python 3

```
git clone git@github.com:duynguyenhoang/pyhtkk.git
cd pyhtkk
pip install -r requirements.txt
```

# Chức năng chính

* [x] Đọc hồ sơ thuế điện tử và export ra file tương thích **iTaxViewer** - Mẫu số 02/QTT-TNCN
* [ ] Hỗ trợ khai báo người phụ thuộc
* [ ] TODO Hỗ trợ tự động kê khai thế tương thích với **iHTKK**

## Đọc hồ sơ thuế điện từ

Công cụ này giúp bạn tạo file docx từ file xml có được từ bước khai thuế TNCN trực tuyến.

Phiên bản hiện tại tương thích với phiên bản **iTaxViewer1.6.3**

```bash
python pyhtkk/py_tax_viewer.py YOUR_HTKK_OR_ONLINE_OUTPUT.xml
```

Công cụ sẽ tự động tạo ra file `.docx` và lưu trữ vào cùng thư mục với file `.xml`

**Example**

```bash
python pyhtkk/py_tax_viewer.py ./HCM-1234567890-02QT-9876543-L69.xml
```
