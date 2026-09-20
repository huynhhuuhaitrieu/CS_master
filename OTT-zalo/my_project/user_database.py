import psycopg2
from psycopg2 import Error

class UserDatabase:
    def __init__(self, host, dbname, user, password):
        self.db_config = {
            "host": host,
            "dbname": dbname,
            "user": user,
            "password": password
        }
        self.conn = None
        self.cur = None

    def connect(self):
        """Mở kết nối tới database."""
        try:
            self.conn = psycopg2.connect(**self.db_config)
            self.cur = self.conn.cursor()
            print("=> Kết nối database thành công.")
        except Error as e:
            print(f"Lỗi kết nối database: {e}")
            raise

    def disconnect(self):
        """Đóng kết nối."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("=> Đã đóng kết nối database.")

    def create_tables(self):
        """Tạo bảng Users nếu chưa tồn tại."""
        if not self.conn or not self.cur:
            raise Exception("Chưa kết nối database!")
        
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Users (
                id VARCHAR(255) PRIMARY KEY,
                phone_number VARCHAR(255),
                display_name VARCHAR(255),
                dob DATE,
                gender SMALLINT,
                created_at TIMESTAMP,
                photo_url TEXT
            )
        """
        try:
            self.cur.execute(create_table_query)
            self.conn.commit()
            print("=> Khởi tạo bảng Users (nếu chưa có) thành công.")
        except Error as e:
            self.conn.rollback()
            print(f"Lỗi tạo bảng: {e}")

    def insert_user(self, user_data):
        """Thêm user mới vào bảng."""
        if not self.conn or not self.cur:
            raise Exception("Chưa kết nối database!")

        insert_query = """
            INSERT INTO Users (id, phone_number, display_name, dob, gender, created_at, photo_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cur.execute(insert_query, (
                user_data['id'],
                user_data['phone_number'],
                user_data['display_name'],
                user_data['dob'] or None,  # Cho phép NULL nếu không nhập
                user_data['gender'],
                user_data['created_at'],
                user_data['photo_url']
            ))
            self.conn.commit()
            print(f"=> Thêm user '{user_data['display_name']}' thành công!")
        except Error as e:
            self.conn.rollback()
            print(f"Lỗi thêm user: {e}")