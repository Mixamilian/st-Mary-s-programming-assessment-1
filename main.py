import pandas as pd
import matplotlib.pyplot as plt


#boolean variable to continue the while loops should the user wish to continue using the dataframe
run = True
while run ==True:
    # basic text based user interface allowing the user to pick between what they would like to do with the data
    df = pd.read_csv('youtube_trending_videos.csv')
    Choice= input("""
    would you like to
    a) load the data
    b) process the data
    c) visualise the data
    """)

    #output for option 'a' of the interface which loads and outputs the dataframe into the terminal
    if Choice.lower() == 'a':
        print(df)
        con = input("Do you wish to continue? (y/n)")
        if con.lower() == 'n':
            run = False

    #output for option 'b' giving the user more options on how they want to process the data based on the assessment specifications
    if Choice.lower() == 'b':
        retrive = input("""
        how would you like this data to be processed
        a)Retrieve the total number of videos and channels in the dataset.
        b)List all unique video categories.
        c)Retrieve detailed information for a specific video using its video_id.
        d)Identify the top 10 trending videos based on key engagement metrics such as views, likes, and comment count.
        """)

    #output for option 'a' of the processing specification
        if retrive.lower() == 'a':
            print(f"the total number of Video id's is: {df['video_id'].count()}")
            print(f"the total number of channel's is: {df['channel_title'].count()}")
            con = input("Do you wish to continue? (y/n)")
            if con.lower() == 'n':
                run = False

        # output for option 'b' of the processing specification
        if retrive.lower() == 'b':
            print(f"there are {df['category_id'].nunique()} unique video categories")
            print(df['category_id'].value_counts())
            con = input("Do you wish to continue? (y/n)")
            if con.lower() == 'n':
                run = False

        # output for option 'c' of the processing specification
        if retrive.lower() == 'c':
            v_ID = input("Enter the video ID: ")
            print(df.groupby('video_id').get_group(v_ID))
            con = input("Do you wish to continue? (y/n)")
            if con.lower() == 'n':
                run = False

        # output for option 'd' of the processing specification
        if retrive.lower() == 'd':
            print(f"the top trending videos based on views are: {df.nlargest(10,['views'])}")
            print(f"the top trending videos based on likes are: {df.nlargest(10, ['likes'])}")
            print(f"the top trending videos based on the number of comments are: {df.nlargest(10, ['comment_count'])}")
            con = input("Do you wish to continue? (y/n)")
            if con.lower() == 'n':
                run = False

    #output for option 'c' the visualisation of the dataframe
    if Choice.lower() == 'c':
        print("""
        generating pie chart basted of number of videos per category id's
        .
        ..
        ...
        """)
        labels = ['24','23','22','25','10','17','26','1','28','20','27','19','2','29','15','43']
        sizes = ['133','71','60','46','44','31','24','20','20','15','10','8','7','5','3','2']
        plt.pie(sizes, labels=labels)
        plt.show()
        con = input("Do you wish to continue? (y/n)")
        if con.lower() == 'n':
            run = False



