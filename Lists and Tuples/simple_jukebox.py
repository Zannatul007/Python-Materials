from nested_data_structure import albums

while True:
    for index,(album,name,year,songs) in enumerate(albums):
        print("{}:{}".format(index+1,album))
    choice = int(input("Make a valid choice\n"))
    if(1<=choice<=len(albums)):
        # print(albums[choice-1])
        song_list = albums[choice-1][3]
        # print(song_list)
    else:
        break
    for index,(track,track_name) in enumerate(song_list):
        print("{}:{}".format(index+1,track_name))
    song_choice = int(input("Please Select The Song Track"))
    if(1<=song_choice<=len(song_list)):
        title = song_list[song_choice-1][1]
        print(title)
    else:
        for index,(album,name,year,songs) in enumerate(albums):
            print("{}:{}".format(index+1,album))



