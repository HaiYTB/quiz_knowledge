def check_answer(question, ans):
    """
    Hàm kiểm tra đáp án
    """
    if ans == str(question["correctAnswer"]):
        return True
    else:
        return False