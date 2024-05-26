import datetime
import decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test__parse_ineco_expense__split_sms():
    sms = SmsMessage(text="123 00, 1000200030004000 20.05.24 20:30 spend_in authcode 5555",
                     author="author",
                     sent_at=datetime.datetime.now()
    )
    raw_sum, raw_details = sms.text.split(', ')
    assert raw_sum == "123 00"
    assert raw_details == "1000200030004000 20.05.24 20:30 spend_in authcode 5555"


def test__parse_ineco_expense__split_raw_details_split_authcode():
    raw_details = "1000200030004000 20.05.24 20:30 spend_in authcode 5555"
    raw_details = raw_details.split(' authcode ')[0]
    assert raw_details == "1000200030004000 20.05.24 20:30 spend_in"


def test__parse_ineco_expense__split_raw_details_split():
    raw_details = "1000200030004000 30.11.24 20:30 spend_in"
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    assert raw_card == "1000200030004000"
    assert raw_date == "30.11.24"
    assert raw_time == "20:30"
    assert spend_in == "spend_in"


def test__parse_ineco_expense__amount_of_only_rubles():
    raw_sum = "999 00"
    amount = decimal.Decimal(raw_sum.split(' ')[-2])
    assert amount == decimal.Decimal(999)


def test__parse_ineco_expense__amount_of_rubles_with_kopeks():
    raw_sum = "999 99"
    amount = decimal.Decimal(raw_sum.split(' ')[-2])
    assert amount == decimal.Decimal(999)


def test__parse_ineco_expense__one_card():
    raw_card = "1000200030004000"
    cards = [BankCard(raw_card[-4:], "Name1")]
    card=[c for c in cards if c.last_digits == raw_card[-4:]][0]
    assert card == BankCard('4000', "Name1")


def test__parse_ineco_expense__many_card_with_one_owner():
    raw_card1 = "1000200030001000"
    raw_card2 = "9999888800002000"
    cards = [BankCard(raw_card1[-4:], "Name1"), BankCard(raw_card2[-4:], "Name1")]
    raw_card = raw_card2
    card=[c for c in cards if c.last_digits == raw_card[-4:]][0]
    assert card == BankCard('2000', "Name1")


def test__parse_ineco_expense__many_card_with_many_owners():
    raw_card1 = "1000200030001000"
    raw_card2 = "9999888800002000"
    raw_card3 = "5000000000001000"
    cards = [BankCard(raw_card1[-4:], "Name1"), BankCard(raw_card2[-4:], "Name1"), BankCard(raw_card3[-4:], "Name2")]
    raw_card = raw_card3
    card=[c for c in cards if c.last_digits == raw_card[-4:]][0]
    assert card == BankCard('1000', "Name1")


def test__parse_ineco_expense__spent_at():
    spent_at = datetime.datetime.strptime('30.11.24 23:59', '%d.%m.%y %H:%M')
    assert spent_at == datetime.datetime(2024, 11, 30, 23, 59)


def test__parse_ineco__expense():
    sent_at = datetime.datetime(2024, 11, 30, 23, 59)
    sms = SmsMessage(text="123 00, 1000200030009999 30.11.24 23:59 spend_in authcode 5555",
                     author="author",
                     sent_at=sent_at
                     )
    cards = [BankCard("9999", "Name")]

    expense = parse_ineco_expense(sms, cards)
    assert expense.amount == decimal.Decimal(123)
    assert expense.card == BankCard("9999", "Name")
    assert expense.spent_in == "spend_in"
    assert expense.spent_at == sent_at
