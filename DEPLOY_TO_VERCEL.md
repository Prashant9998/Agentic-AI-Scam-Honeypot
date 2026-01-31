# ✅ VERCEL DEPLOYMENT - QUICK GUIDE

## What's Fixed

Your API now serves **combined.html** at the root URL instead of the API landing page.

### Routes configured:
- `/` → **combined.html** (main page with tabs)
- `/hackthon.html` → Honeypot interface (loaded in iframe)
- `/api_tester.html` → API tester (loaded in iframe)
- `/api/*` → All API endpoints
- `/docs` → Swagger documentation
- `/redoc` → ReDoc documentation

---

## 📦 DEPLOYMENT CHECKLIST

Before deploying, verify these files exist in your `hackthon` folder:

```
☐ api.py                  (Vercel entry point)
☐ honeypot_api.py         (Main API with updated routes)
☐ combined.html           (Main UI - shows at root)
☐ hackthon.html           (Honeypot - loaded in iframe)
☐ api_tester.html         (API tester - loaded in iframe)
☐ requirements.txt        (Python dependencies)
☐ vercel.json            (Vercel configuration)
```

---

## 🚀 HOW TO DEPLOY

### Option 1: Vercel CLI (Fastest)

1. Open PowerShell in the hackthon folder:
   ```powershell
   cd C:\Users\dell\OneDrive\Desktop\cyber\hackthon
   ```

2. Install Vercel CLI (one time only):
   ```powershell
   npm install -g vercel
   ```

3. Deploy:
   ```powershell
   vercel --prod
   ```

### Option 2: GitHub + Vercel (Automatic)

1. Push all files to your GitHub repository
2. Vercel will automatically detect changes and redeploy
3. Wait 1-2 minutes for deployment to complete

### Option 3: Vercel Dashboard (Manual)

1. Go to https://vercel.com/dashboard
2. Click your project
3. Click **Deployments** tab
4. Click **Redeploy** button
5. Select the latest commit and click **Redeploy**

---

## ✅ VERIFICATION

After deployment, visit your Vercel URL:

**Example**: `https://your-project-name.vercel.app`

### You should see:
1. **Cyber Sentinel** header with two tabs:
   - 🛡️ HONEYPOT
   - 🔧 API TESTER
2. Both tabs should load properly with the interfaces
3. No API landing page with endpoints list

### If you still see the old API landing page:
- **Hard refresh**: Press `Ctrl + Shift + R` (or `Cmd + Shift + R` on Mac)
- **Clear cache**: Open DevTools (F12) → Application → Clear Storage
- **Wait**: Deployment can take 1-2 minutes to propagate

---

## 🧪 TESTING

### Test the main page:
```
https://your-project.vercel.app/
```
Should show **Cyber Sentinel** with tabs ✅

### Test API endpoints:
```bash
# Health check
curl https://your-project.vercel.app/api/health

# Login endpoint (needs API key)
curl -X POST https://your-project.vercel.app/api/login \
  -H "X-API-KEY: honeypot123" \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'
```

### Test documentation:
```
https://your-project.vercel.app/docs
```
Should show Swagger UI ✅

---

## 🔑 IMPORTANT

**API Key**: `honeypot123`

All API endpoints require this header:
```
X-API-KEY: honeypot123
```

The API Tester tab includes this automatically.

---

## 🐛 TROUBLESHOOTING

### Issue: Still showing old page
**Solution**: 
1. Hard refresh browser (Ctrl+Shift+R)
2. Check Vercel deployment logs for errors
3. Verify deployment is complete (green checkmark)

### Issue: iframes not loading
**Solution**: 
1. Check browser console (F12)
2. Verify all HTML files are deployed
3. Check file paths in combined.html

### Issue: 404 errors
**Solution**: 
1. Ensure all files are in the deployment
2. Check Vercel function logs
3. Redeploy with correct files

---

## 📊 FILE SUMMARY

### api.py (Vercel Entry Point)
```python
from honeypot_api import app
__all__ = ['app']
```

### vercel.json (Configuration)
```json
{
    "builds": [{"src": "api.py", "use": "@vercel/python"}],
    "routes": [{"src": "/(.*)", "dest": "api.py"}]
}
```

### honeypot_api.py (Updated Routes)
- ✅ Root `/` serves `combined.html`
- ✅ `/hackthon.html` serves honeypot interface
- ✅ `/api_tester.html` serves API tester
- ✅ All API routes at `/api/*`

---

## 🎯 EXPECTED RESULT

After successful deployment:

**URL**: `https://your-project.vercel.app`

**Shows**: Combined interface with:
- 🛡️ HONEYPOT tab (hackthon.html in iframe)
- 🔧 API TESTER tab (api_tester.html in iframe)
- Cybersecurity themed UI
- Working API endpoints

---

**Ready to deploy?** Run `vercel --prod` from the hackthon folder!

If you see the Cyber Sentinel interface → **SUCCESS!** ✅
