import os
import pathlib
import random
import re

import praw
from dotenv import load_dotenv
from jinja2 import Environment
from jinja2 import FileSystemLoader
from praw.models import Submission
from praw.models import Redditor

load_dotenv()

IMAGE_ONLY_REGEX = re.compile(r"(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|png)")


def main() -> int:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="reddit-saved-pptx",
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
    )

    me: Redditor = reddit.user.me()

    nsfw_posts: list[Submission] = []
    for post in me.saved(limit=None):
        if not isinstance(post, Submission):
            continue

        post: Submission
        if IMAGE_ONLY_REGEX.match(post.url):
            nsfw_posts.append(post)

    random.shuffle(nsfw_posts)

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("base.jinja2")
    result = template.render(nsfw_posts=nsfw_posts)
    pathlib.Path("slide-deck.md").write_text(result, encoding="utf8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
