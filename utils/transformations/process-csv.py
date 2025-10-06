from pathlib import Path
import pandas as pd
import shutil
import datetime
import globals as cfg


source_glossary_filename = 'digitization-glossary-20251006.csv'
source_sources_filename = 'digitization-glossary-sources-20251006.csv'

today = datetime.date.today()
ts = today.strftime("%Y%m%d")

# PATHS
root_dir = cfg.get_project_root()
data_root_path = str(root_dir) + '/data'
app_data_path = str(root_dir) + '/app/data'

# -------------------------------------------------------

# Glossary Copy
glossary_src = str(data_root_path) + '/sources/' + source_glossary_filename
glossary_csv = str(data_root_path) + '/output/glossary-entries.csv'
shutil.copy(glossary_src , glossary_csv)

# Copy Sources
sources_src = str(data_root_path) + '/sources/' + source_sources_filename
target_sources_csv = str(data_root_path) + '/output/glossary-sources.csv'
shutil.copy(glossary_src , target_sources_csv)

# ---------------------------------------------------
# TRANSFORM AND SAVE

glossary_df = pd.read_csv(glossary_csv, encoding="utf8")
glossary_df.columns = map(str.lower, glossary_df.columns)
glossary_df['last_modified'] = ts
glossary_df.index.name = 'id'
glossary_df.to_csv(glossary_csv, encoding='utf-8')

sources_df = pd.read_csv(sources_src, encoding="utf8")
sources_df.columns = map(str.lower, sources_df.columns)
glossary_df['last_modified'] = ts
sources_df.to_csv(target_sources_csv, index=False, encoding='utf-8')


# COPY OUTPUTS TO APP DIRECTORY
source_glossary_csv = str(data_root_path) + '/output/glossary-entries.csv'
app_glossary_csv = str(app_data_path) + '/glossary-entries.csv'
shutil.copy(source_glossary_csv, app_glossary_csv)

target_sources_csv = str(data_root_path) + '/output/glossary-sources.csv'
app_sources_csv = str(app_data_path) + '/glossary-sources.csv'
shutil.copy(target_sources_csv, app_sources_csv)
