import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';


function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-container">
                <a className="navbar-brand" href="#">VitaVue</a>
                <ul className="navbar-menu">
                    <li className="navbar-item">
                        <a className="navbar-link" href="/login">Login</a>
                    </li>
                    <li className="navbar-item">
                        <a className="navbar-link" href="/signup">Sign Up</a>
                    </li>
                </ul>
            </div>
        </nav>
    );
}


export default Navbar;

