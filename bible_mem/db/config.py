from pathlib import Path
import platformdirs

from bible_mem.__version__ import VERSION


APP_NAME = "bible_mem"
DB_NAME = "userdata.sqlite"
DB_PATH = Path(platformdirs.user_data_dir(APP_NAME, False, VERSION)) / DB_NAME
