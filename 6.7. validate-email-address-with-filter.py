def fun(s):
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False

    username_valid = username.replace('-', '').replace('_', '').isalnum()
    extension_valid = len(extension) <= 3
    website_valid = website.isalnum()

    return username_valid and extension_valid and website_valid


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    # fun('joan.santiago.cabezas@gmail.com')
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
