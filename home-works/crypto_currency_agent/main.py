import requests
from connection import config
from agents import Agent, Runner, function_tool

@function_tool
def get_crypto_price():

    digital_coin =requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return digital_coin.text


agent = Agent(
    name = "Digital Data",
    instructions="""
    You provide real-time crypto prices using the Binance API""",
    tools =[get_crypto_price]
)

result = Runner.run_sync(
    agent,
    input="what is the price of one BTCUSDT in USD.",
    run_config=config
)

print(result.final_output)
