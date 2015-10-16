ASCllock.py

ASCllock is a relatively simple clock that runs in the linux terminal. 
It's written in Python3, because that's what I'm learning right now. 
It supports terminal resizing, unicode (any that your terminal can display), and a couple of fun effects. 

It's probably not very efficiently written though, and at large sizes, the update time goes down visibly. 

It requires the Pillow library, which in turn requires a number of other libraries. 
On how to install Pillow, consult this:
http://pillow.readthedocs.org/en/latest/installation.html


There's a couple of functions in the script that can be used to assemble your own version of this hacked together clock

- generate_char_buffer(image ,character_set):
This function takes a PIL RGB Image, and maps pixels to either whitespace or a random character from character_set. 

- print_char_buffer(char_buffer):
This function prints the char_buffer to the terminal

- generate_time_image(width, height, ttf_path, scale):
This function generates a PIL Image of given size displaying the current time in the format HH:MM:SS
ttf_path has to be the path to a .ttf font file 
scale is how big the displayed time should be

- fit_image(width, height, image):
This function takes a PIL image, resizes it and turns it into B&W

- horizontal_scanline_filter(char_buffer, probability, maximum_distortion):
This function takes a char_buffer and returns a char_buffer with horizontal distortion added. 
probability gives the likelyhood that a given line is distorted (0-1)
maximum_distortion is the upper bound of characters a given line can shift

-  vertical_scanline_filter(char_buffer, probability, maximum_distortion):
Does the same as horizontal_scanline_filter, but shifts lines up or down

- add_random_characters_filter(char_buffer, probability, character_set):
This function takes a char_buffer and returns a char_buffer with random characters added to it. 
probability gives the likelyhood that a certain character will be filled 
character_set is a list of characters the function randomly chooses from 

-  add_own_sourcecode_filter(char_buffer, height):
This function adds the sourcecode of the program to the character buffer, to distract python programmers. 
It picks a random selection of lines, with the maximum number of lines given by the height parameter. 

- vertical_wiggle_filter(char_buffer, probability, max_extent):
This function rotates the char_buffer by a random amount, capped at max_extent, the likelyhood given by probability. 

It looks pretty neat.

