from openai import Agent, Runner, function_tool, input_guardrail, RunContextWrapper
from pydantic import BaseModel

# --------------------------
# Step 1: User Context
# --------------------------
class UserContext(BaseModel):
    name: str
    member_id: str | None = None

# --------------------------
# Step 2: Fake Book Database
# --------------------------
BOOKS_DB = {
    "Harry Potter": 3,
    "Quran": 5,
    "Python 101": 2
}

# --------------------------
# Step 3: Tools
# --------------------------
@function_tool
def search_book(book_name: str) -> str:
    """Search if a book exists in the library"""
    return "✅ Found in library" if book_name in BOOKS_DB else "❌ Not available"

@function_tool
def check_availability(book_name: str, member_id: str) -> str:
    """Check copies of a book (only for valid members)"""
    if not member_id or member_id.strip() == "":
        return "🚫 Only registered members can check availability."
    return f"📚 Copies available: {BOOKS_DB.get(book_name, 0)}"

@function_tool
def library_timings() -> str:
    """Return library timings"""
    return "⏰ Library open from 9 AM to 8 PM (Mon-Sat). Closed on Sunday."

# --------------------------
# Step 4: Guardrail Agent
# --------------------------
guardrail_agent = Agent(
    name="GuardrailAgent",
    instructions="Reject queries unrelated to the library. Only answer library-related queries."
)

@input_guardrail
def guard_input(user_query: str) -> bool:
    non_library_keywords = ["weather", "news", "movies"]
    return not any(word in user_query.lower() for word in non_library_keywords)

# --------------------------
# Step 5: Dynamic Instructions
# --------------------------
def dynamic_instruction(ctx: RunContextWrapper):
    user: UserContext = ctx.user_context
    return f"You are helping {user.name}. Be polite and concise."

# --------------------------
# Step 6: Library Agent
# --------------------------
library_agent = Agent(
    name="LibraryAssistant",
    instructions="You are a helpful library assistant.",
    model_settings={"model": "gpt-4.1-mini"},
    tools=[search_book, check_availability, library_timings],
    guardrails=[guard_input],
    dynamic_instruction=dynamic_instruction
)

# --------------------------
# Step 7: Runner
# --------------------------
runner = Runner(library_agent)

# --------------------------
# Step 8: Test Queries
# --------------------------
if __name__ == "__main__":
    user = UserContext(name="Ali", member_id="12345")
    
    queries = [
        "Search Harry Potter",
        "Check availability for Quran",
        "What are the library timings?",
        "Tell me today's weather"  # Should be rejected
    ]
    
    for q in queries:
        print(f"\n👉 Query: {q}")
        result = runner.run_sync(q, user_context=user)
        print("🤖 Response:", result.output_text)
