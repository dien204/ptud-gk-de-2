@echo off

python -m venv venv

call venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r requirements.txt

python main.py

REM Tạm dừng cửa sổ để bạn xem thông báo hoặc lỗi
pause