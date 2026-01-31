"""
UNIFIED SERVER FOR HONEYPOT API + ALL HTML FILES
=================================================

This server runs everything in one place:
- FastAPI backend with honeypot endpoints
- Serves all HTML files (hackthon.html, api_tester.html, combined.html)
- Single server on port 8000

Usage:
    python server.py

Access:
    API:     http://localhost:8000/api/...
    Main UI: http://localhost:8000/app
    Tester:  http://localhost:8000/tester
    Combined: http://localhost:8000/combined
    API Docs: http://localhost:8000/docs
"""

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from pathlib import Path
import secrets
import random
import asyncio
import uvicorn

# ============================================
# FASTAPI APPLICATION SETUP
# ============================================

app = FastAPI(
    title="Agentic Honeypot API",
    description="AI-powered honeypot for fraud detection and scam analysis",
    version="4.0 - Unified Server",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# CONFIGURATION
# ============================================

VALID_API_KEY = "honeypot123"
interaction_logs = []

# Get the directory where this script is located
BASE_DIR = Path(__file__).resolve().parent

# ============================================
# REQUEST/RESPONSE MODELS
# ============================================

class LoginRequest(BaseModel):
    username: str
    password: str

class IVRRequest(BaseModel):
    caller_id: str
    input: str

class KYCRequest(BaseModel):
    aadhaar: str
    pan: str

# ============================================
# AUTHENTICATION MIDDLEWARE
# ============================================

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key or x_api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=401,
            detail={"error": "Unauthorized"}
        )
    return x_api_key

# ============================================
# LOGGING UTILITIES
# ============================================

async def log_interaction(request: Request, endpoint: str, payload: Dict[str, Any]):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip_address": request.client.host,
        "endpoint": endpoint,
        "payload_summary": str(payload)[:200],
        "user_agent": request.headers.get("user-agent", "Unknown")
    }
    interaction_logs.append(log_entry)
    print(f"[HONEYPOT LOG] {log_entry}")

# ============================================
# AI-LIKE BEHAVIOR ANALYSIS
# ============================================

def analyze_login_behavior(username: str, password: str) -> float:
    risk_score = 0.80
    if len(password) < 6:
        risk_score += 0.10
    if password.lower() in ['password', '123456', 'admin', 'test']:
        risk_score += 0.08
    if username.lower() in ['admin', 'test', 'root', 'user']:
        risk_score += 0.05
    risk_score += random.uniform(-0.03, 0.03)
    return min(risk_score, 0.99)

def analyze_kyc_data(aadhaar: str, pan: str) -> float:
    risk_score = 0.85
    if aadhaar.startswith("0000") or aadhaar.startswith("1111"):
        risk_score += 0.10
    if pan.startswith("AAA") or pan.startswith("XXX"):
        risk_score += 0.08
    if not aadhaar.isdigit() or len(aadhaar) != 12:
        risk_score += 0.05
    risk_score += random.uniform(-0.02, 0.04)
    return min(risk_score, 0.99)

def generate_ivr_response(caller_input: str) -> str:
    responses = [
        "Your account is temporarily blocked. Press 9 to continue.",
        "Please hold while we verify your identity. This may take 2-3 minutes.",
        "Your request is being processed. Press 1 for English, 2 for Hindi.",
        "For security reasons, we need to authenticate you. Press # to proceed.",
        "Your transaction is pending approval. Please wait for confirmation SMS.",
        "System is currently under maintenance. Please try again in 5 minutes.",
        "Your card has been temporarily locked. Press 0 to speak with an agent.",
        "Thank you for calling. Your estimated wait time is 15 minutes."
    ]
    
    lower_input = caller_input.lower()
    if any(word in lower_input for word in ['block', 'locked', 'suspend']):
        return responses[0]
    elif any(word in lower_input for word in ['help', 'speak', 'agent']):
        return responses[6]
    else:
        return random.choice(responses)

# ============================================
# HTML FILE SERVING ENDPOINTS
# ============================================

@app.get("/")
async def root():
    """Root endpoint - Landing page with navigation"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Agentic Honeypot - Unified Server</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #fff;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                max-width: 900px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            .subtitle {
                font-size: 1.2em;
                opacity: 0.9;
                margin-bottom: 30px;
            }
            .status {
                display: inline-block;
                background: #10b981;
                padding: 8px 20px;
                border-radius: 25px;
                font-weight: bold;
                margin-bottom: 30px;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
            .section {
                background: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
            }
            .section h3 {
                margin-bottom: 15px;
                color: #ffd700;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 15px;
            }
            .btn {
                padding: 15px 25px;
                background: rgba(255, 255, 255, 0.2);
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 10px;
                color: white;
                text-decoration: none;
                text-align: center;
                font-weight: bold;
                transition: all 0.3s;
                display: block;
            }
            .btn:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            }
            .endpoint {
                display: flex;
                align-items: center;
                padding: 10px;
                margin: 5px 0;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 5px;
                font-size: 0.9em;
            }
            .method {
                font-weight: bold;
                padding: 5px 10px;
                border-radius: 5px;
                margin-right: 15px;
                font-size: 0.85em;
            }
            .post { background: #3b82f6; }
            .get { background: #10b981; }
            .path { font-family: monospace; }
            .footer {
                margin-top: 30px;
                text-align: center;
                opacity: 0.7;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛡️ Agentic Honeypot</h1>
            <p class="subtitle">Unified Server - Everything in One Place</p>
            <div class="status">✅ SERVER ONLINE</div>
            
            <div class="section">
                <h3>🎯 Web Interfaces</h3>
                <div class="grid">
                    <a href="/app" class="btn">📱 Main Honeypot App</a>
                    <a href="/tester" class="btn">🧪 API Tester</a>
                    <a href="/combined" class="btn">🔗 Combined View</a>
                </div>
            </div>
            
            <div class="section">
                <h3>📡 API Endpoints</h3>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <span class="path">/api/login</span>
                    <span style="margin-left: auto; opacity: 0.8;">Fake Bank Login</span>
                </div>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <span class="path">/api/ivr</span>
                    <span style="margin-left: auto; opacity: 0.8;">Fake IVR System</span>
                </div>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <span class="path">/api/kyc</span>
                    <span style="margin-left: auto; opacity: 0.8;">Fake KYC Verification</span>
                </div>
                <div class="endpoint">
                    <span class="method get">GET</span>
                    <span class="path">/api/health</span>
                    <span style="margin-left: auto; opacity: 0.8;">Health Check</span>
                </div>
                <div class="endpoint">
                    <span class="method get">GET</span>
                    <span class="path">/api/logs</span>
                    <span style="margin-left: auto; opacity: 0.8;">View Logs</span>
                </div>
            </div>
            
            <div class="section">
                <h3>📚 Documentation</h3>
                <div class="grid">
                    <a href="/docs" class="btn">📖 Swagger Docs</a>
                    <a href="/redoc" class="btn">📄 ReDoc</a>
                </div>
            </div>
            
            <div class="footer">
                <p>🔒 API Authentication: X-API-KEY: honeypot123</p>
                <p>🚀 Server running on http://localhost:8000</p>
                <p>Version 4.0 • Unified Server</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/app")
async def serve_hackthon_html():
    """Serve the main honeypot application"""
    file_path = BASE_DIR / "hackthon.html"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="hackthon.html not found")
    return FileResponse(file_path)

@app.get("/tester")
async def serve_api_tester():
    """Serve the API tester interface"""
    file_path = BASE_DIR / "api_tester.html"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="api_tester.html not found")
    return FileResponse(file_path)

@app.get("/combined")
async def serve_combined():
    """Serve the combined interface"""
    file_path = BASE_DIR / "combined.html"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="combined.html not found")
    return FileResponse(file_path)

# ============================================
# API ENDPOINTS
# ============================================

@app.post("/api/login")
async def fake_bank_login(
    request: Request,
    login_data: LoginRequest,
    x_api_key: str = Header(None, alias="X-API-KEY")
):
    verify_api_key(x_api_key)
    await asyncio.sleep(random.uniform(0.5, 1.2))
    
    await log_interaction(request, "/api/login", {
        "username": login_data.username,
        "password_length": len(login_data.password)
    })
    
    risk_score = analyze_login_behavior(login_data.username, login_data.password)
    fake_token = f"eyJhbGci.{secrets.token_urlsafe(32)}.{secrets.token_urlsafe(16)}"
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Login successful",
            "token": fake_token,
            "_internal_risk_score": risk_score
        }
    )

@app.post("/api/ivr")
async def fake_ivr_system(
    request: Request,
    ivr_data: IVRRequest,
    x_api_key: str = Header(None, alias="X-API-KEY")
):
    verify_api_key(x_api_key)
    await asyncio.sleep(random.uniform(0.8, 1.5))
    
    await log_interaction(request, "/api/ivr", {
        "caller_id": ivr_data.caller_id,
        "input_length": len(ivr_data.input)
    })
    
    ivr_response = generate_ivr_response(ivr_data.input)
    
    return JSONResponse(
        status_code=200,
        content={
            "ivr_response": ivr_response
        }
    )

@app.post("/api/kyc")
async def fake_kyc_verification(
    request: Request,
    kyc_data: KYCRequest,
    x_api_key: str = Header(None, alias="X-API-KEY")
):
    verify_api_key(x_api_key)
    await asyncio.sleep(random.uniform(1.0, 1.8))
    
    await log_interaction(request, "/api/kyc", {
        "aadhaar_pattern": kyc_data.aadhaar[:4] + "****",
        "pan_pattern": kyc_data.pan[:3] + "***"
    })
    
    risk_score = analyze_kyc_data(kyc_data.aadhaar, kyc_data.pan)
    
    return JSONResponse(
        status_code=200,
        content={
            "kyc_status": "verified",
            "risk_score": round(risk_score, 2)
        }
    )

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "total_interactions": len(interaction_logs)
    }

@app.get("/api/logs")
async def get_logs(
    x_api_key: str = Header(None, alias="X-API-KEY"),
    limit: int = 10
):
    verify_api_key(x_api_key)
    
    return {
        "total_logs": len(interaction_logs),
        "recent_logs": interaction_logs[-limit:],
        "timestamp": datetime.utcnow().isoformat()
    }

# ============================================
# ERROR HANDLERS
# ============================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail if isinstance(exc.detail, dict) else {"error": str(exc.detail)}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == "__main__":
    print("=" * 80)
    print("AGENTIC HONEYPOT - UNIFIED SERVER")
    print("=" * 80)
    print(f"API Key: {VALID_API_KEY}")
    print(f"\nWEB INTERFACES:")
    print(f"   Main App:     http://localhost:8000/app")
    print(f"   API Tester:   http://localhost:8000/tester")
    print(f"   Combined:     http://localhost:8000/combined")
    print(f"\nAPI ENDPOINTS:")
    print(f"   POST /api/login  (Fake Bank Login)")
    print(f"   POST /api/ivr    (Fake Customer Care)")
    print(f"   POST /api/kyc    (Fake KYC Verification)")
    print(f"   GET  /api/health (Health Check)")
    print(f"   GET  /api/logs   (View Logs)")
    print(f"\nDOCUMENTATION:")
    print(f"   Swagger:      http://localhost:8000/docs")
    print(f"   ReDoc:        http://localhost:8000/redoc")
    print("=" * 80)
    print("\nServer starting on http://localhost:8000")
    print("Press CTRL+C to stop\n")
    
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
