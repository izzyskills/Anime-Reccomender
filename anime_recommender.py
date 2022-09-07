import pandas as pd

df = pd.read_csv('anime.csv')
def anime_recommender(df,genre,no_anime,rating=7.0,):
    df_choice = df.loc[ df['Genres'].str.contains(genre),['Name','Score','Rating',"Ranked",'Genres']]
    #drops rows with the score of unknown
    df_choice = df_choice[~df_choice["Score"].eq("Unknown")]
    df_choice["Score"] = df_choice['Score'].astype(float)
    df_choice = df_choice.loc[df_choice['Score']>rating,['Name','Rating','Score','Genres']]
    if df_choice.empty==True:
        choice=df_choice
    else:
        choice= df_choice.sample(n=no_anime)
    return choice
active = True
while active:
    print('this is a program that recommends anime based on the genre of your choice\n')
    print('what are you in the mood for \n 1)Action\n2)Mystery/Thriller\n3)Romance\n4)Sports\n5)Shounen\n6)Seinen')
    gen = input('input the Genre  you want or pick among the listed  ')
    gen_dict = ['Action','Mystery|Thriller',"Romance",'Sports',"Shounen","Seinen"]
    rating = float(input("whats the minimum rating for the anime you want to watch "))
    no_anime = int(input('the number of recomendations you want '))
    #converts to integer if possible or uses the value like that
    try:
        gen =int(gen)
    except ValueError:
        gen = gen
    if isinstance(gen, int):
        arr = gen_dict[gen-1]
        print(arr)

    else:
        arr = gen.title()
    choice = anime_recommender(df,arr,no_anime,rating)
    count = 1
    if choice.empty !=True:
        for index,row in choice.iterrows():
            print(f'the no {count} anime is\n')
            print(f"The name of the anime is \" {row['Name']} \" \nthe User rating is {row['Score']} \nthe genres are {row['Genres']} \nthe pg rating is {row['Rating']}\n")
            count+=1
    else:
        print("there is no anime in the genre and/or rating you picked")
    ans = input('do you want to end program enter Yes ')
    if ans.title()== 'Yes':
        active=False



