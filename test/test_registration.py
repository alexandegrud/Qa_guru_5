from selene.support.shared import browser
from selene import be, have, command
import os

browser.config.hold_browser_open = True

def test_student_registration_form(practice_form_open_browser):
    # Данные пользователя
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Alexander')
    browser.element('#lastName').type('Grudinkin')
    browser.element('#userEmail').type('grudalex@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('89214556789')

    # Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1999"]').click()
    browser.element('.react-datepicker__day--005').click()

    # Хобби и фото
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../pict/Guru_test.jpg'))


    # Адресс
    browser.element('#currentAddress').type('улица Шостаковича')
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()


    # Проверка
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Alexander Grudinkin',
        'grudalex@mail.ru',
        'Male',
        '8921455678',
        '05 August,1999',
        'English',
        'Reading',
        'Guru_test.jpg',
        'улица Шостаковича',
        'Haryana Karnal'))
