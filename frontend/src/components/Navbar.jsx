import './Navbar.css'
import { Link } from 'react-router-dom'

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-logo">
                    <span className="logo-icon">🔐</span>
                    <span className="logo-text">SnapSecure AI</span>
                </Link>

                <ul className="navbar-menu">
                    <li><Link to="/" className="nav-link">Home</Link></li>
                    <li><Link to="/upload" className="nav-link">Upload</Link></li>
                    <li><Link to="/#features" className="nav-link">Features</Link></li>
                </ul>

                <Link to="/upload" className="navbar-cta">
                    Get Started
                </Link>
            </div>
        </nav>
    )
}

export default Navbar
