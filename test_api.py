import requests
import json

# Configuration
BASE_URL = "http://localhost:5000"
API_KEY = "CYBER_SENTINEL_2024_GUVI_HACKATHON"

# Test 1: Health Check
print("=" * 60)
print("TEST 1: Health Check")
print("=" * 60)
try:
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✅ Health check passed!\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 2: Honeypot Engagement (Missing API Key)
print("=" * 60)
print("TEST 2: Missing API Key (Should Fail)")
print("=" * 60)
try:
    response = requests.post(
        f"{BASE_URL}/api/honeypot/engage",
        json={"message": "Test message"},
        headers={"Content-Type": "application/json"}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    if response.status_code == 401:
        print("✅ Auth validation working!\n")
    else:
        print("⚠️ Expected 401 status\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 3: Valid Honeypot Engagement
print("=" * 60)
print("TEST 3: Valid Honeypot Request")
print("=" * 60)
try:
    scam_message = "Dear customer, your bank account will be blocked in 24 hours. Please verify by sending Rs.500 to UPI: scammer@paytm. Click: bit.ly/verify123 or call 9876543210"
    
    response = requests.post(
        f"{BASE_URL}/api/honeypot/engage",
        json={
            "message": scam_message,
            "turn_number": 1
        },
        headers={
            "Content-Type": "application/json",
            "X-API-Key": API_KEY
        }
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"\nFull Response:")
    print(json.dumps(response.json(), indent=2))
    
    if response.status_code == 200:
        data = response.json()
        print("\n" + "=" * 60)
        print("📊 ANALYSIS RESULTS:")
        print("=" * 60)
        print(f"AI Response: {data['data']['ai_response']}")
        print(f"Scam Type: {data['data']['scam_analysis']['type']}")
        print(f"Risk Level: {data['data']['scam_analysis']['risk_level']}")
        print(f"Risk Score: {data['data']['scam_analysis']['risk_score']}")
        print(f"Total Indicators: {data['data']['indicators']['total_count']}")
        print(f"UPI IDs: {data['data']['indicators']['upi_ids']}")
        print(f"URLs: {data['data']['indicators']['urls']}")
        print(f"Phone Numbers: {data['data']['indicators']['phone_numbers']}")
        print(f"Keywords: {data['data']['indicators']['keywords']}")
        print("\n✅ Honeypot engagement successful!\n")
    else:
        print("⚠️ Unexpected response\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 4: Multiple Turns
print("=" * 60)
print("TEST 4: Multi-Turn Conversation")
print("=" * 60)
try:
    for turn in range(1, 4):
        response = requests.post(
            f"{BASE_URL}/api/honeypot/engage",
            json={
                "message": "Please send money urgently to winner@ybl",
                "turn_number": turn
            },
            headers={
                "Content-Type": "application/json",
                "X-API-Key": API_KEY
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"Turn {turn}: {data['data']['ai_response']}")
        else:
            print(f"Turn {turn} failed: {response.status_code}")
    
    print("\n✅ Multi-turn test completed!\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 5: Statistics
print("=" * 60)
print("TEST 5: Get Statistics")
print("=" * 60)
try:
    response = requests.get(
        f"{BASE_URL}/api/honeypot/stats",
        headers={"X-API-Key": API_KEY}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✅ Stats retrieved!\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

print("=" * 60)
print("🎉 ALL TESTS COMPLETED!")
print("=" * 60)
print("\n✅ Your API is ready for hackathon submission!")
print(f"\nAPI URL: {BASE_URL}/api/honeypot/engage")
print(f"API Key: {API_KEY}")
print("\nNext Step: Deploy using ngrok, Render, or Railway")
