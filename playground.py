import openai
from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os
import phi
from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

#Web search Agent 
web_search_agent = Agent(
    name="Web Search Agent",
    role = "Search for Information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Provide sources from where information is gathered"],
    show_tools_calls=True,
    markdown=True
)

#Financial Agent
finance_agent = Agent(
    name="Finanace AI Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True),
    ],
    instructions=["Use tables to display data"],
    show_tools_calls=True,
    markdown=True

)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)