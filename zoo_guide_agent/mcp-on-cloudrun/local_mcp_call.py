import asyncio
from fastmcp import Client
from google.cloud import logging


# Initialize the client
client = logging.Client()

# Create a custom logger for activity tracking
logger = client.logger("mcp-log-data") 

client = Client("http://localhost:8080/mcp")

async def call_tool(species: str):
    async with client:
        result = await client.call_tool("fetch_animals_by_species", {"species": species})        
        # Do not change — used for activity tracking.
        logger.log_text(
            f"MCP agent result: {result}"    
        )      
        print(result)  
        
asyncio.run(call_tool("walrus"))