class User:
    """
    Class that generatesnew instances of users.
    """

    user_list=[]

    def __init__(self, username,password):
        self.username = username
        self.password = password