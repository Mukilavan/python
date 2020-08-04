def brackets(expression):
   all_br = ['()', '{}', '[]']
   while any(x in expression for x in all_br):
      for br in all_br:
         expression = expression.replace(br, '')
   return not expression
input_string = input()
if brackets(input_string):
   print("Yes")
else:
   print("No")
