import pandas as pd
from operator import itemgetter

df_amazon = pd.read_csv("/app/datasets/amazon_prime_titles.csv",delimiter = ',',encoding = "utf-8")
df_disney = pd.read_csv("/app/datasets/disney_plus_titles.csv",delimiter = ',',encoding = "utf-8")
df_hulu = pd.read_csv("/app/datasets/hulu_titles.csv",delimiter = ',',encoding = "utf-8")
df_netflix = pd.read_json("/app/datasets/netflix_titles.json",orient="records")

df_amazon = df_amazon.drop(columns=["show_id","director","country","date_added","rating","description"])
df_disney = df_disney.drop(columns=["show_id","director","country","date_added","rating","description"])
df_hulu = df_hulu.drop(columns=["show_id","director","country","date_added","rating","description"])
df_netflix = df_netflix.drop(columns=["show_id","director","country","date_added","rating","description"])

df_amazon = df_amazon.fillna("Sin Datos")
df_disney = df_disney.fillna("Sin Datos")
df_hulu = df_hulu.fillna("Sin Datos")
df_netflix = df_netflix.fillna("Sin Datos")

df_amazon.cast = df_amazon.cast.replace("1","Sin Datos")
df_amazon.cast = df_amazon.cast.replace("1, 2, 3","Sin Datos")

df_amazon = df_amazon.assign(platform="amazon")
df_disney = df_disney.assign(platform="disney")
df_hulu = df_hulu.assign(platform="hulu")
df_netflix = df_netflix.assign(platform="netflix")

df_final = pd.concat([df_amazon,df_disney,df_hulu,df_netflix], ignore_index=True)

def sep_duration(df):

    df = df.join(df.duration.str.split(expand=True))

    df.rename(columns={0:'duration_int',
                                1:'duration_type'}, inplace=True)
    return df

df_final = sep_duration(df_final)

df_final.duration_int = df_final.duration_int.replace('Sin',0)
df_final.duration_type = df_final.duration_type.replace('Dato','Sin Dato')

df_final.duration_int = df_final.duration_int.astype('int64')
df_final.duration_type = df_final.duration_type.replace('Season','season')
df_final.duration_type = df_final.duration_type.replace('Seasons','season')