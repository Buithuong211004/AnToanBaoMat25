def mahoa(plaintext,k):
    ketqua=""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                start=ord('A')
            else:
                start=ord('a')
            ketqua=ketqua+chr((ord(i)-start+k)%26+start)
        else: ketqua=ketqua+i
    return ketqua

plaintext="BUI THI THUONG"
k=15
print(mahoa(plaintext,k))