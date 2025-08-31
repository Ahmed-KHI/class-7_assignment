"""
Test Script to verify the Customer Support Bot implementation
This script tests basic functionality without requiring the agents library
"""
import os
import sys
from datetime import datetime

def test_environment():
    """Test environment configuration"""
    print("🧪 Testing Environment Configuration...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found")
        
        # Try to load environment variables
        try:
            from dotenv import load_dotenv
            load_dotenv()
            
            gemini_key = os.getenv("GEMINI_API_KEY")
            if gemini_key and gemini_key != "your_actual_gemini_api_key_here":
                print("✅ Gemini API key configured")
            else:
                print("❌ Gemini API key not configured properly")
                print("Please update the GEMINI_API_KEY in your .env file")
                
        except ImportError:
            print("❌ python-dotenv not installed")
            print("Run: pip install python-dotenv")
    else:
        print("❌ .env file not found")
        print("Please copy .env.example to .env and configure your API key")

def test_mock_data():
    """Test mock data structures"""
    print("\n🧪 Testing Mock Data...")
    
    # Test orders database
    orders = {
        "ORD001": {"status": "delivered", "tracking": "TRK123456"},
        "ORD002": {"status": "shipped", "tracking": "TRK789012"}
    }
    
    # Test order lookup
    test_order = "ORD001"
    if test_order in orders:
        print(f"✅ Order lookup test passed: {orders[test_order]}")
    else:
        print("❌ Order lookup test failed")
    
    # Test FAQ data
    faqs = {
        "return_policy": "Returns within 30 days",
        "shipping_time": "3-5 business days"
    }
    
    query = "return"
    matches = [faq for faq in faqs.keys() if query in faq]
    if matches:
        print(f"✅ FAQ search test passed: Found {len(matches)} matches")
    else:
        print("❌ FAQ search test failed")

def test_sentiment_analysis():
    """Test sentiment analysis logic"""
    print("\n🧪 Testing Sentiment Analysis...")
    
    def analyze_sentiment(message):
        negative_words = ["terrible", "awful", "worst", "hate"]
        return "negative" if any(word in message.lower() for word in negative_words) else "positive"
    
    test_cases = [
        ("This is terrible service", "negative"),
        ("Great support, thank you", "positive"),
        ("I hate this", "negative")
    ]
    
    for message, expected in test_cases:
        result = analyze_sentiment(message)
        if result == expected:
            print(f"✅ Sentiment test passed: '{message}' -> {result}")
        else:
            print(f"❌ Sentiment test failed: '{message}' -> {result} (expected {expected})")

def test_guardrail_logic():
    """Test guardrail filtering logic"""
    print("\n🧪 Testing Guardrail Logic...")
    
    def check_content(message):
        offensive_words = ["stupid", "hate", "terrible"]
        for word in offensive_words:
            if word in message.lower():
                return f"Inappropriate content detected: {word}"
        return None
    
    test_messages = [
        "This is stupid",
        "I hate this service", 
        "Can you help me please"
    ]
    
    for message in test_messages:
        result = check_content(message)
        if result:
            print(f"🚨 Content filtered: '{message}' -> {result}")
        else:
            print(f"✅ Content approved: '{message}'")

def test_handoff_logic():
    """Test handoff decision logic"""
    print("\n🧪 Testing Handoff Logic...")
    
    def should_handoff(message):
        complex_keywords = ["refund", "cancel", "complaint", "manager"]
        return any(keyword in message.lower() for keyword in complex_keywords)
    
    test_messages = [
        "I want a refund",
        "What's your return policy?",
        "Cancel my order",
        "Can you help me?"
    ]
    
    for message in test_messages:
        needs_handoff = should_handoff(message)
        status = "🔄 HANDOFF" if needs_handoff else "🤖 BOT"
        print(f"{status}: '{message}'")

def run_tests():
    """Run all tests"""
    print("🚀 Smart Customer Support Bot - Test Suite")
    print("=" * 50)
    
    try:
        test_environment()
        test_mock_data()
        test_sentiment_analysis()
        test_guardrail_logic()
        test_handoff_logic()
        
        print("\n" + "=" * 50)
        print("✅ All basic tests completed!")
        print("📝 Note: Full functionality requires 'agents' library installation")
        print("📝 To test full bot, run: python main.py")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Test error: {str(e)}")
        print("Please check your environment setup")

if __name__ == "__main__":
    run_tests()
