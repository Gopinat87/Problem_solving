def salary_analysis(salaries):

    highest = max(salaries)
    lowest = min(salaries)
    average = sum(salaries) / len(salaries)

    print("Highest:", highest)
    print("Lowest :", lowest)
    print("Average:", average)

salary_analysis([25000,30000,45000,28000])