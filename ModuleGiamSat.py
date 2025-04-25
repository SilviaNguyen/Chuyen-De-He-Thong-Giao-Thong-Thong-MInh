from prometheus_client import Counter, generate_latest
from flask import Flask, Response
app = Flask(__name__)
# Xác định số liệu
transactions_total = Counter('transactions_total', 'Tổng số giao dịch đã xử lý', ['status'])
@app.route('/metrics')
def metrics():
    # Cập nhật số liệu (ví dụ)
    transactions_total.labels(status='success').inc()
    return Response(generate_latest(), mimetype='text/plain')
if __name__ == '__main__':
    app.run(port=9100)
