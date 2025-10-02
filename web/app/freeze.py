
from flask import Flask, render_template
from flask_frozen import Freezer
from markupsafe import Markup
import sys
import markdown2
import pandas as pd
import yaml
from pathlib import Path
import globals as cfg

root_dir = cfg.get_project_root()

current_dir = Path.cwd()
build_dir = str(root_dir) + '/web/app/build'
app = Flask(__name__, template_folder='templates')
freezer = Freezer(app)


#app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_RELATIVE_URLS_PRETTY'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

with open('meta.yml') as metadata:
    meta = yaml.safe_load(metadata)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',
                           pageTitle='404 Error'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html',
                           pageTitle='500 Unknown Error'), 500

# Homepage with content stored in markdown file
@app.route('/')
def home():
    home_mdfile = 'md/home-content.md'
    with open(home_mdfile, encoding="utf-8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])
    return render_template('home.html',
                           home_markdown=Markup(marked_text),
                           pageTitle='Home',
                           title=meta['title'],
                           githubRepo=meta['github-repo'],
                           slug='home'
                           )
@app.route('/glossary/')
def glossary():
    glossary_header_mdfile = 'md/glossary_header.md'
    with open(glossary_header_mdfile, encoding="utf-8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    # Read Transformed Glossary CSV
    glossary_csv = str(root_dir) + 'sources/output/glossary.tsv'   
    glossary_df = pd.read_csv(glossary_csv, sep='\t', lineterminator='\n', encoding='utf-8')
    glossary_df = glossary_df.sort_values(by=['Term'])

    return render_template('glossary.html',
                           datasets_markdown=Markup(marked_text),
                           glossary=glossary_df,
                           pageTitle='Glossary',
                           title=meta['title'],
                           githubRepo=meta['github-repo'],
                           slug='glossary'
                           )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        print("Written to: " + build_dir)
    elif len(sys.argv) > 1 and sys.argv[1] == "test":
        freezer.run(debug=True)
        print("Test run")
    else:
        app.run(port=8000)