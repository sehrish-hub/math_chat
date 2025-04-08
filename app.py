import chainlit as cl
from gmath import solve_math_problem, explain_math_solution, check_math_solution, generate_practice_question

@cl.on_chat_start
async def start():
    cl.user_session.set("history", []) # Initialize empty history
    await cl.Message(content="Welcome to the Math Chatbot! Ask me any math question or type 'practice' for a practice problem.").send()

@cl.on_message
async def process_message(message):
    """Handles user messages and provides math solutions or practice problems."""
    user_input = message.content.strip().lower()
    history = cl.user_session.get("history") # Get current history
    
    # Add user message to history
    history.append({"role": "user", "content": user_input})

    if "practice" in user_input:
        practice_problem = generate_practice_question()
        response = f"Practice Question:\n{practice_problem}"
    else:
        solution = solve_math_problem(user_input)
        response = f"Solution:\n{solution}"
    
    # Add bot response to history
    history.append({"role": "assistant", "content": response})
    
    # Update the session history
    cl.user_session.set("history", history)
    
    # Send response to user
    await cl.Message(content=response).send()

# import chainlit as cl 
# from agents import Agent,  RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
# from dotenv import load_dotenv, find_dotenv
# import os
# load_dotenv(find_dotenv())
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# provider = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=provider,
# )

# run_config = RunConfig(
#     model=model,
#     model_provider=provider,
#     tracing_disabled=True
# )

# agent1 = Agent(
#     instructions="you are a helpful assistant that can answer questions",
#     name="panaversity support agent"
# )

# @cl.on_chat_start
# async def handle_chat_start():
#     """Initialize chat history when conversation starts."""
#     cl.user_session.set("history", []) # Clear session history
#     await cl.Message(
#         content="Hello! I am the panaversity support agent. How can I help you today?",
#     ).send()

# @cl.on_message
# async def handle_message(message: cl.Message):
#     """Handle incoming user messages and generate AI responses."""
     
#     # history = cl.user_session.get("history", [])
#     history = cl.user_session.get("history")# Retrieve history (or initialize if None)
#     history.append({"role": "user", "content": message.content}) # Append user message to history
    
#     # Run AI agent
#     result = await Runner.run(
#         # agent1,
#         input=history,# Send only user messages
#         run_config=run_config,
#         starting_agent=agent1 # Agent should be passed first
#     )
    
#     history.append({"role": "assistant", "content": result.final_output})# Add AI response to history 
    
#     cl.user_session.set("history", history) # Update session history for next turn
#      # Send latest AI response
#     await cl.Message(
#         content=result.final_output,
#     ).send()