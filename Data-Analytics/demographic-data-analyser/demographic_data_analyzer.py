import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=0)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    rows, cols = df.shape
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors'].index) * 100 / rows, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = len(df[df['education'].isin(advanced)])
    lower_education = rows - higher_education

    # percentage with salary >50K
    advanced_50k = len(df[(df['education'].isin(advanced)) & (df['salary'] == '>50K')])
    normal_50k = len(df[(~df['education'].isin(advanced)) & (df['salary'] == '>50K')])
    higher_education_rich = round(advanced_50k * 100 / higher_education, 1)
    lower_education_rich = round(normal_50k * 100 / lower_education, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_min_hours = len(df[df['hours-per-week'] == min_work_hours])
    num_min_workers = len(df[(df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)])

    rich_percentage = round(num_min_workers * 100 / total_min_hours, 1)

    # What country has the highest percentage of people that earn >50K?
    country_df = df.groupby('native-country').size()
    high_earning_df = df[df['salary'] == '>50K'].groupby('native-country').size()
    high_earning_df_percentage = high_earning_df / country_df

    highest_earning_country = high_earning_df_percentage.sort_values(ascending=False).index[0]
    highest_earning_country_percentage = round(high_earning_df_percentage.sort_values(ascending=False)[0] * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_50k = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = india_50k.groupby('occupation').size().sort_values(ascending=False).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
