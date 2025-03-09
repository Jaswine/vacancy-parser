

FAILED_SYMBOL = '@'

def is_email_checker(string: str) -> bool:
    """
        Check that the string is an email
        :param string: str - Some string
        :return: Checking status, Is an email or not
    """
    return True if FAILED_SYMBOL in string else False