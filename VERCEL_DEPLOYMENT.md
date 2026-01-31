# 🚀 Vercel Deployment Guide for Combined.html

## ✅ Changes Made

Your API has been updated to serve `combined.html` at the root URL:
- **Root URL (/)** now serves `combined.html`
- **Added routes** for `hackthon.html` and `api_tester.html` (needed for iframes)
- **API endpoints** remain accessible at `/api/*`

## 📦 Files You Need to Deploy to Vercel

Make sure ALL these files are in your Vercel deployment:

### Required Files:
1. ✅ `api.py` - Vercel entry point
2. ✅ `honeypot_api.py` - Main API logic
3. ✅ `combined.html` - Main UI (shown at root)
4. ✅ `hackthon.html` - Honeypot interface (loaded in iframe)
5. ✅ `api_tester.html` - API tester (loaded in iframe)
6. ✅ `requirements.txt` - Python dependencies
7. ✅ `vercel.json` - Vercel configuration

## 🔄 How to Deploy/Redeploy

### Option 1: Using Vercel CLI
```bash
# Install Vercel CLI if you haven't
npm install -g vercel

# Navigate to your project folder
cd C:\Users\dell\OneDrive\Desktop\cyber\hackthon

# Deploy (it will push all files)
vercel --prod
```

### Option 2: Using Vercel Dashboard (Recommended)
1. Go to https://vercel.com/dashboard
2. Find your project
3. Click on the project
4. Go to **Settings** → **Git**
5. **Trigger a new deployment:**
   - Either push changes to your GitHub repo (if connected)
   - Or click **Redeploy** button in the Deployments tab

### Option 3: Manual Upload
1. Go to https://vercel.com/new
2. Upload your `hackthon` folder
3. Vercel will auto-detect the configuration

## 🎯 What You'll See After Deployment

### Your Deployed URLs:
- **Main Page**: `https://your-project.vercel.app/` → Shows **combined.html**
- **Honeypot Tab**: Accessible via tabs in combined.html
- **API Tester Tab**: Accessible via tabs in combined.html
- **API Docs**: `https://your-project.vercel.app/docs`
- **API Endpoints**: `https://your-project.vercel.app/api/*`

## 🔍 Testing After Deployment

1. Visit your Vercel URL: `https://your-project.vercel.app`
2. You should see the **Cyber Sentinel** interface with two tabs:
   - 🛡️ HONEYPOT tab
   - 🔧 API TESTER tab
3. Both iframes should load properly
4. Test the API using the API Tester tab

## ⚠️ Important Notes

### API Key Configuration
The API key is currently hardcoded as `honeypot123`. For production:
1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add: `API_KEY=your-secure-key-here`
3. Update `honeypot_api.py` to read from environment:
   ```python
   import os
   VALID_API_KEY = os.getenv("API_KEY", "honeypot123")
   ```

### File Structure Check
Before deploying, verify all files are present:
```bash
dir C:\Users\dell\OneDrive\Desktop\cyber\hackthon
```

You should see:
- api.py
- honeypot_api.py
- combined.html
- hackthon.html
- api_tester.html
- requirements.txt
- vercel.json

## 🐛 Troubleshooting

### Issue: Still showing API landing page
**Solution**: 
- Clear browser cache (Ctrl+Shift+R)
- Wait 1-2 minutes for Vercel deployment to complete
- Check Vercel deployment logs for errors

### Issue: iframes not loading
**Solution**: 
- Verify `hackthon.html` and `api_tester.html` are deployed
- Check browser console for errors
- Ensure files are in the same directory as `api.py`

### Issue: 404 errors
**Solution**: 
- Make sure `vercel.json` is configured correctly
- Verify all HTML files are in the deployment
- Check Vercel function logs

### Issue: API not working
**Solution**: 
- Test endpoints directly: `https://your-project.vercel.app/api/health`
- Check if you're including the `X-API-KEY: honeypot123` header
- View Vercel function logs for errors

## 📝 Current Configuration

### vercel.json
```json
{
    "builds": [
        {
            "src": "api.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "api.py"
        }
    ]
}
```

This configuration:
- Builds Python API from `api.py`
- Routes ALL requests to the API
- API then serves HTML files or API endpoints based on the route

## ✨ Next Steps

1. **Deploy the changes** to Vercel
2. **Test the deployment** at your Vercel URL
3. If you see the Cyber Sentinel combined interface with tabs, **you're done!** ✅

## 🆘 Need Help?

If deployment fails:
1. Check Vercel deployment logs
2. Ensure all files are uploaded
3. Verify `requirements.txt` has all dependencies:
   ```
   fastapi
   uvicorn[standard]
   pydantic
   python-multipart
   ```

---

**Ready to deploy?** Run `vercel --prod` or push to your GitHub repo!
