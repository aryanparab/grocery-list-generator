from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.exa import ExaTools
import streamlit as st

def cooker(prompt):
    
    md = Gemini(id="gemini-2.0-flash")
    # md = Groq(id="deepseek-r1-distill-llama-70b")
    chef_agent =Agent(
        description="You are a master chef. You will be given a grocery list and a prompt based on which you have to create a meal plan for the specified duration.",
        model = md,
        name = "Chef",
        instructions=[
            "You are a professional chef. Your task is to create a meal plan based on a grocery list",
            "You will be provided a prompt only with grocery list.",
            "Prompt will contain the duration in weeks, ensure that all ingredients are used efficiently and the user need not buy anything extra before end of duration",
            "Prompt will specify the meals(that is lunch, breakfast and dinner). See to it that the ingredients are well managed",
            "The prompt will specify the type of cuisines. If there are multiple, ensure that all cusines have some sort of reciepes",
            "Your meal plan should provide receipe for the specified meals, everyday of the week for the given duration; like a calendar"
            "Provide some cooking instructions and also ingredients required",
            "Make some rewarding days (1 in 10 days) for eg a big recipe or something special for eat ",
            "If some ingredients can make a dish better, do include. (Only do this for 1 in 10 dishes)",
            "Label Days as days of week."
        ]
    )
    with st.status("Cooking something special...", expanded=True) as status:
        response= chef_agent.run(prompt, stream=False)
        status.update(
        label="It's time!!", state="complete", expanded=False
        )

    return str(response.content)
