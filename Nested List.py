if __name__ == "__main__":
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score


    mini = list(set(students.values()))
    mini.sort()
    key_with_value = [key for key, value in students.items() if value == mini[1]]
    print(key_with_value)
    key_with_value.sort()

    print(*key_with_value, sep="\n")
