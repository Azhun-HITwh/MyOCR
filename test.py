import easyocr
import re

pattern = r"^\d{1,2}0\d$"
reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)
result = reader.readtext('test.jpg', detail=0)
# print(result)
for i in range(0, len(result)):
    # print(i, '\n')
    if re.match(pattern, result[i]):
        print("No.:", result[i], "area:", result[i+1], "price:", result[i+2], "total:", result[i+3], "\n")
        i += 4
