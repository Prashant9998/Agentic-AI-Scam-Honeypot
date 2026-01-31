"""
Quick test script for local honeypot API
Tests all endpoints to ensure they work before deploying to Vercel
"""

import requests
import json

BASE_URL = "http://localhost:8000"
API_KEY = "honeypot123"

def test_health():
    """Test health endpoint (no auth required)"""
    print("\n" + "="*60)
    print("TEST 1: Health Check Endpoint")
    print("="*60)
    
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✅ PASSED - Health endpoint working!")
            return True
        else:
            print("❌ FAILED - Unexpected status code")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_login():
    """Test login endpoint"""
    print("\n" + "="*60)
    print("TEST 2: Login Endpoint (POST /api/login)")
    print("="*60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/login",
            headers={
                "Content-Type": "application/json",
                "X-API-KEY": API_KEY
            },
            json={
                "username": "testuser",
                "password": "test123"
            }
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("✅ PASSED - Login endpoint working!")
                return True
        
        print("❌ FAILED - Unexpected response")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_ivr():
    """Test IVR endpoint"""
    print("\n" + "="*60)
    print("TEST 3: IVR Endpoint (POST /api/ivr)")
    print("="*60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/ivr",
            headers={
                "Content-Type": "application/json",
                "X-API-KEY": API_KEY
            },
            json={
                "caller_id": "+919876543210",
                "input": "My account is blocked"
            }
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✅ PASSED - IVR endpoint working!")
            return True
        else:
            print("❌ FAILED - Unexpected status code")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_kyc():
    """Test KYC endpoint"""
    print("\n" + "="*60)
    print("TEST 4: KYC Endpoint (POST /api/kyc)")
    print("="*60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/kyc",
            headers={
                "Content-Type": "application/json",
                "X-API-KEY": API_KEY
            },
            json={
                "aadhaar": "123456789012",
                "pan": "ABCDE1234F"
            }
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✅ PASSED - KYC endpoint working!")
            return True
        else:
            print("❌ FAILED - Unexpected status code")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_unauthorized():
    """Test authentication (should fail without API key)"""
    print("\n" + "="*60)
    print("TEST 5: Authentication Test (no API key)")
    print("="*60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/login",
            headers={
                "Content-Type": "application/json"
                # No X-API-KEY header
            },
            json={
                "username": "hacker",
                "password": "password"
            }
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 401:
            print("✅ PASSED - Authentication working correctly!")
            return True
        else:
            print("❌ FAILED - Should return 401 without API key")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    print("\n🛡️  HONEYPOT API LOCAL TESTING")
    print(f"Testing API at: {BASE_URL}")
    print(f"API Key: {API_KEY}")
    
    results = []
    
    # Run all tests
    results.append(("Health Check", test_health()))
    results.append(("Login Endpoint", test_login()))
    results.append(("IVR Endpoint", test_ivr()))
    results.append(("KYC Endpoint", test_kyc()))
    results.append(("Authentication", test_unauthorized()))
    
    # Summary
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Your API is working perfectly locally.")
        print("Now we can deploy to Vercel with confidence.")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
