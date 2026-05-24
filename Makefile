.PHONY: draw

draw:
	uvx --from keymap-drawer keymap -c keymap-drawer/config.yaml parse -z config/corne.keymap \
	  | keymap-drawer/strip-outer-cols.py \
	  | uvx --from keymap-drawer keymap -c keymap-drawer/config.yaml draw - \
	  > keymap-drawer/corne.svg
	nix shell nixpkgs#librsvg -c rsvg-convert -o keymap-drawer/corne.png keymap-drawer/corne.svg
