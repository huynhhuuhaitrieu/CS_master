from user_database import UserDatabase
from datetime import datetime

def get_user_input():
    print("\n--- NHẬP THÔNG TIN USER MỚI ---")
    user_id = input("ID (vd: U001): ").strip()
    phone_number = input("Số điện thoại: ").strip()
    display_name = input("Tên hiển thị: ").strip()
    dob = input("Ngày sinh (YYYY-MM-DD, nhấn Enter để bỏ qua): ").strip()
    
    try:
        gender_input = input("Giới tính (1: Nam, 2: Nữ, 0: Khác): ").strip()
        gender = int(gender_input) if gender_input else 0
    except ValueError:
        print("Sai định dạng giới tính, mặc định là 0 (Khác).")
        gender = 0

    photo_url = input("Link ảnh (Photo URL): ").strip()
    
    # Lấy thời gian hiện tại cho created_at
    created_at = datetime.now()

    return {
        "id": user_id,
        "phone_number": phone_number,
        "display_name": display_name,
        "dob": dob,
        "gender": gender,
        "created_at": created_at,
        "photo_url": photo_url
    }

if __name__ == "__main__":
    # Khởi tạo đối tượng db với cấu hình PostgreSQL của bạn
    db = UserDatabase(
        host="localhost", 
        dbname="voting", 
        user="postgres", 
        password="postgres"
    )

    try:
        # 1. Kết nối DB
        db.connect()
        
        # 2. Đảm bảo bảng đã được tạo
        db.create_tables()
        
        # 3. Lấy dữ liệu từ input của người dùng
        user_data = get_user_input()
        
        # 4. Insert dữ liệu nếu có ID
        if user_data['id']:
            db.insert_user(user_data)
        else:
            print("Lỗi: Bắt buộc phải có ID!")

    except Exception as e:
        print(f"Chương trình gặp lỗi: {e}")
    finally:
        # Đóng kết nối an toàn
        db.disconnect()