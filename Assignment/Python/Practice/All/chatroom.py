class Chatroom:
    def __init__(self):
        self.users = {}

    def register(self, user):
        self.users[user.name] = user
        user.chatroom = self

    def send_message(self, message, from_user, to_user):
        if to_user in self.users:
            recipient = self.users[to_user]
            recipient.receive(message, from_user)
        else:
            print(f"User '{to_user}' not found in the chatroom.")

class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = None

    def send(self, message, to_user):
        if self.chatroom:
            self.chatroom.send_message(message, self.name, to_user)
        else:
            print("User is not registered in any chatroom.")

    def receive(self, message, from_user):
        print(f"{self.name} received message from {from_user}: {message}")

# Example usage
if __name__ == "__main__":
    chatroom = Chatroom()

    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Register users to chatroom
    chatroom.register(alice)
    chatroom.register(bob)
    chatroom.register(charlie)

    # Users sending messages
    alice.send("Hi Bob!", "Bob")
    bob.send("Hello Alice! How are you?", "Alice")
    charlie.send("Hey Alice, are you coming to the party?", "Alice")
