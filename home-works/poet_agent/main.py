from agents import Agent, Runner, trace, function_tool
from connection import config
import asyncio
from dotenv import load_dotenv

load_dotenv()
@function_tool
def current_weather():
    return "Sunny"

@function_tool
def current_location():
    return "GH Sindh Karachi"


lyric_poetry_agent = Agent(
    name = 'Lyric poetry Agent',
    instructions="You are a Lyric poetry agent. you analyze  lyric poetry  focusing on feelings and thoughts, like songs or poems about being sad or happy. your task is provide the name of poet first, after analyzing wirte peotry type Lyric. Explain only one para about given stanza to show clearity of stanza. "
)

narrative_poetry_agent = Agent(
    name = "Narrative poetry Agent",
    instructions="You are a Narrative poetry agent. you analyze  Narrative poetry  focusing on  poetry story with characters and events, just like a regular story but written in poem form with rhymes or special rhythm. your task is provide the name of poet first after analyzing wirte peotry type Narrative. Explain only one para about given stanza to show clearity of stanza. ",
    model="gpt3"
)

Dramatic_poetry_agent = Agent(
    name = 'Dramatic poetry Agent',
    instructions="You are a Dramatic poetry agent. you analyze Dramatic poetry focusing on performed out loud, where someone acts like a character and speaks their thoughts and feelings to an audience (acting in a theatre). your task is provide the name of poet first after analyzing wirte peotry type Dramatic. Explain only one para about given stanza to show clearity of stanza."
)


parent_agent = Agent(
    name = "Parent Agent",
    instructions=""" 
        You are a parent agent. Your task is to
        delegate user query to appropriate agent.
        Transfer to Lyric poetry Agent if stanza have feelings and thoughts, like songs or poems about being sad or happy. 
        Transfer to Narrative poetry Agent if stanza have story with characters and events, just like a regular story but written in poem form with rhymes or special rhythm.
        Transfer to Dramatic poetry Agent if stanza have performed out loud, where someone acts like a character and speaks their thoughts and feelings to an audience (acting in a theatre).
        Provide the output to user from approoiate agent
        Any query other than Lyric poetry Agent, Narrative poetry Agent,and Dramatic poetry Agent keep it to 
        yourself and deny the user query.

    """,
    handoffs=[lyric_poetry_agent, narrative_poetry_agent, Dramatic_poetry_agent]
    
)

async def main():
    with trace("poet_agent"):
        result = await Runner.run(
            parent_agent, 
            """             
                That's my last Duchess painted on the wall,
                Looking as if she were alive. I call
                That piece a wonder, now; Fra Pandolf's hands
                Worked busily a day, and there she stands  
            

                 Explain  above Stanza 
            """, 
            run_config=config)
        print(result.final_output)
        print("Last Agent ==> ",result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())


# William Wordsworth
# My Heart Leaps Up" (1802)
# lyric poetry
    # My heart leaps up when I behold
    # A rainbow in the sky:
    # So was it when my life began;
    # So is it now I am a man; 

# Alfred, Lord Tennyson
# The Charge of the Light Brigade" (1854)
# narrative poetry
    # Half a league, half a league,
    # Half a league onward,
    # All in the valley of Death
    # Rode the six hundred

# Robert Browning
# My Last Duchess" (1842)
# dramatic poetry
    # That's my last Duchess painted on the wall,
    # Looking as if she were alive. I call
    # That piece a wonder, now; Fra Pandolf's hands
    # Worked busily a day, and there she stands