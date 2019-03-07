all: emoji.compose modletters.compose apl_keyboard.compose

emoji.compose: emoji-base emojitrans2.pl
	./emojitrans2.pl < $< > $@

modletters.compose: modletters-base emojitrans2.pl
	./emojitrans2.pl < $< > $@

apl_keyboard.compose: apl_keyboard.txt convert.py
	./convert.py < $< > $2
