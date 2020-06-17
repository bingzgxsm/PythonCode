# 使用 raw_input()转换温度

print "这个程序把华氏度转为摄氏度"
print "输入一个华氏度数值: ",
fahrenheit = float(raw_input())           # Get the Fahrenheit temperature from the user
celsius = (fahrenheit - 32) * 5.0 / 9
print "这个华氏度经转换后为",                          # Notice the commas at the ends
print celsius,                            #   of these lines
print "摄氏度"
