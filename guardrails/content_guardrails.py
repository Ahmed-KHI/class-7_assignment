"""
Guardrails for Customer Support Bot
Following teacher's pattern for input/output guardrails
"""
from typing import Optional, Any, Callable
import logging
import re

# Simple guardrail decorator to replace the missing import
def guardrail(description: str = "") -> Callable:
    """Simple decorator to mark functions as guardrails"""
    def decorator(func: Callable) -> Callable:
        func.__guardrail_description__ = description
        return func
    return decorator

# Simple context wrapper class to replace the missing import
class RunContextWrapper:
    def __init__(self, context: Optional[dict] = None):
        self.context = context or {}

logger = logging.getLogger(__name__)

# List of inappropriate/offensive words
OFFENSIVE_WORDS = [
    "stupid", "idiot", "hate", "terrible", "worst", "awful", 
    "useless", "garbage", "damn", "crap", "sucks", "fuck", "shit"
]

# Negative sentiment phrases
NEGATIVE_PHRASES = [
    "i hate", "you suck", "this is terrible", "worst service", 
    "complete garbage", "totally useless", "absolutely awful",
    "hate this company", "worst experience"
]

@guardrail(description="Block or rephrase negative/offensive user input")
def content_filter_guardrail(ctx: RunContextWrapper) -> Optional[str]:
    """
    Input guardrail to check for offensive or overly negative language
    Following teacher's guardrail pattern
    """
    # Get user message from context
    user_message = ""
    if hasattr(ctx, 'context') and ctx.context:
        user_message = ctx.context.get("user_message", "")
    
    if not user_message:
        return None
        
    logger.info(f"Guardrail check for message: '{user_message[:50]}...'")
    
    message_lower = user_message.lower()
    
    # Check for offensive words
    for word in OFFENSIVE_WORDS:
        if word in message_lower:
            logger.warning(f"Offensive language detected: '{word}'")
            return f"I understand you might be frustrated, but let's keep our conversation respectful. How can I help you resolve your issue today?"
    
    # Check for negative phrases
    for phrase in NEGATIVE_PHRASES:
        if phrase in message_lower:
            logger.warning(f"Negative phrase detected: '{phrase}'")
            return f"I'm sorry to hear you're having a difficult experience. Let me connect you with someone who can help make this right for you."
    
    # Check for excessive caps (might indicate shouting/anger)
    caps_ratio = sum(1 for c in user_message if c.isupper()) / len(user_message) if user_message else 0
    if caps_ratio > 0.6 and len(user_message) > 10:
        logger.warning("Excessive capitals detected (possible shouting)")
        return "I can see this is important to you. Let me help you resolve this issue. Could you please provide more details about your concern?"
    
    return None

@guardrail(description="Filter output to ensure professional responses")  
def output_filter_guardrail(ctx: RunContextWrapper, response: str) -> Optional[str]:
    """
    Output guardrail to ensure responses remain professional
    Following teacher's pattern for output guardrails
    """
    logger.info("Output guardrail check")
    
    response_lower = response.lower()
    
    # Check if response contains any inappropriate content
    inappropriate_responses = [
        "i don't know", "i can't help", "that's not my job",
        "figure it out yourself", "not my problem"
    ]
    
    for inappropriate in inappropriate_responses:
        if inappropriate in response_lower:
            logger.warning(f"Inappropriate response detected: '{inappropriate}'")
            return "I want to help you with your request. Let me check what options are available or connect you with someone who can better assist you."
    
    # Ensure response doesn't sound too robotic
    if response.count("I am") > 3 or response.count("I can") > 3:
        logger.info("Response might sound too robotic")
        # Could implement response rewriting here
    
    return None  # Allow response to proceed
