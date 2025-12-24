import { useState } from 'react'
import './UploadPage.css'

function UploadPage() {
    const [selectedFile, setSelectedFile] = useState(null)
    const [isDragging, setIsDragging] = useState(false)
    const [isProcessing, setIsProcessing] = useState(false)
    const [result, setResult] = useState(null)

    const handleDragOver = (e) => {
        e.preventDefault()
        setIsDragging(true)
    }

    const handleDragLeave = () => {
        setIsDragging(false)
    }

    const handleDrop = (e) => {
        e.preventDefault()
        setIsDragging(false)
        const file = e.dataTransfer.files[0]
        if (file && file.type.startsWith('image/')) {
            setSelectedFile(file)
            setResult(null)
        }
    }

    const handleFileSelect = (e) => {
        const file = e.target.files[0]
        if (file) {
            setSelectedFile(file)
            setResult(null)
        }
    }

    const handleAnalyze = async () => {
        if (!selectedFile) return

        setIsProcessing(true)
        const formData = new FormData()
        formData.append('file', selectedFile)

        const apiUrl = import.meta.env.VITE_API_URL || (import.meta.env.DEV ? 'http://localhost:8001' : '')
        try {
            const response = await fetch(`${apiUrl}/analyze`, {
                method: 'POST',
                body: formData,
            })
            const data = await response.json()
            setResult(data)
        } catch (error) {
            console.error('Error:', error)
            setResult({ error: 'Failed to analyze screenshot' })
        } finally {
            setIsProcessing(false)
        }
    }

    const handleReset = () => {
        setSelectedFile(null)
        setResult(null)
        setIsProcessing(false)
    }

    const handleDownload = async () => {
        if (!result || !result.processed_url) return

        try {
            const response = await fetch(result.processed_url)
            const blob = await response.blob()
            const url = window.URL.createObjectURL(blob)
            const a = document.createElement('a')
            a.href = url
            a.download = `${selectedFile.name.split('.')[0]}_protected.${selectedFile.name.split('.').pop()}`
            document.body.appendChild(a)
            a.click()
            window.URL.revokeObjectURL(url)
            document.body.removeChild(a)
        } catch (error) {
            console.error('Download failed:', error)
            // Fallback to direct link if fetch fails
            window.open(result.processed_url, '_blank')
        }
    }

    return (
        <div className="upload-page">
            <div className="upload-container">
                {/* Page Header */}
                <div className="page-header">
                    <h1>Secure Your Screenshot</h1>
                    <p>Upload your screenshot and let our AI protect your sensitive information</p>
                </div>

                {/* Upload Area */}
                <div className="upload-wrapper">
                    {!selectedFile ? (
                        <div
                            className={`upload-zone ${isDragging ? 'dragging' : ''}`}
                            onDragOver={handleDragOver}
                            onDragLeave={handleDragLeave}
                            onDrop={handleDrop}
                        >
                            <div className="upload-icon-large">📸</div>
                            <h2>Drop your screenshot here</h2>
                            <p className="upload-subtitle">or click the button below to browse</p>

                            <input
                                type="file"
                                accept="image/*"
                                onChange={handleFileSelect}
                                className="file-input-hidden"
                                id="file-upload"
                            />
                            <label htmlFor="file-upload" className="upload-btn">
                                <span className="btn-icon">📁</span>
                                Choose File
                            </label>

                            <div className="upload-info">
                                <p>Supported formats: JPG, PNG, GIF, WebP</p>
                                <p>Maximum size: 10MB</p>
                            </div>
                        </div>
                    ) : (
                        <div className="preview-section">
                            {/* Image Preview */}
                            <div className="image-preview-card">
                                <div className="preview-header">
                                    <h3>Original Screenshot</h3>
                                    <button className="reset-btn" onClick={handleReset}>
                                        ✕ Remove
                                    </button>
                                </div>
                                <div className="preview-image-wrapper">
                                    <img
                                        src={URL.createObjectURL(selectedFile)}
                                        alt="Preview"
                                        className="preview-img"
                                    />
                                </div>
                                <div className="file-details">
                                    <div className="detail-item">
                                        <span className="detail-label">Filename:</span>
                                        <span className="detail-value">{selectedFile.name}</span>
                                    </div>
                                    <div className="detail-item">
                                        <span className="detail-label">Size:</span>
                                        <span className="detail-value">{(selectedFile.size / 1024).toFixed(2)} KB</span>
                                    </div>
                                    <div className="detail-item">
                                        <span className="detail-label">Type:</span>
                                        <span className="detail-value">{selectedFile.type}</span>
                                    </div>
                                </div>
                            </div>

                            {/* Action Panel */}
                            <div className="action-panel">
                                <h3>Protection Options</h3>

                                <div className="options-grid">
                                    <div className="option-card active">
                                        <div className="option-icon">🔍</div>
                                        <div className="option-info">
                                            <h4>Auto Detect</h4>
                                            <p>Our AI scans for emails, phone numbers, and other sensitive personal data</p>
                                        </div>
                                    </div>

                                    <div className="option-card">
                                        <div className="option-icon">🌫️</div>
                                        <div className="option-info">
                                            <h4>Blur Style</h4>
                                            <p>Gaussian blur effect</p>
                                        </div>
                                    </div>
                                </div>

                                <button
                                    className="analyze-btn"
                                    onClick={handleAnalyze}
                                    disabled={isProcessing}
                                >
                                    {isProcessing ? (
                                        <>
                                            <span className="spinner"></span>
                                            Analyzing...
                                        </>
                                    ) : (
                                        <>
                                            <span className="btn-icon">🔐</span>
                                            Analyze & Protect
                                        </>
                                    )}
                                </button>

                                {result && (
                                    <div className="result-card">
                                        <h4>Analysis Complete 🛡️</h4>

                                        {result.error ? (
                                            <div className="error-message">
                                                ❌ {result.error}
                                            </div>
                                        ) : (
                                            <div className="result-content">
                                                <div className="processed-image-container">
                                                    <h5>Protected Screenshot</h5>
                                                    <img
                                                        src={result.processed_url}
                                                        alt="Protected Screenshot"
                                                        className="processed-img"
                                                    />
                                                    <button
                                                        onClick={handleDownload}
                                                        className="download-link-btn"
                                                        style={{ width: '100%', cursor: 'pointer', border: 'none' }}
                                                    >
                                                        ⬇ Download Protected Image
                                                    </button>
                                                </div>

                                                <div className="detections-list">
                                                    <h5>Detected Sensitive Data</h5>
                                                    {result.detections && result.detections.length > 0 ? (
                                                        <ul>
                                                            {result.detections.map((item, index) => (
                                                                <li key={index} className="detection-result-item">
                                                                    <span className="detection-type">{item.type}</span>
                                                                    {/* <span className="detection-value">{item.text}</span> */}
                                                                    <span className="detection-coord">
                                                                        (x:{item.box.left}, y:{item.box.top})
                                                                    </span>
                                                                </li>
                                                            ))}
                                                        </ul>
                                                    ) : (
                                                        <p className="no-detections">No sensitive data found.</p>
                                                    )}
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        </div>
                    )}
                </div>

                {/* Features Info */}
                <div className="features-info">
                    <div className="info-card">
                        <span className="info-icon">⚡</span>
                        <div>
                            <h4>Fast Processing</h4>
                            <p>Results in seconds</p>
                        </div>
                    </div>
                    <div className="info-card">
                        <span className="info-icon">🔒</span>
                        <div>
                            <h4>100% Secure</h4>
                            <p>Files not stored</p>
                        </div>
                    </div>
                    <div className="info-card">
                        <span className="info-icon">🎯</span>
                        <div>
                            <h4>High Accuracy</h4>
                            <p>AI-powered detection</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default UploadPage
