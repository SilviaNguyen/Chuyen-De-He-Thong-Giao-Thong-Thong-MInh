import cv2
import pytesseract
from tensorflow.keras.models import load_model
# Tải mô hình đã huấn luyện
model = load_model('license_plate_model.h5')
def detect_license_plate(image_path):
    # Đọc và tiền xử lý hình ảnh
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 100, 200)
    # Phát hiện vùng biển số (đơn giản hóa)
    plate_region = model.predict(edges.reshape(1, *edges.shape, 1))
    # Trích xuất văn bản bằng Tesseract
    plate_text = pytesseract.image_to_string(plate_region, config='--psm 8')
    return plate_text.strip()
# Ví dụ sử dụng
plate_text = detect_license_plate('vehicle_image.jpg')
print(f"Biển số phát hiện: {plate_text}")
