import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class that reads environment variables to set various settings.
    """

    def __init__(self):
        self.API_ID: int = int(os.environ.get("API_ID", 26604254))
        self.API_HASH: str = os.environ.get(
            "API_HASH", "3195acbac32b27313e816afa8e5b3a3d"
        )
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7682816102:AAHuSkkf43uvBHOOsfMPd1aNJEiv9JtDAhA")
        self.OWNER_ID: int = int(os.environ.get("OWNER_ID", 1748933027))
        self.MONGODB_URL: str = os.environ.get(
            "MONGODB_URL", "mongodb+srv://royalinhere:1234@cluster0.twkrr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        )
        self.DATABASE_CHAT_ID: int = int(os.environ.get("DATABASE_CHAT_ID", -1002414990605))
        self.OWNER_USERNAME: str = os.environ.get("OWNER_USERNAME", "lordpuhh")

        # Perform validation
        self._validate()

    def _validate(self):
        """
        Validate environment variables to ensure they are correct.
        """
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN: Missed")


config: Config = Config()
