import './Footer.css'
import { Link } from 'react-router-dom'

function Footer() {
    const currentYear = new Date().getFullYear()

    return (
        <footer className="footer">
            <div className="footer-container">
                {/* Top Section */}
                <div className="footer-top">
                    <div className="footer-brand">
                        <div className="footer-logo">
                            <span className="logo-icon">🔐</span>
                            <span className="logo-text">SnapSecure AI</span>
                        </div>
                        <p className="footer-tagline">
                            AI-powered screenshot privacy protection
                        </p>
                    </div>

                    <div className="footer-links">
                        <div className="footer-column">
                            <h4>Product</h4>
                            <Link to="/">Home</Link>
                            <Link to="/upload">Upload</Link>
                            <a href="/#features">Features</a>
                            <a href="/#how-it-works">How It Works</a>
                        </div>
                    </div>
                </div>

                {/* Security Section */}
                <div className="footer-security" id="security">
                    <div className="security-header">
                        <span className="security-icon">🛡️</span>
                        <h3>Security & Privacy</h3>
                    </div>
                    <div className="security-badges">
                        <div className="security-badge">
                            <span className="badge-icon">🔒</span>
                            <div className="badge-info">
                                <h5>Data Privacy</h5>
                                <p>100% Secure Processing</p>
                            </div>
                        </div>
                        <div className="security-badge">
                            <span className="badge-icon">🚫</span>
                            <div className="badge-info">
                                <h5>No Storage</h5>
                                <p>Files deleted instantly</p>
                            </div>
                        </div>
                        <div className="security-badge">
                            <span className="badge-icon">🤖</span>
                            <div className="badge-info">
                                <h5>AI Compliance</h5>
                                <p>Transparent & Secure</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Bottom Section */}
                <div className="footer-bottom">
                    <p>&copy; {currentYear} SnapSecure AI. All rights reserved.</p>
                    <p className="footer-credit">
                        Built with ❤️ by Team SnapSecure
                    </p>
                </div>
            </div>
        </footer>
    )
}

export default Footer
