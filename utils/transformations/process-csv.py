from pathlib import Path
import pandas as pd
import shutil
import globals
import glob
import yaml
from datetime import date
import globals as cfg

root_dir = cfg.get_project_root()
source_glossary_filename = 'digitization-glossary_20251002.csv'
source_sources_filename = 'digitization-glossary-sources-20251002.csv'

today = date.today()
ts = today.strftime("%Y%m%d")

# -------------------------------------------------------
# Create copies
source_path = str(root_dir) + '/sources/'

# Glossary Copy
glossary_src = str(source_path) + '/original/' + source_glossary_filename
glossary_csv = str(source_path) + '/output/glossary.csv'
shutil.copy(glossary_src , glossary_csv)

# Copy Sources
sources_src = str(source_path) + '/original/' + source_sources_filename
sources_csv = str(source_path) + '/output/sources.csv'
shutil.copy(glossary_src , sources_csv)

# ---------------------------------------------------
# Glossary
glossary_df = pd.read_csv(glossary_csv, encoding="utf8")
print(glossary_df.infer_objects().dtypes)
print(glossary_df.dtypes.to_dict())

sources_df = pd.read_csv(sources_csv, encoding="utf8")
print(sources_df.infer_objects().dtypes)
print(sources_df.dtypes.to_dict())

