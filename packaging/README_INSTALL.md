# Danho Detailpage Maker Codex Plugin

Version: 0.1.0

## Manual Install

1. Extract this zip.
2. Move the plugin folder to:

```text
~/plugins/danho-detailpage-maker-codex
```

On Windows this is usually:

```text
C:\Users\<user>\plugins\danho-detailpage-maker-codex
```

If you are installing from this repository checkout, the plugin folder is:

```text
plugins/danho-detailpage-maker-codex
```

3. Ensure `~/.agents/plugins/marketplace.json` exists and contains this entry:

```json
{
  "name": "danho-detailpage-maker-codex",
  "source": {
    "source": "local",
    "path": "./plugins/danho-detailpage-maker-codex"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

4. In Codex, install `danho-detailpage-maker-codex` from the `personal` marketplace.
5. Start a new Codex thread so the plugin skills are loaded.

## Notes

- This package intentionally does not include install scripts.
- Keep the plugin folder name as `danho-detailpage-maker-codex`.
- If you update the plugin files, reinstall or refresh the plugin in Codex before opening a new thread.
