import base64
import os
import sys

# if sys.argv[1] == "crypt":
#     print(sys.argv[2])
# elif sys.argv[1] == "decrypt":
#     print("siuu",sys.argv[2])


if (sys.argv[1] != "crypt") and (sys.argv[1] != 'decrypt'):
    sys.exit("[ERROR] First arg err")
else:
    if (len(sys.argv) - 1) != 2:
        sys.exit("[ERROR] Should be 2 args")
    else:
        if sys.argv[1] == "crypt":
            text = sys.argv[2]
            result = base64.b64encode(text.encode("ascii"))
            print("Encrypting...")
            print(result.decode("ascii"))
        elif sys.argv[1] == "decrypt":
            text = sys.argv[2]
            result = base64.b64decode(text.encode("ascii"))
            print("Decrypting...")
            print(result.decode("ascii"))

# SGVsbG9Xb3JsZA==
# text = sys.argv[1]
# print(base64.b64encode(text.encode("ascii")))
#
# text = sys.argv[1]
# itog = base64.b64decode(text.encode("ascii"))
# print(itog.decode('ascii'))