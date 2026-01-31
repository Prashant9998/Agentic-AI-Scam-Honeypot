"""
AGENTIC HONEYPOT API FOR FRAUD DETECTION HACKATHON
===================================================

This is a defensive cybersecurity honeypot designed to attract scammers,
analyze their behavior, and generate realistic fake responses.

⚠️ DISCLAIMER: This is NOT a real banking system. It's a honeypot for
fraud detection research and educational purposes only.

Tech Stack: Python + FastAPI
Authentication: API Key via HTTP Header (X-API-KEY)
Deployment: Render / Railway compatible
"""

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
import secrets
import time
import random
import asyncio
import uvicorn

# ============================================
# FASTAPI APPLICATION SETUP
# ============================================

app = FastAPI(
    title="Agentic Honeypot API",
    description="AI-powered honeypot for fraud detection and scam analysis",
    version="3.0",
    docs_url="/docs",  # Swagger UI at /docs
    redoc_url="/redoc"  # ReDoc at /redoc
)

# Enable CORS for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# CONFIGURATION
# ============================================

# API Key for authentication
VALID_API_KEY = "honeypot123"

# In-memory logging (in production, use Redis, PostgreSQL, or SIEM)
interaction_logs = []

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
    """
    Verify API key from request header
    
    Expected Header: X-API-KEY: honeypot123
    
    In production, this would:
    - Check against a database of valid API keys
    - Track rate limits per API key
    - Log all authentication attempts
    """
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
    """
    Log all interactions for analysis
    
    In a production honeypot, these logs would be sent to:
    - SIEM (Security Information and Event Management) systems
    - Threat intelligence platforms
    - Analytics dashboards
    - Alert systems for suspicious patterns
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip_address": request.client.host,
        "endpoint": endpoint,
        "payload_summary": str(payload)[:200],  # Truncate for storage
        "user_agent": request.headers.get("user-agent", "Unknown")
    }
    
    interaction_logs.append(log_entry)
    
    # In production, you would:
    # - Send to SIEM: await siem_client.send(log_entry)
    # - Store in database: await db.logs.insert(log_entry)
    # - Trigger alerts: await check_threat_patterns(log_entry)
    
    print(f"[HONEYPOT LOG] {log_entry}")

# ============================================
# AI-LIKE BEHAVIOR ANALYSIS
# ============================================

def analyze_login_behavior(username: str, password: str) -> float:
    """
    Simulate AI-based risk scoring for login attempts
    
    Real-world factors analyzed:
    - Password strength and patterns
    - Username patterns (generic, suspicious)
    - Historical attack signatures
    - Geolocation anomalies
    """
    risk_score = 0.80  # Base risk score
    
    # Weak password detection
    if len(password) < 6:
        risk_score += 0.10
    
    # Common attack patterns
    if password.lower() in ['password', '123456', 'admin', 'test']:
        risk_score += 0.08
    
    # Suspicious username patterns
    if username.lower() in ['admin', 'test', 'root', 'user']:
        risk_score += 0.05
    
    # Add randomization to appear more realistic
    risk_score += random.uniform(-0.03, 0.03)
    
    # Cap at 0.99 to maintain realism
    return min(risk_score, 0.99)

def analyze_kyc_data(aadhaar: str, pan: str) -> float:
    """
    Simulate AI-based KYC verification and risk scoring
    
    Real-world checks:
    - Format validation
    - Checksum verification
    - Database cross-reference
    - Fraud pattern matching
    """
    risk_score = 0.85
    
    # Check for dummy/test patterns
    if aadhaar.startswith("0000") or aadhaar.startswith("1111"):
        risk_score += 0.10
    
    if pan.startswith("AAA") or pan.startswith("XXX"):
        risk_score += 0.08
    
    # All numeric Aadhaar check
    if not aadhaar.isdigit() or len(aadhaar) != 12:
        risk_score += 0.05
    
    # Add randomization
    risk_score += random.uniform(-0.02, 0.04)
    
    return min(risk_score, 0.99)

def generate_ivr_response(caller_input: str) -> str:
    """
    Generate realistic IVR responses to keep attackers engaged
    
    Strategy: Make responses believable but time-wasting
    """
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
    
    # Simple keyword-based selection (in production, use NLP)
    lower_input = caller_input.lower()
    if any(word in lower_input for word in ['block', 'locked', 'suspend']):
        return responses[0]
    elif any(word in lower_input for word in ['help', 'speak', 'agent']):
        return responses[6]
    else:
        return random.choice(responses)

# ============================================
# API ENDPOINTS
# ============================================

@app.get("/")
async def root():
    """
    Root endpoint - Serve combined.html
    """
    from fastapi.responses import FileResponse
    from pathlib import Path
    
    # Get the directory where this script is located
    base_dir = Path(__file__).resolve().parent
    combined_html_path = base_dir / "combined.html"
    
    # Check if combined.html exists
    if combined_html_path.exists():
        return FileResponse(combined_html_path)
    else:
        # Fallback to API landing page if combined.html doesn't exist
        from fastapi.responses import HTMLResponse
        return HTMLResponse(content="<h1>Combined.html not found. Please deploy all files.</h1>")

@app.post("/")
async def root_post(x_api_key: str = Header(None, alias="X-API-KEY")):
    """
    Root POST endpoint - For hackathon validator testing
    Returns success message with API information
    """
    # Verify API key
    verify_api_key(x_api_key)
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Agentic Honeypot API is running",
            "api_version": "3.0",
            "endpoints": {
                "login": "/api/login",
                "ivr": "/api/ivr",
                "kyc": "/api/kyc",
                "health": "/api/health",
                "logs": "/api/logs"
            },
            "authentication": "X-API-KEY header required"
        }
    )

@app.get("/hackthon.html")
async def serve_hackthon():
    """
    Serve hackthon.html for iframe in combined.html
    """
    from fastapi.responses import FileResponse
    from pathlib import Path
    
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "hackthon.html"
    
    if file_path.exists():
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="hackthon.html not found")

@app.get("/api_tester.html")
async def serve_api_tester():
    """
    Serve api_tester.html for iframe in combined.html
    """
    from fastapi.responses import FileResponse
    from pathlib import Path
    
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "api_tester.html"
    
    if file_path.exists():
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="api_tester.html not found")

@app.post("/api/login")
async def fake_bank_login(
    request: Request,
    login_data: LoginRequest,
    x_api_key: str = Header(None, alias="X-API-KEY")
):
    """
    ENDPOINT 1: Fake Bank Login
    
    This endpoint simulates a banking login system.
    - Always returns success to keep attackers engaged
    - Logs all attempts for behavior analysis
    - Generates fake session tokens
    
    🔒 Authentication Required: X-API-KEY header
    """
    # Verify API key
    verify_api_key(x_api_key)
    
    # Simulate realistic processing delay
    await asyncio.sleep(random.uniform(0.5, 1.2))
    
    # Log the interaction
    await log_interaction(request, "/api/login", {
        "username": login_data.username,
        "password_length": len(login_data.password)
    })
    
    # Analyze behavior and generate risk score
    risk_score = analyze_login_behavior(login_data.username, login_data.password)
    
    # Generate fake JWT-like token (not a real JWT)
    fake_token = f"eyJhbGci.{secrets.token_urlsafe(32)}.{secrets.token_urlsafe(16)}"
    
    # Always return success (honeypot strategy)
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Login successful",
            "token": fake_token,
            # Hidden metadata for analysis (would be logged, not returned in production)
            "_internal_risk_score": risk_score
        }
    )

@app.post("/api/ivr")
async def fake_ivr_system(
    request: Request,
    ivr_data: IVRRequest,
    x_api_key: str = Header(None, alias="X-API-KEY")
):
    """
    ENDPOINT 2: Fake Customer Care / IVR
    
    This endpoint simulates an Interactive Voice Response system.
    - Provides realistic IVR-style responses
    - Designed to waste scammer's time
    - Logs caller patterns
    
    🔒 Authentication Required: X-API-KEY header
    """
    # Verify API key
    verify_api_key(x_api_key)
    
    # Simulate IVR processing delay
    await asyncio.sleep(random.uniform(0.8, 1.5))
    
    # Log the interaction
    await log_interaction(request, "/api/ivr", {
        "caller_id": ivr_data.caller_id,
        "input_length": len(ivr_data.input)
    })
    
    # Generate contextual IVR response
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
    """
    ENDPOINT 3: Fake KYC Verification
    
    This endpoint simulates a KYC (Know Your Customer) verification system.
    - Always returns "verified" status
    - Generates realistic risk scores
    - Logs all KYC attempts (potential data harvesting attacks)
    
    🔒 Authentication Required: X-API-KEY header
    """
    # Verify API key
    verify_api_key(x_api_key)
    
    # Simulate KYC processing delay
    await asyncio.sleep(random.uniform(1.0, 1.8))
    
    # Log the interaction (in production, this would trigger alerts)
    await log_interaction(request, "/api/kyc", {
        "aadhaar_pattern": kyc_data.aadhaar[:4] + "****",  # Mask for logging
        "pan_pattern": kyc_data.pan[:3] + "***"
    })
    
    # Analyze KYC data and generate risk score
    risk_score = analyze_kyc_data(kyc_data.aadhaar, kyc_data.pan)
    
    # Always return verified (honeypot strategy)
    return JSONResponse(
        status_code=200,
        content={
            "kyc_status": "verified",
            "risk_score": round(risk_score, 2)
        }
    )

# ============================================
# ADDITIONAL UTILITY ENDPOINTS
# ============================================

@app.get("/api/health")
async def health_check():
    """
    Health check endpoint for deployment platforms
    """
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
    """
    Retrieve recent interaction logs
    
    🔒 Authentication Required
    """
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
    """
    Custom error handler for HTTP exceptions
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail if isinstance(exc.detail, dict) else {"error": str(exc.detail)}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Catch-all error handler
    """
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("AGENTIC HONEYPOT API - FRAUD DETECTION SYSTEM")
    print("=" * 70)
    print(f"API Key: {VALID_API_KEY}")
    print(f"Endpoints:")
    print(f"  - POST /api/login  (Fake Bank Login)")
    print(f"  - POST /api/ivr    (Fake Customer Care)")
    print(f"  - POST /api/kyc    (Fake KYC Verification)")
    print(f"  - GET  /api/health (Health Check)")
    print(f"  - GET  /api/logs   (View Logs)")
    print(f"\nDocs: http://localhost:8000/docs")
    print("=" * 70)
    
    # Run with uvicorn
    uvicorn.run(
        "honeypot_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes (disable in production)
        log_level="info"
    )
