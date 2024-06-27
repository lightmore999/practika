x_arr=[1,2,3,4,5,6,7,8,9,10,11]
y_arr=[8,8,0,5,5,2,4,3,8,9,6]
n = float(11)
x= 0
y=0
xy=0
xx=0
o=0

for i in x_arr:
    x += i
    xx += i * i
    y += y_arr[i-1]
    xy += i * y_arr[i-1]

a = (n * xy - x * y) / (n* xx - x * x)
b = (y - a * x) / n

for i in x_arr:
    o += (y_arr[i-1] - (a * i + b)) * (y_arr[i-1] - (a * i + b))
    

print(f"y = {round(a,2)}x + {round(b,2)}")
print(o)
# print(x, y, xy, xx, a , b, o)