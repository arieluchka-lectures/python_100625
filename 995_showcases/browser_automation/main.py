import re
import time

from playwright.sync_api import sync_playwright

STUDENT_NAME_COLUMN = ".cell.c1"
STUDENT_EMAIL_COLUMN = ".cell.c2"
STUDENT_PRESENT_COLUMN = ".cell.c3"
STUDENT_ABSENT_COLUMN = ".cell.c6"
USERNAME = "123456789"
PASSWORD = "secretpass123"



LESSON_SUBJECT = input("What is the subject of the lesson? ")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://online.ash-limudim.co.il/login/index.php")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Log in", exact=True).click()
    # page.goto("https://online.ash-limudim.co.il/mod/attendance/take.php?id=24473&sessionid=24078&grouptype=0")


    # create new one
    page.goto("https://online.ash-limudim.co.il/course/view.php?id=1053")
    page.get_by_role("link", name="נוכחות תלמידים").click()
    page.get_by_role("link", name="הוספת מפגש").click()
    page.locator("#id_sestime_starthour").select_option("17")
    page.locator("#id_sestime_endhour").select_option("22")
    page.get_by_role("textbox", name="תאור").fill(LESSON_SUBJECT)
    page.get_by_role("button", name="הוספה").click()



    page.goto("https://online.ash-limudim.co.il/course/view.php?id=1053")
    # page.pause()
    page.get_by_role("link", name="נוכחות תלמידים").click()
    page.get_by_role("link", name="ימים").click()
    time.sleep(1)
    page.get_by_role("link", name="רישום נוכחות").click()
    time.sleep(1)


    attendance_table = page.get_by_role("table").all()[1]
    student_rows = attendance_table.get_by_role("row").all()[2:]
    for student_row in student_rows:
        student_row.locator(STUDENT_NAME_COLUMN).scroll_into_view_if_needed()
        student_name = student_row.locator(STUDENT_NAME_COLUMN).inner_text()

        while True:
            is_student_here = input(f"Is the student '{student_name}' in the zoom? ")
            if is_student_here.lower() != "" and (is_student_here.lower() in "yes" or is_student_here.lower() in "no"): # will work with "Y" "y" "yes" "Yes"
                break
            else:
                print("Something is wrong with input. Make sure to answer with 'y' or 'n'")

        if is_student_here.lower() in "yes":
            student_row.locator(STUDENT_PRESENT_COLUMN).click()
            continue
        elif is_student_here.lower() in "no":
            continue

    page.get_by_role("button", name="שמירת נתוני נוכחות").click()


    # ---------------------
    context.close()
    browser.close()

