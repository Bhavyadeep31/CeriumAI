import openai
import discord
from discord import app_commands
from discord.ext import commands

class Ask_AI(commands.Cog):
    def __init__(self, ceriumAI):
        self.ceriumAI = ceriumAI
        openai.api_key = "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"
        self.messages = [{"role": "system","content":"You are a intelligent assistant."}]
    
    @app_commands.command(name="askai")
    async def ask_ai(self, interaction: discord.Interaction, query: str):
        while True:
            await interaction.response.defer(ephemeral=True)
            message = query
            if message:
                self.messages.append(
                    {"role": "user", "content": message}
                )
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=self.messages
                )
            reply = chat.choices[0].message.content
            await interaction.followup.send(f"{reply}")
            self.messages.append({"role": "r", "content": reply})
                

async def setup(bot):
    await bot.add_cog(Ask_AI(bot))