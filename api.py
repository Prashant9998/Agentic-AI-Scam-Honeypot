"""
Vercel entrypoint for the Agentic Honeypot API

This file imports the FastAPI app from honeypot_api.py 
to satisfy Vercel's deployment requirements.
"""

from honeypot_api import app

# Vercel will look for 'app' in this file
__all__ = ['app']
