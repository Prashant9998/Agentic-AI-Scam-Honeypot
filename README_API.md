# 🛡️ Agentic Honeypot API - Hackathon Documentation

## 📋 Overview

This is a **defensive cybersecurity honeypot** designed to attract scammers, analyze their behavior, and generate realistic fake responses for fraud detection research.

⚠️ **DISCLAIMER**: This is NOT a real banking system. It's for educational and research purposes only.

---

## 🚀 Quick Start

### Local Development

1. **Install Dependencies**
```bash
cd hackthon
pip install -r requirements.txt
```

2. **Run the Server**
```bash
python honeypot_api.py
```

The API will be available at: `http://localhost:8000`

3. **View API Documentation**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 🔐 Authentication

All API endpoints (except `/` and `/api/health`) require authentication via API key.

**Header Required:**
```
X-API-KEY: honeypot123
```

**Unauthorized Response (401):**
```json
{
  "error": "Unauthorized"
}
```

---

## 📡 API Endpoints

### 1️⃣ Fake Bank Login
**Endpoint:** `POST /api/login`

Simulates a banking login system. Always returns success to keep attackers engaged.

**Request:**
```json
{
  "username": "user123",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "status": "success",
  "message": "Login successful",
  "token": "eyJhbGci.fake_token_here.signature"
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: honeypot123" \
  -d '{"username":"testuser","password":"test123"}'
```

---

### 2️⃣ Fake Customer Care / IVR
**Endpoint:** `POST /api/ivr`

Simulates an Interactive Voice Response (IVR) system with realistic, time-wasting responses.

**Request:**
```json
{
  "caller_id": "+919876543210",
  "input": "My account is blocked"
}
```

**Response (200):**
```json
{
  "ivr_response": "Your account is temporarily blocked. Press 9 to continue."
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/api/ivr \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: honeypot123" \
  -d '{"caller_id":"+919876543210","input":"help me unlock account"}'
```

---

### 3️⃣ Fake KYC Verification
**Endpoint:** `POST /api/kyc`

Simulates KYC (Know Your Customer) verification. Always returns "verified" status with AI-generated risk score.

**Request:**
```json
{
  "aadhaar": "123456789012",
  "pan": "ABCDE1234F"
}
```

**Response (200):**
```json
{
  "kyc_status": "verified",
  "risk_score": 0.93
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/api/kyc \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: honeypot123" \
  -d '{"aadhaar":"123456789012","pan":"ABCDE1234F"}'
```

---

### 4️⃣ Health Check
**Endpoint:** `GET /api/health`

Check if the API is running (no authentication required).

**Response (200):**
```json
{
  "status": "healthy",
  "timestamp": "2026-01-29T07:49:41.123456",
  "total_interactions": 42
}
```

**cURL Example:**
```bash
curl http://localhost:8000/api/health
```

---

### 5️⃣ View Logs
**Endpoint:** `GET /api/logs`

Retrieve recent interaction logs (requires authentication).

**Query Parameters:**
- `limit`: Number of recent logs to return (default: 10)

**Response (200):**
```json
{
  "total_logs": 100,
  "recent_logs": [
    {
      "timestamp": "2026-01-29T07:50:00.000000",
      "ip_address": "127.0.0.1",
      "endpoint": "/api/login",
      "payload_summary": "{'username': 'test', 'password_length': 8}"
    }
  ]
}
```

**cURL Example:**
```bash
curl http://localhost:8000/api/logs?limit=5 \
  -H "X-API-KEY: honeypot123"
```

---

## 🤖 AI-Like Behavior Analysis

The honeypot includes simulated AI logic:

### Login Analysis
- Detects weak passwords (< 6 characters)
- Identifies common attack patterns ('password', '123456', etc.)
- Flags suspicious usernames ('admin', 'root', etc.)
- Generates risk scores (0.80 - 0.99)

### KYC Analysis
- Validates Aadhaar/PAN format
- Detects dummy/test patterns (0000, 1111, AAA, XXX)
- Generates realistic risk scores
- All requests return "verified" to keep attackers engaged

### IVR Intelligence
- Context-aware responses based on input keywords
- Realistic delays (0.5 - 1.5 seconds)
- Time-wasting messages to frustrate scammers

---

## 📊 Logging System

All interactions are logged with:
- Timestamp (UTC)
- IP address
- Endpoint accessed
- Payload summary
- User agent

**Production Enhancement:**
In a real-world deployment, logs would be sent to:
- SIEM (Security Information and Event Management) systems
- Threat intelligence platforms
- Analytics dashboards
- Alert systems for suspicious patterns

---

## 🌐 Deployment

### Deploy to Render

1. Create a new Web Service on [Render](https://render.com)

2. Connect your GitHub repository

3. Configure settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn honeypot_api:app --host 0.0.0.0 --port 8000`
   - **Environment:** Python 3.11+

4. Add environment variable (optional):
   - `API_KEY` = `honeypot123`

5. Deploy!

### Deploy to Railway

1. Create a new project on [Railway](https://railway.app)

2. Connect your GitHub repository

3. Railway will auto-detect the Python app

4. Add start command in `railway.toml` or dashboard:
   ```
   uvicorn honeypot_api:app --host 0.0.0.0 --port $PORT
   ```

5. Deploy!

---

## 🧪 Testing with API Tester

Use the provided `api_tester.html` to test all endpoints:

1. Open `api_tester.html` in a browser
2. Update the API URL to your deployed endpoint
3. Enter API Key: `honeypot123`
4. Test each endpoint

---

## 📝 Example Test Scenarios

### Scenario 1: Weak Password Attack
```bash
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: honeypot123" \
  -d '{"username":"admin","password":"123"}'
```
**Result:** Returns success, but internally flags as high-risk

### Scenario 2: Dummy KYC Data
```bash
curl -X POST http://localhost:8000/api/kyc \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: honeypot123" \
  -d '{"aadhaar":"000011112222","pan":"AAAAA0000A"}'
```
**Result:** Returns verified, but logs suspicious patterns

### Scenario 3: IVR Engagement
```bash
curl -X POST http://localhost:8000/api/ivr \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: honeypot123" \
  -d '{"caller_id":"+919999999999","input":"account blocked urgent help"}'
```
**Result:** Returns time-wasting IVR response

---

## 🎯 Hackathon Validation

Your API will be tested by hackathon organizers using:

1. **Authentication Test:** Valid/invalid API keys
2. **Endpoint Availability:** All 3 core endpoints
3. **Response Format:** Correct JSON structure
4. **Status Codes:** Proper HTTP codes (200, 401)
5. **Realistic Behavior:** AI-like risk scoring

**Make sure:**
- ✅ API is publicly accessible
- ✅ All endpoints return correct JSON
- ✅ Authentication works correctly
- ✅ No real user data is stored

---

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:8000 | xargs kill -9
```

### Dependencies Not Installing
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v
```

### API Not Responding
- Check firewall settings
- Verify port 8000 is open
- Check server logs for errors
- Ensure `0.0.0.0` binding (not `127.0.0.1`)

---

## 📚 Additional Resources

- FastAPI Documentation: https://fastapi.tiangolo.com
- Uvicorn Documentation: https://www.uvicorn.org
- Pydantic Models: https://docs.pydantic.dev

---

## 🏆 Hackathon Tips

1. **Demo Your API:** Use Swagger UI (`/docs`) for live demos
2. **Show Logs:** Demonstrate the logging system
3. **Explain AI Logic:** Highlight the behavior analysis code
4. **Security Focus:** Emphasize this is a defensive tool
5. **Scalability:** Mention production enhancements (SIEM, databases)

---

## 🛠️ Future Enhancements

For a production-grade honeypot:
- Database integration (PostgreSQL, MongoDB)
- Redis for distributed logging
- Machine learning for pattern detection
- Real-time alerting (email, Slack, PagerDuty)
- Geographic IP tracking
- Advanced threat intelligence integration
- Rate limiting per IP
- Honeypot token tracking

---

## 📄 License

This project is for educational and research purposes only.

---

**Built for AI-for-Fraud-Detection Hackathon 2024** 🚀
