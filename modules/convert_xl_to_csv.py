
import pandas as pd
def convert_xl_to_csv(xl_file):

    try:
        df = pd.read_excel(xl_file)

        df.to_csv('result.csv', index=False)
        headers={'Content-Type': 'text/csv'}
        
        return f'Successfully converted {xl_file} to result.csv'
    except Exception as e:
        return f'Error converting file: {e}'