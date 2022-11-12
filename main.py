import pandas as pd



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("PudovTestTask.csv", sep=';') #берём исходный файл в csv формате
    df['SubC'] = df['Total'] - (df['SubA'] + df['SubB']) #добавляем столбец с SubC
    #Далее вычисляем среднее для каждой клетки(добавляем столбец в наш df)
    df['meanSubA'] = df['SubA'].mean()
    df['meanSubB'] = df['SubB'].mean()
    df['meanSubC'] = df['SubC'].mean()
    #Вычисляем ковариацию для каждой клетки по формуле(в процентах)
    df['covarSubA'] = (df['SubA'].std() / df['meanSubA']) * 100
    df['covarSubB'] = (df['SubB'].std() / df['meanSubB']) * 100
    df['covarSubC'] = (df['SubC'].std() / df['meanSubC']) * 100
    #Создаем новый df для хранения будущих результатов
    df_res = pd.DataFrame(columns=['meanSubA', 'covarSubA', 'meanSubB', 'covarSubB', 'meanSubC', 'covarSubC'])
    #Записываем в первую строку наш результат(некая сводная таблица)
    df_res.loc[0] = [df['meanSubA'][0], df['covarSubA'][0], df['meanSubB'][0], df['covarSubB'][0],
                     df['meanSubC'][0], df['covarSubC'][0]]
    #Эспортируем результат в файл в формате csv
    df_res.to_csv("Result.csv", index=False, sep=';')
    print(df_res)
