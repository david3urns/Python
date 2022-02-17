#!/usr/bin/python3

#import os to be able to get terminal width
import os

#create the function for the banner:
def cent_banner(banner_title):

    #define variables declaring the ascii art used for the borders
    horz_border = "═"
    vert_border = "║"
    top_left_corner = "╔"
    top_right_corner = "╗"
    bot_left_corner = "╚"
    bot_right_corner = "╝"

    #get the terminal width for the centering function:
    size = os.get_terminal_size()
    columns = size.columns
    title_len = len(banner_title)

    #determine if the terminal width is an even or odd number:
    if (columns % 2) == 0:
        columns = columns
    else:
        columns = columns + 1

    #determine if the banner_title is an odd or even number:
    if (title_len % 2) == 0:
        banner_title = banner_title
    else:
        banner_title = banner_title + " "

    #creates box 1/4 the width of the screen
    banner_width = columns // 4
    #print("Banner width will be " + str(banner_width))
    if (banner_width % 2) == 0:
        banner_width = banner_width
    else:
        banner_width = banner_width + 1

    #do math to center the banner_title text based on the terminal width
    banner_mid_space = banner_width - title_len
    banner_mid_space_half = banner_mid_space // 2
    banner_mid_spaces = banner_mid_space_half * " "

    #creates the actual box based on the terminal width
    banner_top = top_left_corner + horz_border * banner_width + top_right_corner
    banner_mid = vert_border + banner_mid_spaces +  banner_title + banner_mid_spaces + vert_border
    banner_bot = bot_left_corner + horz_border * banner_width + bot_right_corner

    #centers the banner in the terminal window
    cent_banner_top = banner_top.center(columns)
    cent_banner_mid = banner_mid.center(columns)
    cent_banner_bot = banner_bot.center(columns)

    print()
    print(cent_banner_top)
    print(cent_banner_mid)
    print(cent_banner_bot)
    print()

cent_banner("Test")
