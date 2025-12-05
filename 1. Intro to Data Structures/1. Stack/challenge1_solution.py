import stack_finished

string = "ygolonhcet nies gnuak si eman ym"
reversed_string = ""
s = stack_finished.Stack()

# Your solution here.
for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)
