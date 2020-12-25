import discord


class PeezyB(discord.client):

    async def on_ready(self):
        print(f"logged in {self.user}")

    async def on_message(self, message):
        print(message.content)

    async def on_voice_state_update(self, user, before, after):
        print(f"before: {before}")
        print(f"after: {after}")
        pass


if __name__ == "__main__":
    client = PeezyB()
    token = open("./token.txt", "r").read()
    client.run('token')



