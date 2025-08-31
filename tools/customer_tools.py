"""
Function Tools for Customer Support Bot
Following teacher's pattern with @function_tool decorator
"""
from agents import function_tool, RunContextWrapper
from typing import Dict, Any
import logging

# Setup logging following teacher's pattern
logger = logging.getLogger(__name__)

# Mock order database
ORDERS_DB = {
    "ORD001": {"status": "delivered", "tracking": "TRK123456", "date": "2025-08-25", "amount": "$89.99"},
    "ORD002": {"status": "shipped", "tracking": "TRK789012", "date": "2025-08-28", "amount": "$156.50"},  
    "ORD003": {"status": "processing", "tracking": None, "date": "2025-08-30", "amount": "$234.00"},
    "ORD004": {"status": "pending", "tracking": None, "date": "2025-08-31", "amount": "$67.25"},
    "ORD005": {"status": "cancelled", "tracking": None, "date": "2025-08-29", "amount": "$123.75"}
}

# FAQ database
FAQ_DB = {
    "return_policy": "Our return policy allows returns within 30 days of purchase with original receipt.",
    "shipping_time": "Standard shipping takes 3-5 business days, express shipping takes 1-2 business days.",
    "payment_methods": "We accept Visa, MasterCard, American Express, PayPal, and Apple Pay.",
    "warranty": "All products come with a 1-year manufacturer warranty.",
    "contact_hours": "Customer service is available Monday-Friday 9AM-6PM EST.",
    "store_locations": "We have stores in New York, Los Angeles, Chicago, and Miami."
}

# Function to check if order tool should be enabled
def enable_order_tool(ctx: RunContextWrapper, agent) -> bool:
    """Enable order tool only when user mentions order-related keywords"""
    user_message = ctx.context.get("user_message", "").lower() if hasattr(ctx, 'context') else ""
    order_keywords = ["order", "track", "status", "shipped", "delivery", "ord"]
    return any(keyword in user_message for keyword in order_keywords)

@function_tool(
    name_override="get_order_status",
    description_override="Get order status and tracking information for a given order ID",
    is_enabled=enable_order_tool
)
def get_order_status(order_id: str) -> Dict[str, Any]:
    """
    Fetch order status from mock database
    Uses is_enabled parameter following teacher's pattern
    """
    logger.info(f"Tool invocation: get_order_status for order_id={order_id}")
    
    # Normalize order ID
    order_id = order_id.upper().strip()
    
    if order_id in ORDERS_DB:
        order_info = ORDERS_DB[order_id]
        result = {
            "order_id": order_id,
            "status": order_info["status"],
            "tracking_number": order_info.get("tracking"),
            "order_date": order_info["date"],
            "amount": order_info["amount"],
            "found": True
        }
        logger.info(f"Order found: {result}")
        return result
    else:
        # This will trigger the error function
        raise ValueError(f"Order {order_id} not found in our system")

# Error function for order lookup failures
def order_lookup_error(ctx: RunContextWrapper, error: Exception) -> str:
    """
    Error function for order lookup failures
    Following teacher's pattern for error handling
    """
    logger.warning(f"Order lookup error: {str(error)}")
    return f"I'm sorry, but I couldn't find that order. Please check the order ID and try again. Order IDs typically start with 'ORD' followed by numbers (e.g., ORD001)."

# Note: Error handling is managed within the function itself by raising exceptions

@function_tool(
    name_override="search_faq", 
    description_override="Search FAQ database for answers to common customer questions"
)
def search_faq(query: str) -> Dict[str, Any]:
    """
    Search FAQ database for relevant information
    """
    logger.info(f"Tool invocation: search_faq for query='{query}'")
    
    query_lower = query.lower()
    results = []
    
    # Search through FAQ database
    for key, answer in FAQ_DB.items():
        if any(word in key for word in query_lower.split()) or any(word in answer.lower() for word in query_lower.split()):
            results.append({"topic": key.replace("_", " ").title(), "answer": answer})
    
    if results:
        logger.info(f"FAQ results found: {len(results)} matches")
        return {"found": True, "results": results}
    else:
        logger.info("No FAQ results found")
        return {"found": False, "message": "No relevant FAQ found for your query."}
