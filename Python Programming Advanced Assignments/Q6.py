sensor_input = """sensor- reading:20,high:40,low:10
sensor- reading:50,high:40,low:10
sensor- reading:5,high:40,low:10
sensor- reading:30,high:40,low:10"""

lines = sensor_input.split("\n")
for i in lines:
    print(i)