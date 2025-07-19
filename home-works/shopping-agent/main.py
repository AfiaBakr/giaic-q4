from agents import Agent, Runner, function_tool
from connection import config
import requests
import rich



@function_tool
def get_product_items():
    url="https://template6-six.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return products
    except requests.RequestException as e:
        return {"error": str(e)}
    
agent = Agent(
    name= "Shopping Agent",
    instructions="You are a helpful shopping agent. Show all products with detais from available list and suggest one that seems generally useful or appealing",
    tools=[get_product_items]
)

result = Runner.run_sync(
    agent,
    input="I want to see all products with title and price and guide me Which Product you want to buy?",
    run_config= config
)

rich.print(result.final_output)