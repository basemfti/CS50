print("File name :")
ch=input("")
y= ch.split('.')[-1]
x= ch.split('.')[0]
if y=="gif":
   print("image/gif")
elif y=="zip":
   print("application/zip")
elif y=="jpg":
   print("image/jpeg")
elif y=="jpeg":
   print("image/jpeg")
elif y=="png":
   print("image/png")
elif y=="pdf":
   print("application/pdf")
elif y=="PDF":
   print("application/pdf")
elif ch=="plain.txt":
   print("text/plain")
elif ch=="document.PDF":
   print("application/pdf")


else:
   print("application/octet-stream")
