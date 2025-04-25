import React, { useState } from 'react';
function TollManagementApp() {
  const [plate, setPlate] = useState('');
  const [message, setMessage] = useState('');
  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:8000/process_plate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plate_text: plate }),
      });
      const data = await response.json();
      setMessage(`Biển số đã xử lý: ${data.plate}`);
    } catch (error) {
      setMessage('Lỗi khi xử lý biển số');
    }
  };
  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Quản Lý Thu Phí</h1>
      <input
        type="text"
        value={plate}
        onChange={(e) => setPlate(e.target.value)}
        className="border p-2 w-full mb-2"
        placeholder="Nhập biển số xe"
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-500 text-white p-2 w-full rounded"
      >
        Gửi
      </button>
      {message && <p className="mt-2">{message}</p>}
    </div>
  );
}

export default TollManagementApp;
