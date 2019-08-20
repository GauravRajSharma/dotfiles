source "$HOME/.config/fish/alias.fish"
source "$HOME/.config/fish/shortcuts.fish"
source	"$HOME/.config/fish/settings.fish"
set -g simple_ass_prompt_greeting

command -v vg >/dev/null 2>&1; and vg eval --shell fish | source
