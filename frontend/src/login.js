import React, { useState } from 'react';
import axios from 'axios';
import './Login.css'; 



function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/login', {
                username,
                password
            });
            // Store JWT token in local storage
            localStorage.setItem('token', response.data.access_token);
            // Redirect to predict page
            window.location.href = '/predict';
        } catch (error) {
            setErrorMessage('Invalid username or password');
        }
    };

    return (
        <div className="login-container">
                <div className="col-6">
                    <div className="form-container">
                        <h2>Sign in with</h2>
                        <div className="social-buttons">
                            <button className="btn btn-primary">Facebook</button>
                            <button className="btn btn-info">Twitter</button>
                            <button className="btn btn-danger">Google</button>
                        </div>
                        <p><center>OR</center></p>
                        <form onSubmit={handleLogin}>
                            <input 
                                type="text" 
                                placeholder="Username" 
                                value={username} 
                                onChange={(e) => setUsername(e.target.value)} 
                                required 
                            />
                            <input 
                                type="password" 
                                placeholder="Password" 
                                value={password} 
                                onChange={(e) => setPassword(e.target.value)} 
                                required 
                            />
                            <div className="checkbox-container">
                                <a href="/forgot-password" className="forgot-password">Forgot password?</a>
                            </div>
                            <br></br>
                            <button type="submit" className="login-button">Login</button>
                            {errorMessage && <p>{errorMessage}</p>}
                        </form>
                        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
                    </div>
                </div>
            
            
        </div>
    );
}

export default Login;
