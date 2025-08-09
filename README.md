# PySide6 Test structure (uv + CI + Tests + Releases)

A production-ready starter for **PySide6** apps with:
- Clean, extensible structure
- Responsive layout (splitter + adaptive spacing + QSS)
- Tests (pytest-qt)
- CI (GitHub Actions via `uv`) for lint, type, tests
- Release builds for **Windows / macOS / Linux** using **PyInstaller**
- Icons included, fonts fetched via `scripts/fetch_fonts.py` (avoids bundling license assets in repo)

## Quickstart (Dev)
```bash
# Install uv once if you haven't
# curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync --all-extras --dev
uv run python -m app.main
```

## Tests
```bash
uv run pytest
```

## Fonts
We don't bundle fonts directly in this repo to keep the example small and avoid distribution issues.
Run the helper:
```bash
uv run python scripts/fetch_fonts.py
```
It will download **Inter** and **Noto Sans** (SIL OFL) into `src/app/assets/fonts/`.

## Release Build (Local)
```bash
uv run pyinstaller app.spec
# Artifacts in dist/
```

## GitHub Actions
- `.github/workflows/ci.yml` → lint, type-check, tests (headless Qt via xvfb)
- `.github/workflows/release.yml` → build PyInstaller executables for Win/macOS/Linux and attach to a GitHub Release (trigger: tag push v*)


## .env
```
APP_TITLE=PySide UI
THEME_FILE=src/app/assets/styles/app.qss
```