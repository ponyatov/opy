.PHONY: install packages
install: packages
packages:
	sudo apt purge cython
	sudo pip install kivy cython