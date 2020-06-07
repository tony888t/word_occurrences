# Instructions
1. Install python 3.8.x
2. pip install pipenv 
`pip install pipenv`
3. Create environment using pipenv
`pipenv install`
4. Activate environment
`pipenv shell`
5. Run project locally
`python manage.py runserver 0:8000`
This will warn you about unapplied migrations but for this example it's not needed.
6. Navigate to `localhost:8000/`
7. Click on links to display the day on the page and console.


## Running tests
`pytest`

## Lint
`flake8`

## Future changes
- Ability to look for specific words find where it is used and what file.
- Filter table by keyword.

## Learnings
- Researched ways to extract keywords from text.
- Went through multiple ideas from saving into database to using multiple libraries (nlkt, rake-nlkt).
- Ended using gensim due to simplicity.
- Looked at summarising doc and then extract keywords but this changes the keywords so this was not an option.
- When extracting keywords it add suffixes to workd for example `let` and `letting`, even though `letting` is not present in the document. Need to find a way to avoid this with gensim.
- Still need to learn more about word scoring with `gensim`.
