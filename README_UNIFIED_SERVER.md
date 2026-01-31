# 🛡️ Agentic Honeypot - Unified Server

## Overview

This unified server runs **everything in one place**:
- ✅ FastAPI backend with honeypot endpoints
- ✅ All HTML interfaces (hackthon.html, api_tester.html, combined.html)
- ✅ Single server on port 8000
- ✅ No need to run multiple servers

## Quick Start

### Option 1: Windows Batch Script (Easiest)
```bash
start_server.bat
```

### Option 2: Direct Python Command
```bash
python server.py
```

## Access Your Application

Once the server is running, access everything from:

### 🎯 Web Interfaces
- **Landing Page**: http://localhost:8000
- **Main Honeypot App**: http://localhost:8000/app
- **API Tester**: http://localhost:8000/tester
- **Combined View**: http://localhost:8000/combined

### 📡 API Endpoints
- **POST** `/api/login` - Fake Bank Login
- **POST** `/api/ivr` - Fake IVR System
- **POST** `/api/kyc` - Fake KYC Verification
- **GET** `/api/health` - Health Check
- **GET** `/api/logs` - View Interaction Logs

### 📚 Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Authentication

All API endpoints require the following header:
```
X-API-KEY: honeypot123
```

## Testing the API

### Using the Built-in Tester
1. Go to http://localhost:8000/tester
2. The API key is pre-filled
3. Test all endpoints with one click

### Using curl
```bash
# Test Login
curl -X POST http://localhost:8000/api/login \
  -H "X-API-KEY: honeypot123" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"password\":\"test123\"}"

# Test IVR
curl -X POST http://localhost:8000/api/ivr \
  -H "X-API-KEY: honeypot123" \
  -H "Content-Type: application/json" \
  -d "{\"caller_id\":\"+919876543210\",\"input\":\"I need help\"}"

# Test KYC
curl -X POST http://localhost:8000/api/kyc \
  -H "X-API-KEY: honeypot123" \
  -H "Content-Type: application/json" \
  -d "{\"aadhaar\":\"123456789012\",\"pan\":\"ABCDE1234F\"}"

# Health Check
curl http://localhost:8000/api/health

# View Logs
curl http://localhost:8000/api/logs \
  -H "X-API-KEY: honeypot123"
```

## File Structure

```
hackthon/
├── server.py              # Unified server (API + HTML serving)
├── start_server.bat       # Easy startup script for Windows
├── honeypot_api.py        # Original API (not needed for unified server)
├── requirements.txt       # Python dependencies
├── hackthon.html          # Main honeypot interface
├── api_tester.html        # API testing interface
├── combined.html          # Combined view
└── README_UNIFIED_SERVER.md  # This file
```

## How It Works

The unified server (`server.py`):
1. **Imports all API logic** from the original honeypot_api.py
2. **Serves HTML files** via FastAPI's FileResponse
3. **Runs on a single port** (8000) for both API and web interface
4. **Handles routing**:
   - `/` → Landing page
   - `/app` → hackthon.html
   - `/tester` → api_tester.html
   - `/combined` → combined.html
   - `/api/*` → API endpoints

## Benefits

✅ **Single Command** - Start everything with one script
✅ **No CORS Issues** - API and HTML served from same origin
✅ **Easy Deployment** - Deploy one server instead of multiple
✅ **Organized** - All routes in one place
✅ **Development Friendly** - Auto-reload on code changes

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, edit `server.py` and change:
```python
port=8000  # Change to any available port
```

### Dependencies Missing
```bash
pip install -r requirements.txt
```

### HTML Files Not Found
Make sure `hackthon.html`, `api_tester.html`, and `combined.html` are in the same directory as `server.py`.

## Deployment

### For Production
1. Set `reload=False` in `server.py`
2. Change `allow_origins=["*"]` to specific domains
3. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn server:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

### Deploy to Cloud
The unified server works with:
- **Render** - Use `server.py` as entry point
- **Railway** - Auto-detects FastAPI
- **Vercel** - Use `api.py` (already configured)
- **Heroku** - Add Procfile: `web: uvicorn server:app --host 0.0.0.0 --port $PORT`

## Support

For issues or questions:
1. Check the logs in the terminal
2. Visit http://localhost:8000/docs for API documentation
3. Test endpoints at http://localhost:8000/tester

---

**Built for Hackathon** | **Version 4.0** | **Unified Server Architecture**
