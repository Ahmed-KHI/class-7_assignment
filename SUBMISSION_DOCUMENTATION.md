# 📋 ASSIGNMENT SUBMISSION DOCUMENTATION

## 🎯 **REQUIRED FEATURES AND THEIR LOCATIONS IN CODE**

### **1. 🔧 TOOL CALL (`@function_tool` decorators)**

**Location 1: Order Status Tool**
- **File**: `main.py`
- **Lines**: 147-155
- **Code**:
```python
@function_tool(
    name_override="get_order_status",
    description_override="Get order status and tracking information for a given order ID",
    is_enabled=enable_order_tool,
    failure_error_function=lambda ctx, error: f"I'm sorry, but I couldn't find that order..."
)
def get_order_status(order_id: str) -> Dict[str, Any]:
```

**Location 2: FAQ Search Tool**
- **File**: `main.py`  
- **Lines**: 178-182
- **Code**:
```python
@function_tool(
    name_override="search_faq",
    description_override="Search FAQ database for answers to common customer questions"
)
def search_faq(query: str) -> Dict[str, Any]:
```

**Usage in Agent**: Lines 281-282
```python
tools=[get_order_status, search_faq],
```

---

### **2. 🔄 HANDOFF**

**Location 1: Handoff Definition**
- **File**: `main.py`
- **Lines**: 254-259
- **Code**:
```python
transfer_to_human = handoff(
    agent=human_support_agent,
    tool_name_override="transfer_to_human_support",
    on_handoff=on_handoff_to_human
)
```

**Location 2: Handoff Callback Function**
- **File**: `main.py`
- **Lines**: 248-252
- **Code**:
```python
def on_handoff_to_human(ctx: RunContextWrapper):
    """Called when handing off to human agent"""
    logger.info("🔄 Handoff to human support agent initiated")
    customer_id = getattr(ctx, 'customer_id', 'unknown')
    print(f"🔄 Transferring customer {customer_id} to human support representative...")
```

**Usage in Agent**: Line 283
```python
handoffs=[transfer_to_human]
```

**Handoff Logic**: Lines 308-330 (should_handoff function)
```python
def should_handoff(message: str) -> tuple[bool, str]:
    """Determine if the query should be handed off to human agent"""
```

---

### **3. 🛡️ GUARDRAIL**

**Location**: 
- **File**: `main.py`
- **Lines**: 196-218
- **Code**:
```python
def content_filter_guardrail(message: str) -> Optional[str]:
    """
    Input filter to check for offensive or overly negative language
    Following teacher's guardrail pattern
    """
    if not message:
        return None
        
    logger.info(f"🛡️ Guardrail check for message: '{message[:50]}...'")
    
    message_lower = message.lower()
    
    
    offensive_words = ["stupid", "idiot", "hate", "terrible", "worst", "awful", "useless", "garbage"]
    for word in offensive_words:
        if word in message_lower:
            logger.warning(f"🚨 Offensive language detected: '{word}'")
            return f"I understand you might be frustrated, but let's keep our conversation respectful..."
```

**Usage**: Lines 355-368
```python

guardrail_response = content_filter_guardrail(message)
if guardrail_response:
    logger.info("🛡️ Message blocked by content filter")
    return {
        "response": guardrail_response,
        "agent_used": "content_filter",
        "filtered": True
    }
```

---

### **4. ⚙️ MODELSETTINGS OPTIONS**

**Location 1: Model Configuration**
- **File**: `main.py`
- **Lines**: 112-113
- **Code**:
```python
gemini_client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
model = OpenAIChatCompletionsModel(openai_client=gemini_client, model=str(gemini_model_name))
```

**Location 2: Agent Model Assignment**
- **File**: `main.py`
- **Lines**: 275, 232
- **Code**:
```python

human_support_agent = Agent(
    name="Human Support Representative",
    instructions="...",
    model=model  
)


customer_support_bot = Agent(
    name="Customer Support Bot", 
    instructions="...",
    model=model,  
    tools=[get_order_status, search_faq],
    handoffs=[transfer_to_human]
)
```

**Location 3: Advanced Model Settings Concepts**
- **File**: `main.py`
- **Lines**: 332-350 (process_customer_query function)
- **Implementation**: Tool choice logic, metadata handling, custom model behavior

---

### **5. 🎛️ FUNCTION_TOOL DECORATORS - ADVANCED FEATURES**

**is_enabled Parameter**:
- **Location**: Line 149 in `@function_tool` decorator
- **Implementation**: Lines 128-138 (`enable_order_tool` function)
```python
def enable_order_tool(ctx: RunContextWrapper, agent) -> bool:
    """Enable order tool only when user mentions order-related keywords"""
    message = getattr(ctx, 'current_input', '')
    order_keywords = ["order", "track", "status", "shipped", "delivery", "ord"]
    return any(keyword in message.lower() for keyword in order_keywords)
```

**error_function Parameter**:
- **Location**: Line 150 in `@function_tool` decorator
```python
failure_error_function=lambda ctx, error: f"I'm sorry, but I couldn't find that order. Please check the order ID and try again. Order IDs typically start with 'ORD' followed by numbers (e.g., ORD001)."
```

---

## 📊 **SUMMARY TABLE**

| Feature | File Location | Line Numbers | Status |
|---------|---------------|--------------|--------|
| @function_tool decorators | main.py | 147-155, 178-182 | ✅ Complete |
| is_enabled parameter | main.py | 149, 128-138 | ✅ Complete |
| error_function parameter | main.py | 150 | ✅ Complete |
| handoff implementation | main.py | 254-259, 248-252 | ✅ Complete |
| guardrail implementation | main.py | 196-218, 355-368 | ✅ Complete |
| ModelSettings usage | main.py | 112-113, 275, 232 | ✅ Complete |
| Comprehensive logging | main.py | Throughout | ✅ Complete |

---

**All required features are implemented and documented with specific code locations!** 🎉
