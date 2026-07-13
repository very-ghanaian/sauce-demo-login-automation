from pages.base_driver import BaseDriver


class LoginPage(BaseDriver):
    USERNAME_ID = "user-name"
    PASSWORD_ID = "password"
    LOGIN_BUTTON_ID = "login-button"

    def login(self, username, password):
        username_box = self.driver.find_element("id", self.USERNAME_ID)
        password_box = self.driver.find_element("id", self.PASSWORD_ID)
        login_button = self.driver.find_element("id", self.LOGIN_BUTTON_ID)

        username_box.send_keys(username)
        password_box.send_keys(password)
        login_button.click()
