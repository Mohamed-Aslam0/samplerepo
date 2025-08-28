rows = [
    ["id", "name", "salary"],
    [1, "Alice", 50000],
    [2, "Bob", 60000],
    [3, "Charlie", 70000],
    [4,"Aslam",1000000]
]

high_salary = [row[1] for row in rows[1:] if row[2] > 50000]
print(high_salary)
