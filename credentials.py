import random
import string
class Credential:
    """
    Class that generates new instances of Credentials.
    """
    credentials_list = [] #list of credentials
    
    def __init__(self,account,username,password):
        self.account= account
        self.username = username
        self.password = password
        
    def save_credential(self):
        '''
         method saves credential into credential_list
        '''
        Credential.credentials_list.append(self)
        
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in account name and returns credentials that match that account.
        Args:
            account: Account whose credentials to search for
        Returns :
            Credentials that match the account.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def credential_exist(cls,account):
        '''
        Method that checks if a crediantial exists from the credential list.
        
        Args:
            account: Account whose credentials to search for
        Returns :
            Boolean: True or false
        '''
        
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            
        return False
        
    @classmethod
    def display_credential(cls):
        '''
        method that returns the saved credentials
        '''
        return cls.credentials_list
    
    @classmethod
    def generate_password(cls,password_length):
        '''
        method to generate a random password
        '''
        char_password= string.ascii_letters+string.digits

        #password
        password=''.join(random.choice(char_password)
        for i in range(password_length))
        return password
    
    def delete_credential(self):
        '''
        method deletes a saved credential from the credential_list
        '''
        Credential.credentials_list.remove(self)