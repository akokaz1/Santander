import pandas as pd

data_df = pd.read_csv('games.csv')

#  Dealing with NA's/nulls

#print data_df.shape
print pd.isnull(data_df).any()

data_df['ind_empleado'].replace('', 'N', inplace=True)
print data_df.shape
print pd.isnull(data_df).any()

'''
# Lines 20 -37 I convert the data types of the columns
data_df['fecha_dato'] = data_df['fecha_dato'].astype('datetime64[ns]')
data_df['ncodpers'] = data_df['ncodpers'].astype('int')
data_df['ind_empleado'] = data_df['ind_empleado'].astype('string')
data_df['sexo'] = data_df['sexo'].astype('string')
data_df['age'] = data_df['age'].astype('int')
data_df['ind_nuevo'] = data_df['ind_nuevo'].astype('int')
data_df['antiguedad'] = data_df['antiguedad'].astype('int')
data_df['indext'] = data_df['indext'].astype('string')
try:
    data_df['cod_prov'] = data_df['cod_prov'].astype('int')
except ValueError:
    data_df['cod_prov'] = data_df['cod_prov'].astype('string')
data_df['ind_actividad_cliente'] = data_df['ind_actividad_cliente'].astype('int')
try:
    data_df['renta'] = data_df['renta'].astype('float')
except:
    data_df['renta'] = data_df['renta'].astype('string')
data_df['segmento'] = data_df['segmento'].astype('string')

# Now I deal with NA/nulls
'''
