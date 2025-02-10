def banner_text(text,screen_width):

    if(len(text) > screen_width-4 ):
        raise ValueError("String {} is larger than the screen width {}".format(text,screen_width))
    if(text == "*"):
        print(text*screen_width)
    else:
        centered_text = text.center(screen_width-4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)

banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)


        