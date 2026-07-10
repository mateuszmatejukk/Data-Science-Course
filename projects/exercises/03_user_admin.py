"""
Create a class User with attributes username, email, and password and methods:

- `__init__` - initialize the user with username, email, and password.
- `__repr__` - return a string representation of the user.
- `change_password` - change the user's password.
- `login` - print a message indicating the user has logged in.
"""


class User:
    def __init__(self, username, email, password):
        """
        Initialize the user with username, email, and password.

        Parameters:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        """
        pass

    def __repr__(self):
        """
        Return a string representation of the user.

        Returns:
        str: A string representation of the user in the format 'User(username, email)'.
        """
        pass

    def change_password(self, new_password):
        """
        Change the user's password.

        Parameters:
        new_password (str): The new password for the user.
        """
        pass

    def login(self, password):
        """
        Print a message indicating the user has logged in.

        Parameters:
        password (str): The password to log in.
        """
        pass


# Example usage
u1 = User("Alice", "alice@email.com", "strong_password")
print(u1)
u1.change_password("new_password")
u1.login("new_password")

"""
Add a class Admin that inherits from User with additional attributes role and permissions and methods:

- `__init__` - initialize the admin with username, email, password, role, and permissions.
- `__repr__` - return a string representation of the admin with permissions.
- `change_permissions` - change the admin's permissions.
- `login` - print a message indicating the admin has logged in.
- `show_permissions` - print the admin's permissions.
"""


class Admin(User):
    def __init__(self, username, email, password, role, permissions):
        """
        Initialize the admin with username, email, password, role, and permissions.

        Parameters:
        username (str): The username of the admin.
        email (str): The email of the admin.
        password (str): The password of the admin.
        role (str): The role of the admin.
        permissions (list): The permissions of the admin.
        """
        pass

    def __repr__(self):
        """
        Return a string representation of the admin with permissions.

        Returns:
        str: A string representation of the admin in the format 'Admin(username, email, role) Permissions: permissions'.
        """
        pass

    def add_permissions(self, new_permissions):
        """
        Change the admin's permissions.

        Parameters:
        new_permissions (list): The new permissions for the admin.
        """
        pass

    def show_permissions(self):
        """
        Print the admin's permissions.
        """
        pass


# Example usage
a1 = Admin(username="Bob", email="bob@email.com", password="admin_password", role="admin",
           permissions=["read", "write"], )
print(a1)
a1.add_permissions(new_permissions=["read", "write", "delete"])
a1.login("admin_password")
a1.show_permissions()
