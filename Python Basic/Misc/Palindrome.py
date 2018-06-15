class Palindrome(object):
    """description of class"""

    __max = 10
    min = 5

    def check_palindrome(self, text):
        return text == text[::-1]

        
