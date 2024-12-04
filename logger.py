import logging
from logging.handlers import RotatingFileHandler

# Log configuration
log_file = 'logs/app.log'

# Create a rotating file handler
handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Configure the logger
logger = logging.getLogger('todo_cli_app')
logger.setLevel(logging.INFO)
logger.addHandler(handler)
