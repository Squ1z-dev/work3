import numpy as np
import pandas as pd

names = ["Максим", "Андрій", "Анна", "Настя", "Оксана","Микита","Іван","Олександр","Христя"]
students = np.random.choice(names, 100)
age = np.random.randint(16,30,100)
grades_math =np.random.randint(0,101, 100)
grades_prog =np.random.randint(0,101, 100)

df = pd.DataFrame({
    "Name": students,
    "Age": age,
    "Math grades": grades_math,
    "Programing grades": grades_prog

})

df["Avarage grades"] = (df["Math grades"]+ df["Programing grades"])/2
students_over_80 = df[df["Avarage grades"]>80]

df["Status"] = np.where(
    df["Avarage grades"] >= 75,
    "Pass",
    "Fail"
)
pased = (df["Status"]=="Pass").sum()
failed= (df["Status"]=="Fail").sum()
print("Passed: ", pased)
print("Failed: ", failed)

df.to_csv("students_results.csv", index=False)
print("sucsessfully ended ")