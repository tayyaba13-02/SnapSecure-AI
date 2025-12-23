import './LandingPage.css'
import { Link } from 'react-router-dom'

function LandingPage() {
    return (
        <div className="landing-page">
            {/* Hero Section */}
            <section className="hero-section">
                <div className="hero-content">
                    <div className="hero-badge">
                        <span className="badge-icon">✨</span>
                        <span>AI-Powered Privacy Protection</span>
                    </div>

                    <h1 className="hero-title">
                        Protect Your <span className="gradient-text">Privacy</span><br />
                        Before You Share
                    </h1>

                    SnapSecure AI automatically detects and blurs sensitive information in your screenshots.
                    Share confidently without exposing personal data.

                    <div className="hero-buttons">
                        <Link to="/upload" className="btn-primary">
                            <span>Try It Now</span>
                            <span className="btn-icon">→</span>
                        </Link>
                        <a href="#how-it-works" className="btn-secondary">
                            <span className="btn-icon">▶</span>
                            <span>See How It Works</span>
                        </a>
                    </div>

                    <div className="hero-stats">
                        <div className="stat">
                            <div className="stat-number">4+</div>
                            <div className="stat-label">Data Types</div>
                        </div>
                        <div className="stat">
                            <div className="stat-number">AI</div>
                            <div className="stat-label">Powered</div>
                        </div>
                        <div className="stat">
                            <div className="stat-number">100%</div>
                            <div className="stat-label">Privacy</div>
                        </div>
                    </div>
                </div>

                <div className="hero-visual">
                    <div className="visual-card">
                        <div className="card-header">
                            <div className="card-dots">
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>
                            <span className="card-title">Screenshot Protection</span>
                        </div>
                        <div className="card-content">
                            <div className="detection-item">
                                <span className="detection-icon">📧</span>
                                <span className="detection-text">Email Address</span>
                                <span className="detection-status">✓</span>
                            </div>
                            <div className="detection-item">
                                <span className="detection-icon">📱</span>
                                <span className="detection-text">Phone Number</span>
                                <span className="detection-status">✓</span>
                            </div>
                            <div className="detection-item">
                                <span className="detection-icon">🆔</span>
                                <span className="detection-text">CNIC/SSN Detected</span>
                                <span className="detection-status">✓</span>
                            </div>
                            <div className="detection-item">
                                <span className="detection-icon">💻</span>
                                <span className="detection-text">IP Address Masked</span>
                                <span className="detection-status">✓</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>


            {/* Section Divider */}
            <div className="section-divider"></div>

            <div className="section-intro">
                <p>
                    Explore the cutting-edge capabilities that make SnapSecure AI your trusted partner
                    in protecting sensitive information across all your screenshots.
                </p>
            </div>

            {/* Features Section */}
            <section className="features-section" id="features">
                <div className="section-header">
                    <h2>Powerful Features</h2>
                    <p>
                        Our advanced AI technology combines OCR, machine learning, and computer vision
                        to provide comprehensive privacy protection. Discover the powerful features that
                        make SnapSecure AI the most reliable screenshot security solution.
                    </p>
                </div>

                <div className="features-grid">
                    <div className="feature-card">
                        <div className="feature-icon">🤖</div>
                        <h3>AI Detection</h3>
                        <p>Advanced machine learning algorithms detect sensitive patterns with high accuracy</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon">⚡</div>
                        <h3>Real-Time Processing</h3>
                        <p>Get instant results with our optimized OCR and detection pipeline</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon">🎨</div>
                        <h3>Multiple Redaction Styles</h3>
                        <p>Choose from blur, pixelate, or black-out to hide sensitive information</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon">🔒</div>
                        <h3>100% Private</h3>
                        <p>Your screenshots are processed securely and never stored permanently</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon">📱</div>
                        <h3>Mobile Friendly</h3>
                        <p>Works seamlessly on all devices - desktop, tablet, and mobile</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon">🚀</div>
                        <h3>Easy to Use</h3>
                        <p>Simple drag-and-drop interface - no technical knowledge required</p>
                    </div>
                </div>
            </section>

            {/* Section Divider */}
            <div className="section-divider"></div>
            <div className="section-intro">
                <p>
                    From upload to download, our streamlined process ensures maximum security with
                    minimum effort. See how simple privacy protection can be.
                </p>
            </div>

            {/* How It Works Section */}
            <section className="how-it-works-section" id="how-it-works">
                <div className="section-header">
                    <h2>How It Works</h2>
                    <p>
                        Our intelligent three-step process ensures your sensitive data is protected
                        in seconds. Simply upload, let our AI analyze, and download your secured screenshot.
                        No technical expertise required - it's that easy!
                    </p>
                </div>

                <div className="steps-container">
                    <div className="step">
                        <div className="step-number">1</div>
                        <div className="step-content">
                            <h3>Upload Screenshot</h3>
                            <p>Drag and drop your screenshot or click to browse from your device</p>
                        </div>
                    </div>

                    <div className="step-arrow">→</div>

                    <div className="step">
                        <div className="step-number">2</div>
                        <div className="step-content">
                            <h3>AI Analysis</h3>
                            <p>Our AI scans for emails, phone numbers, and other sensitive personal data</p>
                        </div>
                    </div>

                    <div className="step-arrow">→</div>

                    <div className="step">
                        <div className="step-number">3</div>
                        <div className="step-content">
                            <h3>Download Protected</h3>
                            <p>Get your secured screenshot with all sensitive information blurred</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* Section Divider */}
            <div className="section-divider"></div>
            <div className="section-intro">
                <p>
                    Our AI recognizes a wide range of sensitive data patterns. Here's everything
                    we automatically detect and protect in your screenshots.
                </p>
            </div>

            {/* Protected Data Types */}
            <section className="data-types-section">
                <div className="section-header">
                    <h2>What We Protect</h2>
                    <p>
                        SnapSecure AI detects and protects 4+ types of sensitive information using
                        advanced pattern recognition and machine learning. From personal
                        identifiers to contact info, we've got you covered.
                    </p>
                </div>

                <div className="data-types-grid">
                    <div className="data-type">
                        <span className="data-icon">📧</span>
                        <span className="data-name">Email Addresses</span>
                    </div>
                    <div className="data-type">
                        <span className="data-icon">📱</span>
                        <span className="data-name">Phone Numbers</span>
                    </div>
                    <div className="data-type">
                        <span className="data-icon">🆔</span>
                        <span className="data-name">SSN/CNIC</span>
                    </div>
                    <div className="data-type">
                        <span className="data-icon">💻</span>
                        <span className="data-name">IP Addresses</span>
                    </div>
                </div>
            </section>

            {/* Section Divider */}
            <div className="section-divider"></div>
            <div className="section-intro">
                <p>
                    Join thousands of users who trust SnapSecure AI to keep their sensitive
                    information safe. Start protecting your privacy today!
                </p>
            </div>

            {/* CTA Section */}
            <section className="cta-section">
                <div className="cta-content">
                    <h2>Ready to Protect Your Privacy?</h2>
                    <p>Start securing your screenshots in seconds</p>
                    <Link to="/upload" className="cta-button">
                        Get Started Now
                        <span className="btn-icon">→</span>
                    </Link>
                </div>
            </section>
        </div>
    )
}

export default LandingPage
