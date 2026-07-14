from pages.base_driver import BaseDriver

class InventoryPage(BaseDriver):
    BACKPACK_ADD_TO_CART_ID = "add-to-cart-sauce-labs-backpack"

    def add_backpack_to_cart(self):
        button = self.find("id", self.BACKPACK_ADD_TO_CART_ID)
        button.click()
    
    def go_to_cart(self):
        badge = self.find("class name", "shopping_cart_badge")
        return badge.text
    