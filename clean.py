import pandas as pd

def clean(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged_df = merged_df.drop(columns=['id'])
    merged_df = merged_df.dropna()
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    return merged_df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='respondent_contact (CSV)')
    parser.add_argument('input2', help='respondent_other (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)

    merged_df_shape = cleaned.shape
    print(merged_df_shape)