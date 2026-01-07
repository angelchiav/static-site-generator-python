# Static Site Generator

A Python-based static site generator that converts Markdown files into HTML pages. It recursively processes a content directory, converts Markdown to HTML, and generates a complete static website ready to deploy.

## What it does

This tool takes a directory of Markdown files and generates a static website. It processes all `.md` files recursively, extracts titles, converts Markdown syntax to HTML, and wraps everything in a template. Static assets like CSS and images are copied to the output directory.

The generator supports standard Markdown features including headings, paragraphs, bold and italic text, code blocks, blockquotes, lists, links, and images. It handles nested directory structures and automatically creates the appropriate HTML file structure.

## Requirements

- Python 3.13 or higher
- No external dependencies (uses only Python standard library)

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/static-site-generator-python.git
cd static-site-generator-python
```

That's it. No package installation needed since it only uses Python's standard library.

## Usage

### Basic usage

Run the generator with the default base path:

```bash
python3 src/main.py
```

This will:
- Read Markdown files from the `content/` directory
- Generate HTML files in the `docs/` directory
- Copy static assets from `static/` to `docs/`
- Use `template.html` as the page template

### Custom base path

If you're deploying to a subdirectory (like GitHub Pages), specify the base path:

```bash
python3 src/main.py "/your-base-path/"
```

The base path is used to fix relative URLs in links and images. Make sure it starts and ends with a slash.

### Preview locally

After generating, you can preview the site using Python's built-in HTTP server:

```bash
cd docs
python3 -m http.server 8888
```

Then open `http://localhost:8888` in your browser.

Or use the provided script:

```bash
./main.sh
```

## Project structure

```
.
├── content/          # Markdown source files
│   ├── index.md      # Homepage
│   ├── blog/         # Blog posts (example)
│   └── contact/      # Other pages
├── static/           # Static assets (CSS, images)
│   ├── index.css
│   └── images/
├── template.html     # HTML template for pages
├── docs/             # Generated HTML output (created by generator)
└── src/              # Source code
    ├── main.py       # Entry point
    └── ...           # Other modules
```

## How it works

The generator processes files in several steps:

1. **Copy static assets**: Files from `static/` are copied to the output directory
2. **Recursive processing**: Walks through the `content/` directory
3. **Markdown conversion**: Each `.md` file is converted to HTML
4. **Template application**: The HTML content is inserted into `template.html`
5. **Title extraction**: The first heading in each Markdown file becomes the page title
6. **URL fixing**: Links and image sources are adjusted based on the base path

Markdown files named `index.md` become `index.html` in the same directory. Other Markdown files (like `about.md`) become `about/index.html`.

## Supported Markdown features

- Headings (h1 through h6)
- Paragraphs
- **Bold text** (double asterisks)
- *Italic text* (single underscore)
- `Inline code` (backticks)
- Code blocks (triple backticks)
- Blockquotes (greater than sign)
- Unordered lists (dash prefix)
- Ordered lists (numbered)
- Links: `[text](url)`
- Images: `![alt text](image-url)`

## Template

The `template.html` file uses placeholders that get replaced:
- `{{ Title }}` - Page title extracted from the first heading
- `{{ Content }}` - Converted HTML content from Markdown

You can customize the template to match your site's design. Just make sure to keep those placeholders.

## Example

Given a Markdown file like this:

```markdown
# My Blog Post

This is a **bold** statement and here's some *italic* text.

- First item
- Second item

[Link to home](/)
```

The generator will create an HTML page with the content converted and wrapped in your template.

## Development

The codebase is organized into modules that handle different aspects:
- `markdown_to_blocks.py` - Splits Markdown into blocks
- `block_to_block_type.py` - Identifies block types
- `markdown_to_html_node.py` - Converts blocks to HTML nodes
- `text_to_textnodes.py` - Parses inline formatting
- `generate_page.py` - Generates a single page
- `generate_page_recursive.py` - Recursively processes directories

There are test files for most modules if you want to understand the implementation better.

## License

This project is open source. Feel free to use it however you like.
