FROM python:3.9-slim

# Tích hợp uv vào container để cài đặt thư viện siêu tốc
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

# Chỉ copy file pyproject.toml (và file lock nếu có) để tận dụng cache của Docker
COPY pyproject.toml ./
# COPY uv.lock ./

# Dùng uv để đọc và cài đặt trực tiếp các thư viện từ pyproject.toml vào hệ thống
RUN uv pip install --system -r pyproject.toml

# Copy mã nguồn Python vào container
COPY user_database.py test_user_database.py ./

CMD ["python", "test_user_database.py"]