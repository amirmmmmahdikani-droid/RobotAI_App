"""
Robot AI Configuration
"""

# --------------------------
# Owner
# --------------------------

OWNER_NAME = "امیر"
OWNER_PASSWORD = "1247"

PRIVATE_MODE = True

# --------------------------
# Robot
# --------------------------

ROBOT_NAME = "Tobi"

ROBOT_VERSION = "1.0"

LANGUAGE = "fa"

# --------------------------
# AI
# --------------------------

AI_PROVIDER = "openai"

API_KEY = ""

MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = f"""
تو {ROBOT_NAME} هستی.

صاحب تو {OWNER_NAME} است.

اگر کسی درباره صاحب سوال کرد و حالت صاحب فعال نبود،
اطلاعات خصوصی را نگو.

اگر سوال ساده بود
کوتاه جواب بده.

اگر سوال علمی بود
کامل جواب بده.

همیشه فارسی صحبت کن.
"""

# --------------------------
# Memory
# --------------------------

MEMORY_FILE = "memory.txt"

MAX_MEMORY_LINES = 1000

# --------------------------
# ESP32
# --------------------------

ESP32_ENABLED = True

ESP32_IP = "192.168.4.1"

ESP32_PORT = 80

REQUEST_TIMEOUT = 5

# --------------------------
# Voice
# --------------------------

VOICE_ENABLED = True

VOICE_LANGUAGE = "fa"

# --------------------------
# Offline
# --------------------------

OFFLINE_ENABLED = True

# --------------------------
# Network
# --------------------------

INTERNET_TIMEOUT = 20

# --------------------------
# Debug
# --------------------------

DEBUG = True
