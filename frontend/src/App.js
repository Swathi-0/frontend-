import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Signup from './signup';
import Login from './login';
import Predict from './predict';
import Navbar from './Navbar';
import Footer from './Footer';

function App() {
    return (
        <Router>
            <Navbar /> {/* Add this line */}
            <div>
                <br>
                </br>
                <br>
                </br>
                <br>
                </br>
                <h1>VitaVue - Your Ultimate  Health Moniter</h1>
                <Routes>
                    <Route path="/signup" element={<Signup />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/predict" element={<Predict />} />
                    {/* Redirect from the root path to the login page */}
                    <Route path="/" element={<Navigate to="/login" replace />} />
                </Routes>
                <Footer />
            </div>
        </Router>
    );
}

export default App;
