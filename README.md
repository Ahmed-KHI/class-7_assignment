# Smart Customer Support Bot

A comprehensive customer support bot built using OpenAI Agent SDK, following advanced patterns for function tools, guardrails, handoffs, and ModelSettings.

## 🎯 Assignment Requirements

This project fulfills all assignment requirements:

### ✅ 1. Two Agents
- **BotAgent**: Handles FAQs, order lookup using function tools
- **HumanAgent**: For escalation and complex issues

### ✅ 2. Function Tools with Advanced Features
- `@function_tool` decorator with `is_enabled` parameter
- `error_function` for graceful error handling
- Order status lookup and FAQ search tools

### ✅ 3. Guardrails
- `@guardrail` decorator for content filtering
- Blocks offensive/negative language
- Provides professional responses

### ✅ 4. Agent Handoff
- `@handoff` decorator for escalation
- Automatic handoff for complex queries
- Sentiment-based handoff triggers

### ✅ 5. ModelSettings Usage
- `tool_choice="auto"` configuration
- Custom `metadata` with customer info
- Session tracking and analytics

### ✅ 6. Comprehensive Logging
- Tool invocation logging
- Handoff event logging
- Error tracking and debugging

## 📁 Project Structure

```
class-7_assignment/
├── main.py                    # Main bot implementation
├── config/
│   └── gemini_config.py      # Gemini API configuration
├── tools/
│   └── customer_tools.py     # Function tools implementation
├── agents_package/
│   └── customer_agents.py    # Agent definitions
├── guardrails/
│   └── content_guardrails.py # Guardrail implementations
├── requirements.txt          # Dependencies
├── .env.example             # Environment template
└── README.md               # This file
```

## 🛠️ Features Demonstrated

### Function Tools
```python
@function_tool(
    name_override="get_order_status",
    description_override="Get order status and tracking information",
    is_enabled=enable_order_tool  
)
def get_order_status(order_id: str) -> Dict[str, Any]:
    
```

### Guardrails
```python
@guardrail(description="Block or rephrase negative/offensive user input")
def content_filter_guardrail(ctx: RunContextWrapper) -> Optional[str]:
    
```

### Handoffs
```python
transfer_to_human = handoff(
    agent=human_support_agent,
    tool_name_override="transfer_to_human_support",
    on_handoff=on_handoff_to_human
)
```

### ModelSettings
```python
model_settings = ModelSettings(
    tool_choice="auto",  
    metadata={
        "customer_id": customer_id,
        "session_id": session_id,
        "sentiment": sentiment_analysis
    }
)
```

## 🎮 Demo Scenarios

The bot includes 6 comprehensive test scenarios:

1. **Valid Order Lookup** - Tests function tools with `is_enabled`
2. **FAQ Search** - Tests knowledge base search
3. **Offensive Language** - Tests guardrail functionality  
4. **Complex Query** - Tests handoff mechanism
5. **Invalid Order** - Tests error function handling
6. **Multiple FAQ** - Tests ModelSettings with metadata

## 🔍 Key Implementation Highlights

### Following Teacher's Patterns
- Uses `agents` library with proper imports
- Gemini API integration following class patterns
- Proper error handling and logging
- Structured project organization

### Advanced OpenAI Agent SDK Features
- **is_enabled functions** for conditional tool availability
- **error_function** for graceful error handling
- **Custom guardrails** for content filtering
- **Handoff mechanisms** with callback functions
- **ModelSettings** with tool_choice and metadata
- **Comprehensive logging** for debugging and analytics

### Production-Ready Features
- Environment variable configuration
- Comprehensive error handling
- Logging and monitoring
- Modular code structure
- Documentation and comments

## 📊 Logging Output

The bot provides detailed logging:
```
2025-08-31 - customer_support_bot - INFO - 🔧 Tool invocation: get_order_status for order_id=ORD002
2025-08-31 - customer_support_bot - INFO - ✅ Order found: {'order_id': 'ORD002', 'status': 'shipped'}
2025-08-31 - customer_support_bot - INFO - 🔄 Handoff to human support agent initiated
```

## 🎓 Educational Value

This implementation demonstrates:
- Advanced Agent SDK patterns
- Production-ready code structure
- Comprehensive error handling
- Logging and monitoring best practices
- Following established patterns and conventions

## 🤖 Author

Built following teacher's methodology from the agenticai_thursday_classcode repository, implementing all assignment requirements with advanced OpenAI Agent SDK features.
