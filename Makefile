default: config scripts
all: config scripts

config: .config
	stow -R -v config

scripts: .scripts
	stow -R -v scripts

home: .home
	stow -R -v home

.config:
	echo "--target=$(HOME)/.config" > .stowrc

.scripts:
	echo "--target=$(HOME)/.scripts" > .stowrc

.home:
	echo "--target=$(HOME)" > .stowrc

clean:
	rm .stowrc
