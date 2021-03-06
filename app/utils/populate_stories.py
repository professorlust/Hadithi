from app import db
from app.models import Story, AuthorAccount
import json

stories = open("stories.json", "r")
authors = open("authors.json", "r")

with stories as story_data:
    loaded_stories = json.load(story_data)

with authors as author_data:
    loaded_authors = json.load(author_data)

author_story = list(zip(loaded_authors, loaded_stories))

for au_st in author_story:
    author = AuthorAccount(full_name=au_st[0]["full_name"], email=au_st[0]["email"], password=au_st[0]["password"])
    story = Story(title=au_st[1]["title"], tagline=au_st[1]["tagline"],
                  category=au_st[1]["category"], content=au_st[1]["content"], author_id=author.id)
    db.session.add(author)
    db.session.add(story)
db.session.commit()
