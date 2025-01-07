import asyncio
from telethon.sync import TelegramClient
from telethon import errors
from telethon.errors import FloodWaitError


class TelegramForwarder:
    def __init__(self, api_id, api_hash, phone_number):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.client = TelegramClient('session_' + phone_number, api_id, api_hash)

    async def forward_messages_to_channel(self, source_chat_id, destination_channel_id):
        await self.client.connect()

        # Ensure you're authorized
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            await self.client.sign_in(self.phone_number, input('Enter the code: '))

        async for message in self.client.iter_messages(source_chat_id, reverse=True):
            try:
                await self.client.forward_messages(entity=destination_channel_id,messages=message.id,from_peer=source_chat_id,drop_author=True,)
                print(f"Message forwarded           ID: {message.id}          StrinGhost")
                await asyncio.sleep(0.2)  # Adjust the delay time as needed
            except  errors.FloodWaitError as e:
                print(f"Rate limited. Waiting for {e.seconds} seconds...")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Error forwarding message (ID: {message.id}): {e}")

        print("All messages forwarded successfully!")
        


# Function to read credentials from file
def read_credentials():
    try:
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
            api_id = lines[0].strip()
            api_hash = lines[1].strip()
            phone_number = lines[2].strip()
            return api_id, api_hash, phone_number
    except FileNotFoundError:
        print("Credentials file not found.")
        return None, None, None

# Function to write credentials to file
def write_credentials(api_id, api_hash, phone_number):
    with open("credentials.txt", "w") as file:
        file.write(api_id + "\n")
        file.write(api_hash + "\n")
        file.write(phone_number + "\n")

async def main():
    # Attempt to read credentials from file
    api_id, api_hash, phone_number = read_credentials()

    # If credentials not found in file, prompt the user to input them
    if api_id is None or api_hash is None or phone_number is None:
        api_id = input("Enter your API ID: ")
        api_hash = input("Enter your API Hash: ")
        phone_number = input("Enter your phone number: ")
        # Write credentials to file for future use
        write_credentials(api_id, api_hash, phone_number)

    forwarder = TelegramForwarder(api_id, api_hash, phone_number)

    source_chat_id = int(input("Enter the source chat ID: "))
    destination_channel_id = int(input("Enter the destination chat ID: "))
        
    await forwarder.forward_messages_to_channel(source_chat_id, destination_channel_id)

# Start the event loop and run the main function
if __name__ == "__main__":
    asyncio.run(main())