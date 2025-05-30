#!/usr/bin/env python3
"""
SIMO KHDN FastAPI Server Launcher
Starts the server with proper configuration and error handling
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8+ is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def check_dependencies():
    """Check and install required dependencies"""
    required_packages = [
        "fastapi",
        "uvicorn", 
        "requests",
        "jinja2",
        "pandas",
        "openpyxl"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is missing")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install"
            ] + missing_packages)
            print("✅ All packages installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages")
            return False
    
    return True

def create_directories():
    """Create necessary directories"""
    directories = ["logs", "templates"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Directory '{directory}' ready")

def start_server():
    """Start the FastAPI server"""
    print("\n🚀 Starting SIMO KHDN FastAPI Server...")
    print("📍 Server will be available at: http://localhost:8069")
    print("📝 API documentation at: http://localhost:8069/docs")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    try:
        # Import here to ensure dependencies are installed
        import uvicorn
        from config import SERVER_HOST, SERVER_PORT, DEBUG_MODE
        
        uvicorn.run(
            "main:app",
            host=SERVER_HOST,
            port=SERVER_PORT,
            reload=DEBUG_MODE,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False
    
    return True

def main():
    """Main launcher function"""
    print("=" * 60)
    print("🏦 SIMO KHDN FastAPI Server Launcher")
    print("   Hệ thống quản lý rủi ro thanh toán KHDN")
    print("=" * 60)
    
    # Check system requirements
    if not check_python_version():
        sys.exit(1)
    
    # Check and install dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Create necessary directories
    create_directories()
    
    # Start the server
    if not start_server():
        sys.exit(1)

if __name__ == "__main__":
    main()