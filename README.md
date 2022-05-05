## :zero: Hướng dẫn sử dụng git
- **Bước 1**: Vào bên trong thư mục của dự án và chạy lệnh khởi tạo:
```c
$ git init
```
- **Bước 2** : Thêm tất cả các file vào trong stagging.
```c
$ git add .
``` 
![](https://i.imgur.com/8xDWj1v.png)
- Kiểm tra các file được thêm vào chưa:
```
$ git status
```
- **Bước 4**: Dán nhãn cho source
```
$ git commit -m "message"
```
![](https://i.imgur.com/pMAyz46.png)

**Bước 5**: Tạo repo trên github
- Chọn vào **New** để tạo một Repo trên github.
![](https://i.imgur.com/YdcwaqA.png)
- Đặt tên cho Repo theo nhu cầu riêng, chú ý cú pháp: không có dấu cách, ký tự đặc biệt.
![](https://i.imgur.com/mi0CDWy.png)
- Nhấn **Create repository**
- Copy câu lệnh như hình sau:
![](https://i.imgur.com/KzMDcO3.png)
- Paste lệnh vừa copy vào terminal của Vscode -> Enter.
![](https://i.imgur.com/IW9nMhF.png)

**Bước 6**: Đẩy toàn bộ code từ máy cá nhân lên github.
```
$ git push
```
Nếu là lần đầu tiên push code lên repo thì chạy lếnh sau:
```
$ git push -u origin master
```
- Sau đó chọn **Sign in with your browser**.

![](https://i.imgur.com/fPvc3jM.png)
- Kiểm tra kết quả -> reload lại github.

![](https://i.imgur.com/9uLs0Yq.png)

## :one: Chuẩn bị
- Tạo mội trường python

 ```c
 $ python -m venv venv .\venv\Scripts\activate 
  ```
 :warning: Tạo file `.gitignore` và điền tên thư mục môi trường python vào file vừa tạo 
## :two: Tiến hành cài đặt
-  **Bước 1**: Cài Fastapi và Uvicorn bằng pip:
 ```c
 $ pip install fastapi pip install uvicorn 
  ``` 
  - **Bước 2**: Code một số tính request đơn giản tại file **main.py**.
  - **Bước 3**: Chạy server bằng lệnh sau:
  ```c
  $ uvicorn main:app --reload # Mini_server
  ```