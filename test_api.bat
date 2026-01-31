@echo off
REM Honeypot API Test Script for Windows
REM Run this script to test all endpoints

set API_URL=http://localhost:8000
set API_KEY=honeypot123

echo ======================================
echo  HONEYPOT API ENDPOINT TESTING
echo ======================================
echo.

REM Test 1: Health Check (No Auth Required)
echo TEST 1: Health Check
curl -X GET %API_URL%/api/health
echo.
echo.

REM Test 2: Root Endpoint
echo TEST 2: Root Endpoint
curl -X GET %API_URL%/
echo.
echo.

REM Test 3: Login Endpoint (With Auth)
echo TEST 3: Fake Bank Login
curl -X POST %API_URL%/api/login -H "Content-Type: application/json" -H "X-API-KEY: %API_KEY%" -d "{\"username\":\"testuser\",\"password\":\"test123\"}"
echo.
echo.

REM Test 4: IVR Endpoint (With Auth)
echo TEST 4: Fake Customer Care IVR
curl -X POST %API_URL%/api/ivr -H "Content-Type: application/json" -H "X-API-KEY: %API_KEY%" -d "{\"caller_id\":\"+919876543210\",\"input\":\"My account is blocked\"}"
echo.
echo.

REM Test 5: KYC Endpoint (With Auth)
echo TEST 5: Fake KYC Verification  
curl -X POST %API_URL%/api/kyc -H "Content-Type: application/json" -H "X-API-KEY: %API_KEY%" -d "{\"aadhaar\":\"123456789012\",\"pan\":\"ABCDE1234F\"}"
echo.
echo.

REM Test 6: Unauthorized Access (No API Key)
echo TEST 6: Unauthorized Access (Should Fail)
curl -X POST %API_URL%/api/login -H "Content-Type: application/json" -d "{\"username\":\"hacker\",\"password\":\"password\"}"
echo.
echo.

REM Test 7: Invalid API Key
echo TEST 7: Invalid API Key (Should Fail)
curl -X POST %API_URL%/api/login -H "Content-Type: application/json" -H "X-API-KEY: wrongkey123" -d "{\"username\":\"hacker\",\"password\":\"password\"}"
echo.
echo.

REM Test 8: View Logs
echo TEST 8: View Interaction Logs
curl -X GET "%API_URL%/api/logs?limit=5" -H "X-API-KEY: %API_KEY%"
echo.
echo.

echo ======================================
echo  ALL TESTS COMPLETED
echo ======================================
pause
