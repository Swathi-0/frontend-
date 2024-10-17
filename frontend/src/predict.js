import React, { useState } from 'react';
import axios from 'axios';

function Predict() {
    const [nirVoltage, setNirVoltage] = useState('');
    const [bpm, setBpm] = useState('');
    const [spo2, setSpo2] = useState('');
    const [predictedGlucose, setPredictedGlucose] = useState(null);

    const handlePredict = async () => {
        const token = localStorage.getItem('token');
        if (!token) {
            alert('You must be logged in to make a prediction.');
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', {
                nirVoltage: parseFloat(nirVoltage),
                bpm: parseFloat(bpm),
                spo2: parseFloat(spo2)
            }, {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            });

            setPredictedGlucose(response.data.predictedGlucose);
        } catch (error) {
            console.error('Error predicting glucose level:', error);
        }
    };

    return (
        <div>
            <h2>Glucose Level Prediction</h2>
            <input 
                type="number" 
                value={nirVoltage} 
                onChange={(e) => setNirVoltage(e.target.value)} 
                placeholder="Enter NIR Voltage" 
            />
            <input 
                type="number" 
                value={bpm} 
                onChange={(e) => setBpm(e.target.value)} 
                placeholder="Enter BPM" 
            />
            <input 
                type="number" 
                value={spo2} 
                onChange={(e) => setSpo2(e.target.value)} 
                placeholder="Enter SpO2" 
            />
            <button onClick={handlePredict}>Predict</button>
            {predictedGlucose !== null && (
                <div>
                    <h2>Predicted Glucose Level: {predictedGlucose}</h2>
                </div>
            )}
        </div>
    );
}

export default Predict;
