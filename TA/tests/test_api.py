import requests


def test_new_shuffled_deck():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    assert response.ok
    print(response.json())


def test_draw_a_card():
    response = requests.get('https://deckofcardsapi.com/api/deck/bmk0ezfsf3ay/draw/?count=2')
    assert response.ok
    print(response.json())

def test_reshuffle_a_deck():
    response = requests.get('https://deckofcardsapi.com/api/deck/bmk0ezfsf3ay/shuffle/')
    assert response.ok
    print(response.json())

def test_create_new_deck():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/')
    assert response.ok
    print(response.json())







