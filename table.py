for i in range(2,20):
    with open(f"table_multiplication_{i}", "w") as f:
        for j in range(1, 11):
            f.write(f"{i}*{j} = {i*j}\n")
