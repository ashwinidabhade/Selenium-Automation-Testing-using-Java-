from enum import member


class AddMemberPage:

    def __init__(self, page):
        self.page = page

    def create_member(self, member):

        # Sabha Selection
        self.page.locator(
        "xpath=/html/body/div/div/div/main/div/form/div[1]/div[2]/div[1]/div[1]/button"
        ).click()
        self.page.wait_for_timeout(1000)


        # Salutation
        self.page.locator(
        "xpath=/html/body/div/div/div/main/div/form/div[2]/div[2]/div[1]/div[1]/button"
        ).click()

        self.page.locator('[role="option"]').filter(
        has_text=str(member["Salutation"])
        ).first.click()
        # Name Details
        self.page.fill(
        "xpath=/html/body/div/div/div/main/div/form/div[2]/div[2]/div[1]/div[2]/input",
        str(member["FirstName"])
        )
        self.page.wait_for_timeout(500)

        self.page.fill(
            "xpath=/html/body/div/div/div/main/div/form/div[2]/div[2]/div[1]/div[3]/input",
            str(member["MiddleName"])
        )
        self.page.wait_for_timeout(500)


        self.page.fill(
            "xpath=/html/body/div/div/div/main/div/form/div[2]/div[2]/div[1]/div[4]/input",
            str(member["LastName"])
        )
        self.page.wait_for_timeout(500)


        # DOB
        dob = str(member["DOB"]).split(" ")[0]

        print("DOB =", dob)

        self.page.fill(
         "xpath=/html/body/div/div/div/main/div/form/div[2]/div[2]/div[3]/div[1]/input",
        dob
       )
        self.page.wait_for_timeout(500)


        #  Joining Date
        joining_date = str(member["Joining Date"]).split(" ")[0]

        print("Joining Date =", joining_date)

        self.page.fill(
         "xpath=/html/body/div/div/div/main/div/form/div[2]/div[2]/div[3]/div[2]/input",
        joining_date
         )
        self.page.wait_for_timeout(500)

        # Address
        self.page.fill(
            "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[1]/input",
            str(member["Address"])
        )
        self.page.wait_for_timeout(500)
        # State
        self.page.locator(
        "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[2]/div[1]/button"
        ).click()

        self.page.get_by_role("option",name=str(member["State"])
        ).click()
        self.page.wait_for_timeout(2000)

        # District
        self.page.locator(
        "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[2]/div[2]/button"
        ).click()

        self.page.get_by_role("option",name=str(member["District"])).click()
        self.page.wait_for_timeout(2000)



        # Taluka
        self.page.locator(
        "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[2]/div[3]/button"
        ).click()

        self.page.get_by_role("option",name=str(member["Taluka"])).click()
        self.page.wait_for_timeout(2000)


        # City
        self.page.locator(
        "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[2]/div[4]/button"
        ).click()

        self.page.get_by_role("option",name=str(member["City"])).click()
        self.page.wait_for_timeout(2000)



        # Pincode
        self.page.fill(
            "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[2]/div[5]/input",
            str(member["Pincode"])
        )

        # Email
        self.page.fill(
            "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[4]/div[1]/input",
            str(member["Email"])
        )

        # Mobile
        self.page.fill(
            "xpath=/html/body/div/div/div/main/div/form/div[3]/div[2]/div[4]/div[2]/input",
            str(member["Mobile"])
        )
        self.page.wait_for_timeout(500)

        #category
        self.page.locator("xpath=/html/body/div/div/div/main/div/form/div[4]/div[2]/div[1]/div/div[1]/button").click()
        self.page.get_by_role("option", name=str(member["Category"])).click()
        self.page.wait_for_timeout(1000)

        # #payment mode
        # # self.page.get_by_text("Cheque").click()
        # self.page.get_by_text(
        # str(member["Payment Mode"])
        # ).click()
        # self.page.wait_for_timeout(500)

        #payment date
        payment_date = str(member["Payment Date"]).split(" ")[0]

        print("Payment Date =", payment_date)

        self.page.fill(
         "xpath=/html/body/div/div/div/main/div/form/div[4]/div[2]/div[5]/input",
        payment_date
         )
        self.page.wait_for_timeout(500)




        # Declaration
        self.page.check(
            "xpath=/html/body/div/div/div/main/div/form/div[5]/div[1]/div/button"
        )
        self.page.wait_for_timeout(500)

        # Submit
        self.page.locator(
            "xpath=/html/body/div/div/div/main/div/form/div[5]/div[2]/button[2]"
        ).click()

        self.page.wait_for_timeout(2000)