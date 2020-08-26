import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*/.!@#$%^&|\<>?.,;:"

all = lower + upper + numbers + symbols

length = 16
password = "".join(random.sample(all,length))
print("Este es tu nuevo password: ", password)