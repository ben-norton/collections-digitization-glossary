from pathlib import Path
import pandas as pd
import shutil
import datetime
import globals as cfg

root_dir = cfg.get_project_root()
source_glossary_filename = 'digitization-glossary_20251002.csv'
source_sources_filename = 'digitization-glossary-sources-20251002.csv'

today = datetime.date.today()
ts = today.strftime("%Y%m%d")

# -------------------------------------------------------
# Create copies
source_path = str(root_dir) + '/sources/'

# Glossary Copy
glossary_src = str(source_path) + '/original/' + source_glossary_filename
glossary_csv = str(root_dir) + '/web/app/data/glossary-entries.csv'
shutil.copy(glossary_src , glossary_csv)

# Copy Sources
sources_src = str(source_path) + '/original/' + source_sources_filename
target_sources_csv = str(root_dir) + '/web/app/data/glossary-sources.csv'
shutil.copy(glossary_src , target_sources_csv)

# ---------------------------------------------------
# Glossary

glossary_df = pd.read_csv(glossary_csv, encoding="utf8")
glossary_df.columns = map(str.lower, glossary_df.columns)
glossary_df['last_modified'] = ts
glossary_df.to_csv(glossary_csv, index=False, encoding='utf-8')
#print(glossary_df.infer_objects().dtypes)
#print(glossary_df.dtypes.to_dict())

sources_df = pd.read_csv(sources_src, encoding="utf8")
sources_df.columns = map(str.lower, sources_df.columns)
glossary_df['last_modified'] = ts
sources_df.to_csv(target_sources_csv, index=False, encoding='utf-8')
#print(sources_df.infer_objects().dtypes)
#print(sources_df.dtypes.to_dict())

