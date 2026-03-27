import os
import json

claude_dir = os.path.expanduser('~/.claude')
settings_file = os.path.join(claude_dir, 'settings.json')

os.makedirs(claude_dir, exist_ok=True)

data = {}
if os.path.exists(settings_file):
    try:
        with open(settings_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        pass

if 'env' not in data:
    data['env'] = {}

print("Let's configure Claude Code for OpenRouter!")
api_key = input("Please paste your OpenRouter API Key (should start with sk-or-): ").strip()

data['env']['ANTHROPIC_BASE_URL'] = 'https://openrouter.ai/api'
data['env']['ANTHROPIC_AUTH_TOKEN'] = api_key
# The Anthropic API key MUST remain empty to stop Claude Code from trying to use Anthropic
data['env']['ANTHROPIC_API_KEY'] = ''
data['env']['ANTHROPIC_MODEL'] = 'google/gemini-2.5-pro-preview'

data['model'] = 'sonnet[1m]'

with open(settings_file, 'w') as f:
    json.dump(data, f, indent=2)

print("\n✓ Setup is complete! ~/.claude/settings.json has been generated.")
print("─────────────────────────────────────────────────────────────")
print("FINAL INSTRUCTIONS:")
print("1. Please completely QUIT your current terminal window (don't just open a new tab).")
print("2. Open a brand NEW terminal window.")
print("3. Run `claude` in the new terminal.")
print("4. You should see `google/gemini-2.5-pro-preview` in the startup text, confirming the setup!")
