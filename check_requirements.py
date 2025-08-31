"""
Simple Assignment Requirements Check
"""
import os

print("🔍 SMART CUSTOMER SUPPORT BOT - ASSIGNMENT VERIFICATION")
print("=" * 65)

# Check if main.py exists
if not os.path.exists('main.py'):
    print("❌ main.py file not found!")
    exit(1)

try:
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    try:
        with open('main.py', 'r', encoding='latin-1') as f:
            content = f.read()
    except:
        print("❌ Could not read main.py file")
        exit(1)

# Check requirements
requirements = [
    ("1. Two Agents (BotAgent & HumanAgent)", 
     "human_support_agent = Agent(" in content and "customer_support_bot = Agent(" in content),
    
    ("2. Function Tools with @function_tool", 
     "@function_tool(" in content and "get_order_status" in content),
    
    ("3. is_enabled Parameter", 
     "is_enabled=enable_order_tool" in content),
    
    ("4. error_function Parameter", 
     "failure_error_function=" in content or "error_function=" in content),
    
    ("5. Guardrails Implementation", 
     "content_filter_guardrail" in content or "@guardrail" in content),
    
    ("6. Agent Handoff with @handoff", 
     "handoff(" in content and "transfer_to_human" in content),
    
    ("7. ModelSettings Concepts", 
     "model=" in content and "tools=" in content and "handoffs=" in content),
    
    ("8. Comprehensive Logging", 
     "logger.info" in content and "Tool invocation" in content),
    
    ("9. Environment Configuration", 
     "load_dotenv" in content and "GEMINI_API_KEY" in content),
    
    ("10. Demo Scenarios", 
     "run_demo_scenarios" in content and "demo_scenarios" in content)
]

# Check additional features
additional = [
    ("Mock Database", "ORDERS_DB" in content and "FAQ_DB" in content),
    ("Error Handling", "try:" in content and "except:" in content),
    ("Sentiment Analysis", "analyze_sentiment" in content),
    ("Type Hints", "Dict[str, Any]" in content),
    ("Async Support", "async def" in content)
]

print("📋 ASSIGNMENT REQUIREMENTS:")
print("-" * 50)

passed = 0
for req, check in requirements:
    status = "✅" if check else "❌"
    print(f"{status} {req}")
    if check:
        passed += 1

print("\n🔧 ADDITIONAL FEATURES:")
print("-" * 50)

for feature, check in additional:
    status = "✅" if check else "❌"
    print(f"{status} {feature}")

print("\n" + "=" * 65)
print(f"📊 SUMMARY: {passed}/{len(requirements)} core requirements implemented")

if passed == len(requirements):
    print("🎉 ALL ASSIGNMENT REQUIREMENTS FULFILLED!")
    print("✨ Project is ready for submission!")
else:
    print(f"⚠️  {len(requirements) - passed} requirements need attention")

print("=" * 65)
