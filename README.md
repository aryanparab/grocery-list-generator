# Grocery List Generator

A simple tool to generate organized, shareable grocery lists from recipes, pantry inventory, and user preferences. Grocery List Generator helps you plan shopping trips more efficiently by aggregating ingredients, consolidating quantities, grouping items by store sections, and exporting lists in common formats.

Why this repository exists
- Save time: stop manually collecting ingredients from multiple recipes.
- Reduce waste: use pantry-aware generation to avoid buying what you already have.
- Improve shopping efficiency: group items by store sections so you spend less time in-store.
- Shareable output: export lists as CSV/JSON or printable formats for easy sharing and archiving.

Table of contents
- Features
- Why it's useful
- Installation
- Quickstart
  - CLI
  - Web UI / API (if included)
- Configuration
- Examples
- Development
- Contributing
- License
- Contact

Features
- Parse recipe files (Markdown, JSON, or other supported formats) to extract ingredient lists.
- Merge duplicate ingredients and normalize units (e.g., "1 cup sugar" + "200 g sugar").
- Apply pantry/inventory to remove already-owned items.
- Support for dietary filters (e.g., vegetarian, gluten-free) when generating shopping lists.
- Group items by store section (produce, dairy, meat, bakery, etc.).
- Export to CSV, JSON, and human-readable text or printable formats.
- Optional price estimation when price data is available.

Why it's useful
- Meal planning: assemble weekly shopping lists from chosen recipes.
- Budgeting: estimate shopping costs and avoid surprise purchases.
- Waste reduction: prevents buying duplicates of items already in pantry.
- Accessibility: quick export and sharing with family, roommates, or co-shoppers.

Installation
Note: adjust these commands to this repository's language (Node/Python/Rust) and package manager as appropriate.

- Clone the repository
  git clone https://github.com/aryanparab/grocery-list-generator.git
  cd grocery-list-generator

- If this is a Node.js project
  npm install
  npm run build

- If this is a Python project
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt

- Docker (optional)
  docker build -t grocery-list-generator .
  docker run -it --rm grocery-list-generator

Quickstart

CLI (example)
If the repository exposes a CLI named `grocery-list-generator`, a typical workflow might look like:

- Generate a grocery list from a folder of recipes and a pantry file:
  grocery-list-generator generate --recipes ./recipes --pantry ./pantry.json --output grocery-list.csv

- Generate and print grouped list to stdout:
  grocery-list-generator generate --recipes ./week-recipes --group-by section --format text

Web UI / API (example)
If the project includes a web interface or API, start the server and visit the UI:

- Start the server:
  npm start
  # or
  python -m grocery_list_generator.server

- Browse to:
  http://localhost:3000
  Use the UI to upload recipes, set pantry items, apply dietary filters, and export lists.

Configuration
- recipes/ : directory for recipe files (Markdown, JSON, etc.)
- pantry.json : optional pantry inventory file
- config.yaml (or .json) : project configuration (default store sections, unit preferences, currency, diet rules)

Examples
- Minimal example recipe (YAML/JSON/Markdown depending on project):
  title: "Tomato Pasta"
  ingredients:
  - "200 g pasta"
  - "2 tomatoes"
  - "1 tbsp olive oil"
  - "1 clove garlic"

- Minimal pantry.json:
  {
    "pasta": "500 g",
    "olive oil": "1 bottle"
  }

Development
- Run tests:
  npm test
  # or
  pytest

- Linting and formatting:
  npm run lint
  # or
  black . && flake8

- Code structure (example)
  - src/ or grocery_list_generator/ : core logic and modules
  - cli/ : command-line entry
  - web/ : web server and UI
  - tests/ : unit and integration tests

Contributing
Contributions are welcome! Suggested workflow:
1. Fork the repo
2. Create a feature branch: git checkout -b feat/my-feature
3. Make changes and add tests
4. Open a pull request describing your change

Please follow the project's code style and include tests for new functionality.

License
Include the repository's license here (e.g., MIT). If none, add a LICENSE file and choose a license.

Contact
Maintained by aryanparab. Open an issue or a pull request for bugs, feature requests, or questions.

---

Next steps
- I added a general README that fits a typical grocery list generator project. If you tell me the project's language (Node/Python/etc.), CLI entrypoint, or main files (e.g., `index.js`, `main.py`, `package.json`), I will update the Installation and Quickstart sections with exact commands and examples tailored to this repository.
Link : https://aryanparab-grocery-list-generator-streamlit-app-dxclse.streamlit.app/groc
Demo Video : https://drive.google.com/file/d/1gW5i3gI_a1QX9t67hLzP_tpa-QEh3NFY/view?usp=sharing

Google Oauth causing issues in production so had to bypass login in the hosted app
