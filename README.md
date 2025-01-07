# Telegram Autoforwarder
The Telegram Autoforwarder is a simple Telethon based Python script to forward all the messages from one (group/channel) to another (group/channel). It works with both groups and channels, requiring only the necessary permissions to access the messages.

## Features

- Forward all messages from one chat to another.
- Forwards Files, Videos, Images with ease.
- Works with both groups and channels.
- Forwarded Tag is hidden by default.
- Simple setup and usage.

## How it Works

The script uses the Telethon library to interact with the Telegram API. You provide the script with your Telegram API ID, API hash, and phone number for authentication. Once configured, the script continuously checks for messages in the specified source chat and forwards them to the destination chat from oldest to newest messages.

## Setup and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/StrinGhost/Telegram-Auto-Forwarder.git
   cd Telegram-Auto-Forwarder
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the script:

   - Open `TeleForwarder.py` file and provide your Telegram API ID, API hash, and phone number in the appropriate variables.
   - Modify other settings as needed directly in the script.

4. Run the script:

   ```bash
   python TeleForwarder.py
   ```
   
## Notes

- Remember to keep your API credentials secure and do not share them publicly.
- Ensure that you have the necessary permissions to access messages in the chats you want to use.
- Adjust the script's behavior and settings according to your requirements.

## License
This project is licensed under the MIT License.

### Acknowledgment
This project is based on work from the original repository:  
[Telegram-Autoforwarder](https://github.com/redianmarku/Telegram-Autoforwarder.git) by [redianmarku](https://github.com/redianmarku).
