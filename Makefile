slides:
	python -m reddit_saved_pptx
	npx @marp-team/marp-cli@latest slide-deck.md -o output.pptx

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

install:
	poetry install

lint/black:
	black reddit_saved_pptx
