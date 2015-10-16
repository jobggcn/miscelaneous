"""
ASCllock.py 
Oliver Baumbach 

Displays an ASCII Clock in the terminal. 
"""


import os, sys
import random, datetime, time
from shutil import get_terminal_size
from PIL import Image, ImageDraw, ImageFont 

import string



def generate_char_buffer(image ,character_set):
    image_width, image_height = image.size 
    char_buffer = [] 
    for row in range(image_height):
        row_buffer = [random.choice(character_set) if sum(image.getpixel((column,row))) else ' ' for column in range(image_width)]
        char_buffer.append(row_buffer) 
    return char_buffer

def print_char_buffer(char_buffer):
    for row in char_buffer:
        print(''.join(row))

def generate_time_image(width, height, ttf_path, scale):
    image = Image.new('RGB',(width, height), 'black') 
    draw = ImageDraw.Draw(image) 
    
    time_string = datetime.datetime.now().strftime('%H:%M:%S')
    
    for size in range(height):
        _font = ImageFont.truetype(ttf_path, size)
        f_width, f_height = _font.getsize(time_string) 
        if f_width >= width*scale or f_height >= height*scale:
            _font = ImageFont.truetype(ttf_path, size-1)
            break
    
    f_width, f_height = _font.getsize(time_string) 
    w_offset = round((width - f_width)/2)
    h_offset = round((height - f_height)/2)
    draw.text((w_offset, h_offset),time_string, fill = 'white', font = _font)
    return image 

def fit_image(width, height, image):
    image = image.resize((width, height), Image.ANTIALIAS)
    image = image.convert('1')
    image = image.convert('RGB') 
    return image
                

def horizontal_scanline_filter(char_buffer, probability, maximum_distortion):
    for row_index in range(len(char_buffer)):
        if random.random() < probability:
            distortion = random.randint(0,maximum_distortion)
            if random.random() < 0.5:
                char_buffer[row_index] = char_buffer[row_index][distortion:] + char_buffer[row_index][:distortion]
            else:
                char_buffer[row_index] = char_buffer[row_index][-distortion:] + char_buffer[row_index][:-distortion]
    return char_buffer

def vertical_scanline_filter(char_buffer, probability, maximum_distortion):
    for column_index in range(len(char_buffer[0])):
        if random.random() < probability:
            distortion = random.randint(0,maximum_distortion)
            if random.random() < 0.5: #Sweep up 
                for row_index in range(len(char_buffer)-distortion): 
                    char_buffer[row_index - distortion][column_index] = char_buffer[row_index][column_index]
                    char_buffer[row_index][column_index] = ' ' 
            else: #Sweep down 
                for row_index in reversed(range(len(char_buffer)-distortion)):
                    char_buffer[row_index + distortion][column_index] = char_buffer[row_index][column_index]
                    char_buffer[row_index][column_index] = ' ' 
    return char_buffer
                
def add_random_characters_filter(char_buffer, probability, character_set):
    for row_index in range(len(char_buffer)):
        for column_index in range(len(char_buffer[row_index])):
            if random.random() < probability and char_buffer[row_index][column_index] == ' ':
                char_buffer[row_index][column_index] = random.choice(character_set)
    return char_buffer

def add_own_sourcecode_filter(char_buffer, height):
    with open('ASCllock.py', 'r') as source_file: 
        source = source_file.readlines()
    
    source = [line.strip() for line in source] #Replace tabs with 4 spaces 
    l_index = 0 
    for line in random.sample(source,random.randint(0,height)):
        for c_index in range(min( (len(line),len(char_buffer[l_index])) )):
            char_buffer[l_index][c_index] = line[c_index]
        l_index += 1 
    return char_buffer
    
def vertical_wiggle_filter(char_buffer, probability, max_extent):
    if random.random() < probability:
        wiggle = random.randint(0,max_extent)
        char_buffer = char_buffer[wiggle:] + char_buffer[:wiggle] 
    return char_buffer

#Testing the generators and filters
while True:
    t_width, t_height = get_terminal_size()
    img = generate_time_image(t_width, t_height, '/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf', 0.9)
    #img = fit_image(t_width, t_height, img)
    #img = Image.open('test.jpg')
    char_buffer = generate_char_buffer(img, string.ascii_lowercase)
    char_buffer = vertical_scanline_filter(char_buffer, 0.05, 5)
    char_buffer = horizontal_scanline_filter(char_buffer, 0.05, 5)
    char_buffer = add_random_characters_filter(char_buffer, 0.01, string.ascii_lowercase)
    char_buffer = add_own_sourcecode_filter(char_buffer, round(t_height/2))
    char_buffer = vertical_wiggle_filter(char_buffer, 0.1, 5)
    print_char_buffer(char_buffer)
    time.sleep(0.1)
