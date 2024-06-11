class MustContainAtSymbolError(Exception):
    def __init__(self, msg):
        pass

class NameTooShortError(Exception):
    def __init__(self, msg):
        pass

class InvalidDomainError(Exception):
    def __init__(self, msg):
        pass


def email_validation(email):
    valid_domains = ['.com', '.bg', 'net', 'org']

    try:
        index_of_at = email.index('@')
        try:
            forth_element = email[:index_of_at][3]
            for i in range(len(valid_domains) + 1):
                try:
                    domain = valid_domains[i]
                    if domain in email:
                        return 'Email is valid'
                except IndexError:
                    raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
        except IndexError:
            raise NameTooShortError('Name must be more than 4 characters')

    except ValueError:
        raise MustContainAtSymbolError('Email must contain @')


current_email = input()
while current_email != 'End':
    print(email_validation(current_email))
    current_email = input()
