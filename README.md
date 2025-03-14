1. Thông tin cá nhân

 - Họ và tên: Nguyễn Thị Mỹ Duyên

 - MSSV: 22640511

 - Email: nguyenthimyduyen031200@gmail.com


2. Mô tả Project

Ứng dụng "Quản lý Công việc" giúp người dùng theo dõi và quản lý danh sách công việc của họ. Hệ thống bao gồm hai tác nhân:

 - Admin: Quản lý danh sách công việc, tình trạng hoàn thành, và xóa công việc.

 - User: Thêm, chỉnh sửa, và theo dõi tình trạng công việc.

Mỗi công việc sẽ bao gồm:

 - Task: Tên công việc

 - Status: Trạng thái hoàn thành (Pending/Done)

 - Created: Ngày tạo công việc

 - Finished: Ngày hoàn thành

3. Hướng dẫn cài đặt

 - Clone repository

$ git clone https://github.com/[your-github-username]/ptud-gk-de-2.git
$ cd ptud-gk-de-2

 - Cài đặt môi trường

Tạo môi trường ảo và cài đặt các package cần thiết:

$ python -m venv venv

$ source venv/bin/activate  # Trên macOS/Linux

$ venv\Scripts\activate    # Trên Windows

$ pip install -r requirements.txt

 - Cấu hình cơ sở dữ liệu

Tạo file .env và thiết lập các biến môi trường:

FLASK_APP=app.py

FLASK_ENV=development

DATABASE_URL=sqlite:///tasks.db

Khởi tạo cơ sở dữ liệu:

$ flask db init

$ flask db migrate -m "Initial migration."

$ flask db upgrade

Chạy ứng dụng

$ flask run


4. Mở trình duyệt và truy cập: http://127.0.0.1:5000

