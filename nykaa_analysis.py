import pandas as pd

# Load all 5 sheets
sheets = {
    'Face Wash': 'Face Wash',
    'Moisturizers': 'Moisturizers', 
    'Kajal': 'Kajal & Eyeliner',
    'Shampoo': 'Shampoo',
    'Lip Care': 'Lip Care'
}

all_data = []
for name, sheet in sheets.items():
     df = pd.read_excel(r'C:\Users\arsma\Desktop\analytics\nykaa multi category.xlsx', 
                       sheet_name=sheet, 
                       header=1)
     df['Category'] = name
     all_data.append(df)
 
combined = pd.concat(all_data, ignore_index=True)

# Print column names first so we know what we're working with
print(combined.columns.tolist())
print(combined.shape)