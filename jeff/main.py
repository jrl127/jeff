import re
import long_responces as long

highest_prob_list = {}




def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # counts how many words are present in each predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # caculates the percent of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
#    highest_prob_list = {}
    tt = " "
    best_match = 0
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        # nonlocal = highest_prob_list
         highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    # 1-----------------------------------------
    ListA = {}
    response('Welcome!', ['hello', 'hi', 'sup', 'hey', 'heyo', 'hola'], single_response=True)
    all_values = highest_prob_list.values()
    a = max(all_values)
    b = max(highest_prob_list, key=highest_prob_list.get)
    ListA[b] = a
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    a = max(all_values)
    b = max(highest_prob_list, key=highest_prob_list.get)
    ListA[b] = a
    response('My name is Jeff! Hello human', ['What', 'is', 'your', 'name'], required_words=['hello', 'jeff'])
    a = max(all_values)
    b = max(highest_prob_list, key=highest_prob_list.get)
    ListA[b] = a
    best_match = max(ListA, key=ListA.get)

    return best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    response = check_all_messages(user_input)
    return response


# testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))












