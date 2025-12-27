import pytest
import allure
from pages.main_page import MainPage
from data.data_important_questions import AllAnswer
from locators.locators_main_page import ElementsMainPage as EMP

class TestImportantQuestions:

    questions_data = [
        (0, EMP.ELEMENT_FIRST,   AllAnswer.answer_one),
        (1, EMP.ELEMENT_SECOND,  AllAnswer.answer_two),
        (2, EMP.ELEMENT_THIRD,   AllAnswer.answer_three),
        (3, EMP.ELEMENT_FOURTH,  AllAnswer.answer_four),
        (4, EMP.ELEMENT_FIFTH,   AllAnswer.answer_five),
        (5, EMP.ELEMENT_SIXTH,   AllAnswer.answer_six),
        (6, EMP.ELEMENT_SEVENTH, AllAnswer.answer_seven),
        (7, EMP.ELEMENT_EIGHTH,  AllAnswer.answer_eight)
    ]

    @allure.title('Проверка соответствия ответов под каждым вопросом')
    @allure.description('Тест-кейс на проверку текста ответа под вопросами"')
    @pytest.mark.parametrize("question_index, answer_locator, expected_answer", questions_data)
    def test_visibility_text_questions(self, driver, website, question_index, answer_locator, expected_answer):
        driver.get(website)
        section = MainPage(driver)
        section.scroll_bottom_page()
        section.click_questions(question_index)
        section.wait_answer(answer_locator)
        answer_text = driver.find_element(*answer_locator).text
        # Проверяем каждый текст ответа
        assert answer_text == expected_answer
