t=input()
if((t>='a' and t<='z') or (t>='A' and t<='Z')):
  if(t== 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u' or t == 'A'
       or t == 'E' or t == 'I' or t == 'O' or t == 'U'):
       print("Vowel")
  else:
       print("Consonant")
else:
  print("invalid")
