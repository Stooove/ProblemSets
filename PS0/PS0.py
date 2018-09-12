# Problem Set 0
# Name: Steve
# Collaborators: None
# Time: 2 min
#


def main():
    firstname = name('first')
    lastname = name('last')
    print (firstname)
    print (lastname)


def name(whichname):
    nameinput = input('Enter your {} name: '.format(whichname))
    return nameinput


if __name__ == '__main__':
    main()