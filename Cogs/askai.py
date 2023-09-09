import os
import openai
import discord
from discord import app_commands
from discord.ext import commands

openai.api_key = os.getenv("API_TOKEN")

class Ask_AI(commands.Cog):
    def __init__(self, ceriumAI):
        self.ceriumAI = ceriumAI
        
    @app_commands.command(name="askai")
    async def ask_ai(self, interaction: discord.Interaction, *, query: str):
        await interaction.response.send_message(f'CeriumAI is thinking...', ephemeral=False)

        async with interaction.channel.typing():
            bot_response = chatgpt_response(prompt=query)

        await interaction.followup.send(
            f"**Question:**\n\n"
            f"`{query}`\n\n"
            f"**Response:**\n"
            f"{bot_response}", ephemeral=False)

def chatgpt_response(prompt: str):
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.3, max_tokens=1000)

        response_dict = response.get("choices")

        if response_dict and len(response_dict) > 0:
            prompt_response = response_dict[0]["text"]
            return prompt_response

async def setup(bot):
    await bot.add_cog(Ask_AI(bot))