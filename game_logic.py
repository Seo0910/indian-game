from player import get_remaining_cards

def calculate_win_prob(card, opponent_card, is_player=True):
    remaining = get_remaining_cards(card, opponent_card)
    if is_player:
        wins = sum(1 for c in remaining if c > opponent_card)
    else:
        wins = sum(1 for c in remaining if c < opponent_card)
    return int((wins / len(remaining)) * 100)

def expected_reward(win_prob, max_amount=100):
    return int(max_amount * (1 - win_prob / 100))

def resolve_round(player_card, computer_card, player_bets, player_money, computer_money, player_prob, computer_prob):
    explanation = ""
    round_result = ""

    player_expected = expected_reward(computer_prob)
    computer_expected = expected_reward(player_prob)

    if not player_bets:
        if player_card > computer_card:
            player_money -= computer_expected
            computer_money += computer_expected
            round_result = "�������� �ʾ� ���� ������ϴ�."
            explanation = f"����� ��� ���� ���� �ս�: {computer_expected}��\n��� �¸� ó����"
        elif player_card < computer_card:
            loss = int(player_money / 3)
            player_money -= loss
            computer_money += loss
            round_result = "�й�! (���� �� ��)"
            explanation = f"���� �ս� ����: ���� �ڻ��� 1/3\n���� �ݾ�: {loss}��"
        else:
            round_result = "���º�"
            explanation = "���� ���� �� ���� �̵� ����"
    else:
        if player_card > computer_card:
            player_money += computer_expected
            computer_money -= computer_expected
            round_result = "�¸�!"
            explanation = f"��� ��� �ս� ���� ����: {computer_expected}��\n���� {player_prob}% Ȯ���� �����ϴ�."
        elif player_card < computer_card:
            player_money -= player_expected
            computer_money += player_expected
            round_result = "�й�!"
            explanation = f"�� ��� ���� ���� �ս�: {player_expected}��\n���� {computer_prob}% Ȯ���� �����ϴ�."
        else:
            round_result = "���º�"
            explanation = "���� ���� �� ���� �̵� ����"

    return player_money, computer_money, round_result, explanation
