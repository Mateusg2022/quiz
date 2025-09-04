import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_choice_passing():
    question = Question(title='q1')

    c1 = question.add_choice('a', False)
    c2 = question.add_choice('b', False)
    c3 = question.add_choice('c', True)

    assert not c1.is_correct
    assert not c2.is_correct
    assert c3.is_correct

def test_remove_choice_by_id():
    question = Question(title='q1')
    c1 = question.add_choice('a', False)
    
    assert len(question.choices) == 1

    question.remove_choice_by_id(c1.id)

    assert len(question.choices) == 0

def test_remove_all_choices():

    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', True)

    assert len(question.choices) == 3

    question.remove_all_choices()
   
    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q1')

    c1 = question.add_choice('a', False)
    c2 = question.add_choice('b', False)
    c3 = question.add_choice('c', False)

    assert not c1.is_correct
    assert not c2.is_correct
    assert not c3.is_correct

    lista_corretas = [c2.id, c3.id]

    question.set_correct_choices(lista_corretas)

    assert not c1.is_correct
    assert c2.is_correct
    assert c3.is_correct

def test_correct_selected_choices():
    question = Question(title='q1')

    c1 = question.add_choice('a', True)
    c2 = question.add_choice('b', False)
    c3 = question.add_choice('c', False)

    assert question.correct_selected_choices([c1.id]) == [c1.id]

def test_find_choice_by_id():
    question = Question(title='q1')

    c1 = question.add_choice('a', True)

    choiceId = question._find_choice_by_id(question.choices[0].id)

    assert choiceId == question.choices[0]

def test_find_correct_choice_ids():
    question = Question(title='q1')

    c1 = question.add_choice('a', True)
    c2 = question.add_choice('b', True)
    c3 = question.add_choice('c', False)

    correctChoicesIds = question._find_correct_choice_ids()

    assert correctChoicesIds == [c1.id, c2.id]

def test_check_valid_choice_id():
    question = Question(title='q1')

    c1 = question.add_choice('a', True)

    assert question._check_valid_choice_id(1) == None

def test_check_valid_choice_id_throw_exception():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question._check_valid_choice_id(3123123) 

def test_list_choice_ids():
    question = Question(title='q1')

    c1 = question.add_choice('a', True)
    c2 = question.add_choice('b', True)
    c3 = question.add_choice('c', False)

    assert question._list_choice_ids() == [c1.id, c2.id, c3.id]




    