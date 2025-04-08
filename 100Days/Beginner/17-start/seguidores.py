class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Luis")
user_2 = User("002","Zam")

user_1.follow(user_2)

print(f'{user_1.id} {user_1.username} Seguidores: {user_1.followers} Seguidos: {user_1.following}')
print(f'{user_2.id} {user_2.username} Seguidores: {user_2.followers} Seguidos: {user_2.following}')