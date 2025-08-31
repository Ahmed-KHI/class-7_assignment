"""
Setup script for Smart Customer Support Bot
Helps with installation and configuration
"""
import os
import subprocess
import sys

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("Please run manually: pip install -r requirements.txt")
        return False

def setup_environment():
    """Set up environment file"""
    print("\n🔧 Setting up environment...")
    
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    if os.path.exists('.env.example'):
        
        with open('.env.example', 'r') as src, open('.env', 'w') as dst:
            dst.write(src.read())
        print("✅ Created .env file from template")
        print("⚠️  Please edit .env file and add your actual Gemini API key")
        return True
    else:
        print("❌ .env.example file not found")
        return False

def check_api_key():
    """Check if API key is configured"""
    print("\n🔑 Checking API key configuration...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key and api_key != "your_actual_gemini_api_key_here":
            print("✅ Gemini API key is configured")
            return True
        else:
            print("❌ Gemini API key not configured")
            print("Please edit .env file and add your API key:")
            print("GEMINI_API_KEY=your_actual_gemini_api_key_here")
            return False
            
    except ImportError:
        print("❌ python-dotenv not available yet")
        return False

def main():
    """Main setup function"""
    print("🚀 Smart Customer Support Bot Setup")
    print("=" * 50)
    
    deps_ok = install_dependencies()
    
    env_ok = setup_environment()
    
    if deps_ok:
        api_ok = check_api_key()
    else:
        api_ok = False
    
    print("\n" + "=" * 50)
    
    if deps_ok and env_ok and api_ok:
        print("🎉 Setup completed successfully!")
        print("\nYou can now run:")
        print("• python test_bot.py  (basic tests)")
        print("• python main.py      (full demo)")
        print("• python interactive_demo.py  (interactive mode)")
    else:
        print("⚠️  Setup completed with issues")
        print("\nPlease:")
        if not deps_ok:
            print("• Install dependencies: pip install -r requirements.txt")
        if not env_ok:
            print("• Create .env file from .env.example")
        if not api_ok:
            print("• Configure your Gemini API key in .env file")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
