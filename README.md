# reddit-saved-pptx
Convert your Reddit saved posts into a powerpoint presentation. Code can be easily adjusted to your needs.

## Requirements
- python
- npm (npx)
- [A Reddit application](https://www.reddit.com/prefs/apps)

## Usage
```bash
# One-time setup of the necessary environment variables
cp .env.sample .env

# Build the powerpoint. Result will be in the same directory called `output.pptx`.
make slides
```