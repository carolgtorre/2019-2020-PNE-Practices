from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")

IP = "192.168.1.144"
PORT = 139
c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = "Hello from the teacher's server"
print(f"Response: {response}")
