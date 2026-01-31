# 🚀 RENDER.COM DEPLOYMENT - STEP BY STEP GUIDE

## ✅ Prerequisites Checklist

All files ready in `hackthon` folder:
- ✅ `honeypot_api.py` - Main FastAPI application
- ✅ `requirements.txt` - Python dependencies
- ✅ `combined.html` - Main UI
- ✅ `hackthon.html` - Honeypot interface
- ✅ `api_tester.html` - API tester
- ✅ `render.yaml` - Render configuration (optional but helpful)

---

## 🎯 DEPLOYMENT STEPS

### Step 1: Create Render Account
1. Go to **https://render.com**
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with **GitHub** (recommended) or email
4. Verify your email if required

---

### Step 2: Create New Web Service

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Choose your deployment method:

#### **Option A: Deploy from GitHub (Recommended)**
   - Connect your GitHub account
   - Select your repository
   - Click **"Connect"**

#### **Option B: Deploy from Git URL**
   - Enter your git repository URL
   - Click **"Continue"**

#### **Option C: Manual Upload**
   - Select **"Public Git repository"**
   - Or skip and manually configure

---

### Step 3: Configure Your Service

Fill in these settings:

**Name:**
```
honeypot-api
```
(or any name you prefer)

**Region:**
```
Choose closest to you (e.g., Singapore, Oregon, Frankfurt)
```

**Branch:**
```
main
```
(or your default branch)

**Root Directory:**
```
hackthon
```
(if your files are in a subfolder, otherwise leave blank)

**Runtime:**
```
Python 3
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn honeypot_api:app --host 0.0.0.0 --port $PORT
```

**Instance Type:**
```
Free
```

---

### Step 4: Environment Variables (Optional)

You can add these if needed:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11` |
| `API_KEY` | `honeypot123` |

*Leave empty for now - not required*

---

### Step 5: Deploy!

1. Click **"Create Web Service"**
2. Wait for deployment (2-5 minutes)
3. Watch the build logs - should see:
   ```
   Building...
   Installing requirements...
   Starting server...
   Your service is live 🎉
   ```

---

## ✅ VERIFICATION

Once deployed, Render will give you a URL like:
```
https://honeypot-api.onrender.com
```

### Test Your Endpoints:

**1. Health Check:**
```
https://honeypot-api.onrender.com/api/health
```
Should return:
```json
{
  "status": "healthy",
  "timestamp": "...",
  "total_interactions": 0
}
```

**2. Main Page:**
```
https://honeypot-api.onrender.com/
```
Should show your **Cyber Sentinel** interface with tabs

**3. API Tester:**
- Click the **"API TESTER"** tab
- Update the URL field to your Render URL
- Click **"Test Honeypot Endpoint"**
- Should get **SUCCESS** ✅

---

## 🎨 Update Your Frontend

After deployment, update the API URL in your `api_tester.html`:

**Before (local):**
```javascript
apiUrlInput.value = window.location.origin;
```

**After (Render):**
```javascript
apiUrlInput.value = 'https://honeypot-api.onrender.com';
```

Or leave it as is - it will auto-detect the current origin.

---

## 🐛 TROUBLESHOOTING

### Build Failed?
- Check **Build Logs** in Render dashboard
- Verify `requirements.txt` is correct
- Ensure Python version is compatible

### 404 Error?
- Verify **Start Command** is correct
- Check that `honeypot_api.py` exists
- Ensure **Root Directory** is set correctly

### 405 Error Again?
- This shouldn't happen on Render!
- Verify you're using the correct URL with `/api/` prefix
- Check that API key is included in headers

### App Sleeps After 15 Minutes?
- **Free tier** sleeps after inactivity
- First request after sleep takes ~30 seconds
- Upgrade to paid tier for 24/7 uptime (optional)

---

## 📊 COMPARISON: Before & After

| Issue | Vercel | Render |
|-------|--------|--------|
| 405 Error | ❌ Yes | ✅ Fixed |
| FastAPI Support | ⚠️ Complex | ✅ Native |
| Setup Time | 🔴 Hours | 🟢 5 mins |
| Free Tier | ✅ Yes | ✅ Yes |

---

## 🎉 SUCCESS CHECKLIST

After deployment, verify:
- ✅ Main page loads (Cyber Sentinel UI)
- ✅ `/api/health` returns 200 OK
- ✅ API Tester tab works
- ✅ Can test all endpoints (login, IVR, KYC)
- ✅ No 405 errors!

---

## 📝 FINAL NOTES

**Your Render URL:**
```
https://YOUR-APP-NAME.onrender.com
```

**API Key:**
```
honeypot123
```

**Endpoints:**
- `POST /api/login` - Fake bank login
- `POST /api/ivr` - IVR simulation
- `POST /api/kyc` - KYC verification
- `GET /api/health` - Health check
- `GET /api/logs` - View logs (requires API key)

---

**Need help?** Let me know if you get stuck at any step! 🚀
