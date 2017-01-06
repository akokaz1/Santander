'''This scrip takes the training data creates a new csv file which only contains the features I'm interested in '''


import pandas as pd

data_df = pd.read_csv('train_ver2.csv')
data_df = data_df[['fecha_dato',
                'ncodpers',
                'ind_empleado',
                'sexo',
                'age',
                'ind_nuevo',
                'antiguedad',
                'indext',
                'cod_prov',
                'ind_actividad_cliente',
                'renta',
                'segmento']]

data_df.to_csv('games.csv')
