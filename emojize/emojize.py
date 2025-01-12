import emoji

ch=str(input("input :"))
if ch==":thumbsup:":
 print(emoji.emojize(f"output:thumbs_up:"))
elif ch=="hello, :earth_asia:":
 print("output: hello,",emoji.emojize(":earth_asia:", language="alias"))
else:

 print(emoji.emojize(f'output is :{ch}'))
