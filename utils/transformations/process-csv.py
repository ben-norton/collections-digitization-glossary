from pathlib import Path
import pandas as pd
import shutil
import datetime
import globals as cfg
from globals import get_latest_glossary_file, get_latest_sources_file

source_glossary_filename = get_latest_glossary_file()
source_sources_filename = get_latest_sources_file()

today = datetime.date.today()
ts = today.strftime("%Y%m%d")

# PATHS
root_dir = cfg.get_project_root()
data_root_path = str(root_dir) + '/data'
app_data_path = str(root_dir) + '/app/data'


def process_csv_files():
	# Glossary Copy
	glossary_src = get_latest_glossary_file()
	glossary_csv = str(data_root_path) + '/output/glossary-terms.csv'
	shutil.copy(glossary_src , glossary_csv)

	# Copy Sources
	sources_src = get_latest_sources_file()
	target_sources_csv = str(data_root_path) + '/output/glossary-sources.csv'
	shutil.copy(glossary_src , target_sources_csv)

	# ---------------------------------------------------
	# TRANSFORM AND SAVE

	glossary_df = pd.read_csv(glossary_csv, encoding="utf8")
	glossary_df.columns = map(str.lower, glossary_df.columns)
	glossary_df['last_modified'] = ts
	glossary_df.rename(columns={'term': 'label'}, inplace=True)
	glossary_df.index.name = 'id'
	glossary_df.to_csv(glossary_csv, encoding='utf-8')

	sources_df = pd.read_csv(sources_src, encoding="utf8")
	sources_df.columns = map(str.lower, sources_df.columns)
	glossary_df['last_modified'] = ts
	sources_df.to_csv(target_sources_csv, index=False, encoding='utf-8')


	# COPY OUTPUTS TO APP DIRECTORY
	source_glossary_csv = str(data_root_path) + '/output/glossary-terms.csv'
	app_glossary_csv = str(app_data_path) + '/glossary-terms.csv'
	shutil.copy(source_glossary_csv, app_glossary_csv)

	target_sources_csv = str(data_root_path) + '/output/glossary-sources.csv'
	app_sources_csv = str(app_data_path) + '/glossary-sources.csv'
	shutil.copy(target_sources_csv, app_sources_csv)

