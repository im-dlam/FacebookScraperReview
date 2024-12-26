
# Facebook Review Scraper

## Mô tả

Ứng dụng cung cấp API để scrape đánh giá từ các trang doanh nghiệp trên Facebook. API hỗ trợ các phương thức GET và POST nhận URL và trả về dữ liệu các đánh giá.

## Yêu cầu hệ thống

1. **Python**: Phiên bản >= 3.7.
2. **Thư viện cần thiết**:
   - Flask
   - requests
   - beautifulsoup4

# Hướng dẫn sử dụng

## Cài đặt các thư viện

Chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install Flask requests beautifulsoup4
```

## Khởi động server

Chạy lệnh sau để khởi động server:

```bash
python main.py
```

## Sử dụng API

### Gửi yêu cầu GET

```bash
curl "http://127.0.0.1:5076/FacebookScraper?url=https://www.facebook.com/somebusiness/reviews"
```

### Gửi yêu cầu POST

```bash
curl -X POST http://127.0.0.1:5076/FacebookScraper \
-H "Content-Type: application/json" \
-d '{"url": "https://www.facebook.com/somebusiness/reviews"}'
```

## Kết quả API

### Phản hồi thành công

```json
[
    {
        "refId": "123456789",
        "stars": 5,
        "name": "John Doe",
        "profile": "https://www.facebook.com/profile/123456",
        "date": "2024-12-26T00:00:00",
        "order": 1,
        "content": "Great service!",
        "replies": [
            {
                "refId": "987654321",
                "name": "Jane Smith",
                "date": "2024-12-26T01:00:00",
                "order": 1,
                "content": "I agree!"
            }
        ]
    }
]
```

### Phản hồi lỗi

#### Thiếu URL

```json
{
    "error": "No URL provided."
}
```

#### Giới hạn thời gian (1 yêu cầu/giây cho mỗi URL):

```json
{
    "error": "Requests are limited to 1 per second per URL."
}
```

## Lưu ý

- **Cấu hình JSON**: Khi sử dụng POST, dữ liệu phải được gửi dưới dạng JSON.
- **Kết nối Internet**: Đảm bảo kết nối Internet ổn định.
- **Giới hạn thời gian**: API chỉ hỗ trợ tối đa 1 yêu cầu/giây cho mỗi URL.

## Hỗ trợ

Nếu gặp lỗi, vui lòng:

1. Kiểm tra cấu hình Python và thư viện.
2. Đảm bảo URL cung cấp là hợp lệ.
3. Xem lại logs nếu server báo lỗi.
