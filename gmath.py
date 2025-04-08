import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
 
def solve_math_problem(problem):
    prompt = f"Solve the following math problem: {problem}"
    response = model.generate_content(prompt)
    return response.text
def explain_math_solution(problem, solution):
    prompt = f"Explain the solution to the following math problem: {problem}\n\nSolution: {solution}"
    response = model.generate_content(prompt)
    return response.text
def check_math_solution(problem, solution):
    prompt = f"Check if the following solution is correct for the math problem: {problem}\n\nSolution: {solution}"
    response = model.generate_content(prompt)
    return response.text
def generate_practice_question():
    """Generates a math practice problem using AI."""
    prompt = f"Generate a unique math problem for students to practice."
    response = model.generate_content(prompt)
    return response.text




