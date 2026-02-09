import numpy as np
from sklearn.neighbors import KNeighborsClassifier

str_input = input("Enter values for chieu cao, can nang (separated by space): ")
a, b = map(int, str_input.split())
# 1. Chuẩn bị dữ liệu (Dữ liệu mẫu)
# X: Đặc trưng [Chiều cao (cm), Cân nặng (kg)]
X = np.array([
    [150, 45], [155, 48], [160, 50],  # Nhóm áo Size S (Nhỏ)
    [175, 75], [180, 80], [178, 78]   # Nhóm áo Size L (Lớn)
])

# y: Nhãn (Label) tương ứng
y = np.array(['Size S', 'Size S', 'Size S', 'Size L', 'Size L', 'Size L'])

# 2. Khởi tạo mô hình
# n_neighbors=3: Chọn 3 "hàng xóm" gần nhất để bỏ phiếu
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# 3. Huấn luyện mô hình (Fit)
knn.fit(X, y)

# 4. Dự đoán một dữ liệu mới
# Một người mới cao 158cm, nặng 49kg -> Sẽ thuộc nhóm nào?
nguoi_moi = np.array([[a, b]])

ket_qua = knn.predict(nguoi_moi)

print(f"Dữ liệu mới (Cao, Nặng): {nguoi_moi[0]}")
print(f"Kết quả dự đoán với k={k}: {ket_qua[0]}")