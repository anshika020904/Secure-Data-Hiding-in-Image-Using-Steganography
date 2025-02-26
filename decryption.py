import cv2

img = cv2.imread("encryptedImage.png")

# Read stored password and message length
with open("secret_info.txt", "r") as f:
    stored_password = f.readline().strip()
    msg_length = int(f.readline().strip())

message = ""
n = 0
m = 0
z = 0

c = {i: chr(i) for i in range(255)}

pas = input("Enter passcode for Decryption: ")
if stored_password == pas:
    for i in range(msg_length):  # Read exactly the number of characters stored
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
