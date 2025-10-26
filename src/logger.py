import logging
import os
from datetime import datetime

# Log file
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] [Line: %(lineno)d] - %(message)s",
    level=logging.INFO
)


