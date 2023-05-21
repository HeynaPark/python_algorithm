def solution(phone_book):
    phone = sorted(phone_book)

    for p1, p2 in zip(phone, phone[1:]):
        if p2.startswith(p1):
            return False
    return True
