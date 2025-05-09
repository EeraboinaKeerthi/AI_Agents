from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()

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

multi_ai_agent =Agent(
    team = [ web_search_agent,finance_agent],
    instructions= ["Provide sources from where information is gathered","Use tables to display data"],
    show_tools_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA ",stream =True)