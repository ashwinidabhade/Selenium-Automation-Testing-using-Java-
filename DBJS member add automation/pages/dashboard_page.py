class DashboardPage:

    def __init__(self, page):
        self.page = page

    def navigate_to_add_member(self):

        self.page.locator("xpath=/html/body/div/div/div/aside/div/nav/div[1]/button/div").click()

        self.page.locator("xpath=/html/body/div/div/div/aside/div/nav/div[1]/div/button[2]").click()