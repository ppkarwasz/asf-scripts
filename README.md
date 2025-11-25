# asf-scripts

Scripts for ASF projects

## Development Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Prerequisites

Install `uv` following the [official instructions](https://docs.astral.sh/uv/getting-started/installation/).

### Getting Started

1. Clone the repository and navigate to the project directory.

2. Sync dependencies:

   ```bash
   uv sync
   ```

3. Run tests:

   ```bash
   uv run pytest
   ```

4. Run linting and formatting checks:

   ```bash
   uv run ruff check .
   uv run ruff format --check .
   ```

5. Auto-fix linting issues and format code:

   ```bash
   uv run ruff check --fix .
   uv run ruff format .
   ```
