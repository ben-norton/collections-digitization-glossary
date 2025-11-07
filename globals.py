import os
from datetime import date
from pathlib import Path

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))

def get_source_root() -> Path:
    return Path(get_project_root(), "data")

def get_today():
    today = date.today()
    ts = today.strftime("%Y%m%d")
    return ts

def get_latest_glossary_file() -> Path:
    return Path(get_project_root(), "data/sources/digitization-glossary-20251107.csv")

def get_latest_sources_file() -> Path:
    return Path(get_project_root(), "data/sources/digitization-glossary-sources-20251105.csv")

def get_latest_glossary_text_file() -> Path:
    return Path(get_project_root(), "data/collections-digitization-glossary_20251107.txt")