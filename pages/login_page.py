from pages.base_driver import BaseDriver


class LoginPage(BaseDriver):
    USERNAME_ID = "user-name"
    PASSWORD_ID = "password"
    LOGIN_BUTTON_ID = "login-button"

    
#this method is for logging in to the application. We can use it in other pages as well.
    def login(self, username, password):
        username_box = self.find("id", self.USERNAME_ID)
        password_box = self.find("id", self.PASSWORD_ID)
        login_button = self.find("id", self.LOGIN_BUTTON_ID)

        username_box.send_keys(username)
        password_box.send_keys(password)
        login_button.click()
