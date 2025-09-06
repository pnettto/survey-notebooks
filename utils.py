def clean_df(df, extra_col):
    # Drop first row (empty)
    df = df.drop(df.index[0])

    # Add year column name
    df.iloc[0, 0] = "year"

    # Make years the header
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])

    # Drop all rows starting with Nan
    df = df.dropna(subset=[df.columns[0]])

    # # Remove indicator group titles
    patterns_to_remove = [
        "Utemiljö",
        "Missbruksproblem", 
        "Utomhusstörningar",
        "Andel uppfattat minst ett problem",
        "Utsatthet för brott",
        "Oro för att utsättas för brott",
        "Konkret känsla av otrygghet",
        "Polisens agerande mot problem",
        "Tillit"
    ]
    mask = ~df.iloc[:, 0].astype(str).str.startswith(tuple(patterns_to_remove))
    df = df[mask]

    # Transpose df
    df = df.transpose()

    # Make the first row the header
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])

    # Reset index
    df = df.reset_index()

    # Rename first column to "year"
    df.columns.values[0] = "year"

    # Remove rows with 'Year' == '2020_1' or '2016_1'
    df = df[~df['year'].isin(['2020_1', '2016_1'])]

    # Rename '2020_2' to '2020' and '2016_2' to '2016', etc
    df['year'] = df['year'].replace({'2020_2': '2020', '2016_2': '2016', '2006*': '2006'})
    
    # Rename special characters ä, å and ö
    df.columns = df.columns.str.replace('ä', 'a').str.replace('å', 'a').str.replace('ö', 'o')

    # Rename columns to snake_casing for easier coding
    df.columns = df.columns.str.replace(' ', '_').str.replace('.', '').str.replace(',', '').str.lower()

    # Transform years to numbers
    df["year"] = df["year"].astype(int)

    # Transform numeric columns to numbers
    df = df.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',', '.'), errors="coerce") if x.dtype == 'object' else x)

    # Add extra column
    if isinstance(extra_col, dict):
        for col_name, col_value in extra_col.items():
            df.insert(0, col_name, col_value)

    return df