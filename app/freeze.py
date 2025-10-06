
from flask import Flask, render_template, request
from flask_frozen import Freezer
from markupsafe import Markup
import markdown2
import pandas as pd
import yaml
import os
import sys

build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
app = Flask(__name__, template_folder='templates')
freezer = Freezer(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_RELATIVE_URLS_PRETTY'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

# Source Files
glossary_csv = 'data/glossary-entries.csv'
df = pd.read_csv(glossary_csv, encoding='utf-8')

sources_csv = 'data/glossary-sources.csv'
df_sources = pd.read_csv(sources_csv, encoding='utf-8')

# CONFIG
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


with open('meta.yml') as metadata:
    meta = yaml.safe_load(metadata)


@app.route('/')
def index():
    # Get filter parameters
    search = request.args.get('search', '').strip()
    category = request.args.get('category', '').strip()
    prov_class = request.args.get('prov_class', '').strip()
    sort_by = request.args.get('sort_by', 'term')

    # Start with full glossary
    filtered_df = df.copy()

    # Apply search filter
    if search:
        filtered_df = filtered_df[
            filtered_df['term'].str.contains(search, case=False) |
            filtered_df['definition'].str.contains(search, case=False)
            ]

    # Apply category filter
    if category:
        filtered_df = filtered_df[filtered_df['category'] == category]

    # Apply tag filter
    if prov_class:
        filtered_df = filtered_df[filtered_df['prov_class'] == prov_class]

    # Sort results
    if sort_by in filtered_df.columns:
        filtered_df = filtered_df.sort_values(by=sort_by)

    # Convert to list of dictionaries
    terms = filtered_df.to_dict(orient='records')

    # Get all unique categories and tags for filters
    all_categories = sorted(df['category'].unique().tolist())
    all_prov_classes = sorted(df['prov_class'].unique().tolist())
#    all_tags = sorted(set([tag.strip() for tags in df['tags'] for tag in tags.split(',')]))

    return render_template('glossary.html',
                           terms=terms,
                           all_categories=all_categories,
                           all_prov_classes=all_prov_classes,
                           current_search=search,
                           current_category=category,
                           current_prov_class=prov_class,
                           current_sort=sort_by,
                           total_count=len(terms),
                            active_page='glossary')

@app.route('/term/<int:term_id>/')
def term_detail(term_id):
    term = df[df['id'] == term_id].to_dict(orient='records')
    if term:
        return render_template('term_detail.html', term=term[0])
    return "Term not found", 404

@app.route('/sources/')
def sources():
    sources = df_sources.to_dict(orient='records')

    return render_template('sources.html',
                           sources=sources,
                            active_page = 'sources',
                           )

@app.route('/about/')
def about():
    about_mdfile = 'md/about-content.md'
    with open(about_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    return render_template('about.html',
                           about_markdown=Markup(marked_text),
                           active_page='about',
                           slug='about')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        print("Written to: " + build_dir)
    elif len(sys.argv) > 1 and sys.argv[1] == "test":
        freezer.run(debug=True)
        print("Test run")
    else:
        app.run(port=5000)