# Notes on Machine Learning and Artificial Intelligence

## Writing Content Procedure
- Write in Jupyter or markdown using standard format
- Add to correct folder
- Run make_site.ipynb
- View Page

## Deployment Procedure

- pelican content -o output -s pelicanconf.py
- ghp-import output
- git push origin gh-pages

## Development Procedure

- cd output
- python -m pelican.server
- pelican
- go to localhost:8000
