

with open("../excel_matur/Dane/soki.txt", "r") as file1:
    data = list(map(str.replace('\\t',"").strip("\\n", ""), file1.readlines()))
    # for i in data:
    #     print(i)
    print(data)
    file1.close()

# with open("../excel_matur/Dane/soki.txt", "r") as file1:
#     data = [line.replace("\t", "").replace("\n", "") for line in file1]
#     print(data)

