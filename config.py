from pathlib import Path
NECCESARY_COLUMNS = ["timestamp", "sala", "temperatura","humedad","co2"]





BASE_DIR = Path(__file__).parent.resolve()
DATA_PATH = BASE_DIR / "data"

CSV_PATH = DATA_PATH / "logs_ambientales_ecowatch.csv"

EXTRACTION_PATHS = [
    {'extension':'csv', 'path' : CSV_PATH}
]