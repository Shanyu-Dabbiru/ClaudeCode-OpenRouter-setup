# OpenRouter Configuration for Claude Code

This script configures `~/.claude/settings.json` to route Claude Code requests through [OpenRouter](https://openrouter.ai/).

## Prerequisites

*   Python 3
*   An [OpenRouter API key](https://openrouter.ai/keys)

## Usage

1.  **Run the script:**

    ```bash
    python setup.py
    ```

2.  **Enter your API key:** When prompted, paste your OpenRouter API key and press Enter.

3.  **Restart your terminal:** For the changes to take effect, you must completely close and reopen your terminal window.

## Important Notes

*   The script creates a backup of your existing `settings.json` file as `settings.json.bak`.
*   You need to have run Claude Code at least once before running this script to ensure `settings.json` exists.
*   This script specifically sets the model to `google/gemini-2.5-pro-preview`.
