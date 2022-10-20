import pandas as pd
c = pd.read_excel("C:\\excelsheet\\Book1.xlsx")
df = pd.DataFrame(c)
print(df)
print("After sorting years_of_experience:")
print()
print(df.sort_values("Years_of_experience" , ascending=False))

'''Name  Years_of_experience        DOB
0        sahithi                   12 1995-09-02
1        manogna                    8 1994-03-12
2        vanitha                   12 1989-03-04
3  sruthikeerthi                    5 1994-04-12
4          priya                    3 1984-04-11
After sorting years_of_experience:

            Name  Years_of_experience        DOB
0        sahithi                   12 1995-09-02
2        vanitha                   12 1989-03-04
1        manogna                    8 1994-03-12
3  sruthikeerthi                    5 1994-04-12
4          priya                    3 1984-04-11'''
