import pandas as pd
import env
from babel.numbers import format_currency




def wrangle_zillow(df):
    '''Read the zillow sql database into a pandas dataframe 
        where only the 2017 Single Family residential properties show along with the following columns:
        bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, 
        taxvaluedollarcnt, yearbuilt, taxamount, and fips.

        Dropping all nulls from the dataset,
        and converting dtypes to drop decimals on fips, yearbuilt, and calculated square feet columns.

        Imported currency converter for taxamount and taxvalue in USD.

        Rename columns to: Bedroom_count, Bathroom_count, square_feet, Tax_value, Tax_amount and Fips_code
    '''

    #Acquire zillow database from MySQL
    df = pd.read_sql("SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt,  taxamount , fips FROM properties_2017 JOIN propertylandusetype USING (propertylandusetypeid)WHERE propertylandusetype.propertylandusedesc = 'Single Family Residential';", env.get_db_url('zillow'))

    #Dropped all nulls
    df = df.dropna()

    #Changing dtype of Fips, squarefeet and yearbuilt
    df['fips'] = df['fips'].astype('int')
    df['yearbuilt'] = df['yearbuilt'].astype('int')
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].astype('int')

    #Renamed columns for easier reading
    df = df.rename(columns={"bedroomcnt": "Bedroom_Count", "bathroomcnt": "Bathroom_count", "calculatedfinishedsquarefeet": "square_feet", "taxvaluedollarcnt": "Tax_Value", "taxamount": "Tax_amount", "fips": "Fips_code"})

    return df