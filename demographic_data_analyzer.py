import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented in the dataset?
    race_count = df["race"].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. What percentage of people have a Bachelor's degree?
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. What percentage of people with advanced education make >50K?
    advanced_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (
            df[advanced_education]["salary"]
            .eq(">50K")
            .mean()
            * 100
        ),
        1
    )

    # 5. What percentage of people without advanced education make >50K?
    lower_education_rich = round(
        (
            df[~advanced_education]["salary"]
            .eq(">50K")
            .mean()
            * 100
        ),
        1
    )

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # 7. What percentage of people who work minimum hours make >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(
        (
            num_min_workers["salary"]
            .eq(">50K")
            .mean()
            * 100
        ),
        1
    )

    # 8. What country has the highest percentage of people that earn >50K?
    country_salary = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(), 1
    )

    # 9. Most popular occupation for people who earn >50K in India
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:")
        print(race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage with Bachelors degrees:",
            percentage_bachelors
        )
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )
        print(
            "Min work time:",
            min_work_hours,
            "hours/week"
        )
        print(
            "Percentage of rich among min workers:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )
        print(
            "Top occupations in India:",
            top_IN_occupation
        )

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }