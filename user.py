class User:
    """
    Class that generatesnew instances of users.
    """

    user_list=[]

    def __init__(self, username,password):
        self.username = username
        self.password = password

        def save_user(self):
            '''
            method to login user object to user list
            '''
            User.user_list.append(self)

        @classmethod
        def user_verification(cls,username,password):
            '''
            method to login user credentials on login
            '''
            for user in User.user_list:
                if(user.username == username and user.password == password):
                    return user