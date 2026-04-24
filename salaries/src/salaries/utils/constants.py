from pathlib import Path

BASE_PATH = Path(__file__).parents[1]
ASSETS_PATH = BASE_PATH / "assets"
COMPONENTS_PATH = BASE_PATH / "components"
IMAGE_PATH = ASSETS_PATH / "image"
STYLES_PATH = ASSETS_PATH / "styles"
MARKDOWN_PATH = ASSETS_PATH / "markdown"
DATA_PATH = ASSETS_PATH / "data"

print(ASSETS_PATH)
print(COMPONENTS_PATH)
print(IMAGE_PATH)
print(STYLES_PATH) 
print(MARKDOWN_PATH)
print(DATA_PATH)