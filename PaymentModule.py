import requests
import hashlib
import time
def create_payment(amount, order_info, plate_number):
    url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
    params = {
        'vnp_Amount': amount * 100,  # Chuyển sang đơn vị nhỏ nhất
        'vnp_Command': 'pay',
        'vnp_CreateDate': time.strftime('%Y%m%d%H%M%S'),
        'vnp_CurrCode': 'VND',
        'vnp_IpAddr': '127.0.0.1',
        'vnp_Locale': 'vn',
        'vnp_OrderInfo': f"{order_info} - Biển số: {plate_number}",
        'vnp_OrderType': 'toll',
        'vnp_ReturnUrl': 'http://yourdomain.com/payment_callback',
        'vnp_TmnCode': 'YOUR_TMN_CODE',
        'vnp_TxnRef': f"TXN{int(time.time())}",
        'vnp_Version': '2.1.0',
    }
    # Tạo chữ ký bảo mật (đơn giản hóa)
    secret_key = 'YOUR_SECRET_KEY'
    data = '&'.join([f"{k}={v}" for k, v in sorted(params.items())])
    params['vnp_SecureHash'] = hashlib.sha256((data + secret_key).encode()).hexdigest()
    response = requests.get(url, params=params)
    return response.url
# Ví dụ sử dụng
payment_url = create_payment(100000, 'Thanh toán phí cầu đường', '1234-AB')
print(f"URL thanh toán: {payment_url}")
