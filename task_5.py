
import json

class TestCase:
    steps = {}
    result = ''
    def __init__(self, steps = {}, result = None):
        self.steps = steps
        self.result = result

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        step_to_remove = step_number
        if step_to_remove in self.steps:
            del self.steps[step_to_remove]
        else:
            print('no such step', step_to_remove)

    def set_result(self, result):
        self.result = result

   
    def get_test_case(self):
        test_case_dict = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }
        print(json.dumps(test_case_dict, ensure_ascii=False, indent=4))
    

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку «Удалить»')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()