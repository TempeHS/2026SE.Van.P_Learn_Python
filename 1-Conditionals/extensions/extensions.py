extensions = input("What file? ")
if extensions.endswith(".jpg"):
    print("image/jpeg")
elif extensions.endswith(".pdf"):
    print("application/pdf")
elif extensions.endswith(".gif"):
    print("image/gif")
elif extensions.endswith(".jpeg"):
    print("image/jpeg")
elif extensions.endswith(".png"):
    print("image/png")
elif extensions.endswith(".txt"):
    print("text/plain")
elif extensions.endswith(".zip"):
    print("application.zip")
else:
    print("application/octet-stream")