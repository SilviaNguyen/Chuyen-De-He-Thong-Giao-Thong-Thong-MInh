from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class LicensePlate(BaseModel):
    plate_text: str
class PaymentRequest(BaseModel):
    plate_text: str
    amount: float
@app.post("/process_plate")
async def process_plate(plate: LicensePlate):
    if not plate.plate_text:
        raise HTTPException(status_code=400, detail="Biển số không hợp lệ")
    # Mô phỏng xử lý biển số
    return {"status": "success", "plate": plate.plate_text}

@app.post("/create_payment")
async def create_payment(request: PaymentRequest):
    # Mô phỏng tạo thanh toán
    return {"status": "pending", "transaction_id": "TXN123456"}
