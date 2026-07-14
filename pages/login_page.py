from pages.base_driver import BaseDriver


class LoginPage(BaseDriver):
    USERNAME_ID = "user-name"
    PASSWORD_ID = "password"
    LOGIN_BUTTON_ID = "login-button"

    #We have an update in method why we took the "id" out of the find method and put it in the base_driver.py file. So we can use it in other pages as well.

    def login(self, username, password):
        username_box = self.find(self.USERNAME_ID)
        password_box = self.find(self.PASSWORD_ID)
        login_button = self.find(self.LOGIN_BUTTON_ID)

        username_box.send_keys(username)
        password_box.send_keys(password)
        login_button.click()
