class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):

        self.page.goto("https://demo4.stsgram.com/")
        self.page.wait_for_load_state("networkidle")

        # Staff Login
        self.page.locator("xpath=/html/body/div/div/div[3]/div/div/div/div[2]/div[2]/button").click()

        self.page.fill("xpath=/html/body/div/div/div/div/div/div[2]/form/div[1]/input", username)
        self.page.fill("xpath=/html/body/div/div/div/div/div/div[2]/form/div[2]/input", password)

        self.page.locator("xpath=/html/body/div/div/div/div/div/div[2]/form/button").click()