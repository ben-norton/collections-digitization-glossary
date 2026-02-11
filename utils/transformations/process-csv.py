from pathlib import Path
import pandas as pd
import shutil
import datetime
import globals as cfg
from globals import get_latest_glossary_file, get_latest_sources_file
import csv

source_glossary_filename = get_latest_glossary_file()
source_sources_filename = get_latest_sources_file()

today = datetime.date.today()
ts = today.strftime("%Y%m%d")

# PATHS
root_dir = cfg.get_project_root()
data_root_path = str(root_dir) + '/data'
app_data_path = str(root_dir) + '/app/static/data'


def process_csv_files():
	# Glossary Copy
	glossary_src = get_latest_glossary_file()
	glossary_csv = str(data_root_path) + '/output/glossary-terms.csv'
	shutil.copy(glossary_src, glossary_csv)

	# Copy Sources
	sources_src = get_latest_sources_file()
	target_sources_csv = str(data_root_path) + '/output/glossary-sources.csv'
	shutil.copy(glossary_src, target_sources_csv)

	# ---------------------------------------------------
	# TRANSFORM AND SAVE

	glossary_df = pd.read_csv(glossary_csv, sep='\t', encoding="utf8")
	glossary_df.columns = map(str.lower, glossary_df.columns)
	# Add timestamp column
	glossary_df['last_modified'] = ts
	# Rename term column
	glossary_df.rename(columns={'term': 'label'}, inplace=True)
	glossary_df.index.name = 'id'
	# Drop empty rows
	glossary_df = glossary_df.dropna(how='all')
	glossary_df.to_csv(glossary_csv, encoding='utf-8')

	sources_df = pd.read_csv(sources_src, encoding="utf8")
	sources_df.columns = map(str.lower, sources_df.columns)
	glossary_df['last_modified'] = ts
	sources_df.to_csv(target_sources_csv, index=False, encoding='utf-8')

	# COPY OUTPUTS TO APP DIRECTORY
	source_glossary_csv = str(data_root_path) + '/output/glossary-terms.csv'
	app_glossary_csv = str(app_data_path) + '/glossary-terms.csv'
	shutil.copy(source_glossary_csv, app_glossary_csv)
	# GENERATE TEXT FILE FOR DOWNLOAD
	terms_target_txt = str(app_data_path) + '/collections-digitization-glossary.txt'
	csv_to_txt_basic(app_glossary_csv, terms_target_txt, delimiter=' ')

	target_sources_csv = str(data_root_path) + '/output/glossary-sources.csv'
	app_sources_csv = str(app_data_path) + '/glossary-sources.csv'
	shutil.copy(target_sources_csv, app_sources_csv)


def csv_to_txt_basic(csv_filepath, txt_filepath, delimiter=' '):
	"""
    Converts a CSV file to a plain text file.
    Args:
        csv_filepath (str): The path to the input CSV file.
        txt_filepath (str): The path to the output TXT file.
        delimiter (str): The string to use to join columns in the TXT file.
        Adds blank row between terms in text file
    """
	with open(csv_filepath, 'r', newline='', encoding='utf-8') as infile:
		csv_reader = csv.reader(infile)
		with open(txt_filepath, 'w', encoding='utf-8') as text_output:
			for row in csv_reader:
				# Skip the first column (index 0) and write the rest
				for column in row[1:]:
					text_output.write(column + '\n')
				text_output.write('\n')

		print(f"CSV file '{csv_filepath}' successfully converted to TXT file '{txt_filepath}'.")


process_csv_files()
