import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)




from playwright.sync_api import sync_playwright

from pages.login import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_member import AddMemberPage

from utils.excelreader import get_member_data


def test_add_members():

    members = get_member_data(
        "data/memberlist.xlsx"
    )

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        login = LoginPage(page)
        dashboard = DashboardPage(page)
        member_page = AddMemberPage(page)

        login.login(
            "testclerkho.stts@example.com",
            "Admin@123"
        )

        for member in members:

            dashboard.navigate_to_add_member()

            member_page.create_member(member)

        browser.close()


if __name__ == "__main__":
    test_add_members()