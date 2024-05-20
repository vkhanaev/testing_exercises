import datetime
import decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    raw_card1 = "1000200030004000"
    raw_card2 = "9999888800004000"
    raw_card3 = "5000000000004000"

    card1 = BankCard(raw_card1[-4:], "Tom")
    card2 = BankCard(raw_card2[-4:], "Tom")
    card3 = BankCard(raw_card3[-4:], "Jerry")
    cards = [card1, card2, card3]

    raw_card = raw_card2
    raw_date = "20.05.24"
    raw_time = "20:30"
    spend_in = "Shop"
    raw_sum = "123 00"
    authcode = 5555
    raw_details = f"{raw_card} {raw_date} {raw_time} {spend_in} authcode {authcode}"
    sms_text = f"{raw_sum}, {raw_details}"
    sms_message = SmsMessage(sms_text, "author", datetime.datetime.now())

    amount = decimal.Decimal(raw_sum.split(' ')[-2])
    card = [c for c in cards if c.last_digits == raw_card[-4:]][0]
    spend_at = datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M')
    expected_result = Expense(amount, card, spend_in, spend_at)

    assert parse_ineco_expense(sms_message, cards) == expected_result
