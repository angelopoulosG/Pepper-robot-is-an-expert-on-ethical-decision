# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:12:58 2020

@author: Georgios Angelopoulos
"""



##############################################################################
##############################################################################

def triggers_deny_suggested(parsed_tree, question_context):
    for token in parsed_tree:
        if token.i == 0 and token.lemma_.lower() == 'no':
            return True
        if token.i == 0 and token.lemma_.lower() == 'yes':
            return False
        
        if (str(token.dep_) == 'neg' and str(token.head) in ['do', 'have']) or (str(token.dep_) == 'neg' and str(token.head) in ['agree']):
            return True
        


    return False



def triggers_accept_suggested(parsed_tree, question_context):

    for token in parsed_tree:
        if token.i == 0 and token.lemma_.lower() == 'no':
            return False
        if token.i == 0 and token.lemma_.lower() == 'yes':
            return True

        if (str(token.dep_) == 'neg' and str(token.head) in ['do', 'have']) or (str(token.dep_) == 'neg' and str(token.head) in ['agree']):
            return False
    for token in parsed_tree:
        if (str(token.dep_) != 'neg' and str(token.head) in ['do', 'have']) or (str(token.dep_) != 'neg' and str(token.head) in ['agree']):
            return True

    return False

##############################################################################
##############################################################################

def get_trigger_words_greeting():
    return ["hi", "hey", "hello", "morning", "afternoon", "evening", "night", "welcome"]


def triggers_greeting(root_tuple, parsed_tree):
    trigger_words_greeting = get_trigger_words_greeting()
    for token in parsed_tree:
        if str(token.lemma_) in trigger_words_greeting:
            return True

    return False

##############################################################################
##############################################################################

def get_trigger_words_goodbye():
    return ["bye", "goodbye", "ciao", "au-revoir"]

def triggers_request_goodbye(root_tuple, parsed_tree):
    trigger_words_goodbye = get_trigger_words_goodbye()
    for token in parsed_tree:
        if str(token.lemma_) in trigger_words_goodbye:
            return True
    return False

##############################################################################
##############################################################################

def get_trigger_words_cancel():
    return ["cancel", "stop"]

def triggers_request_cancel(root_tuple, parsed_tree):
    root_lemma, root_text = root_tuple
    trigger_words_cancel = get_trigger_words_cancel()
    for token in parsed_tree:

        if str(token.dep_) == 'neg' and root_lemma in trigger_words_cancel:
            return False
    if root_lemma in trigger_words_cancel:
        return True
    else:
        return False

##############################################################################
##############################################################################

def get_trigger_words_first():
    return ["first", "one"]

def triggers_request_first(root_tuple, parsed_tree):
    root_lemma, root_text = root_tuple

    trigger_words_first = get_trigger_words_first()
    for token in parsed_tree:

        if str(token.dep_) == 'neg' and root_lemma in ['choose', 'want', 'agree', 'chose']:
            return False
        if str(token.lemma_) in trigger_words_first:
            return True

    return False


##############################################################################
##############################################################################
    
def get_trigger_words_second():
    return ["second", "two"]

def triggers_request_second(root_tuple, parsed_tree):

    root_lemma, root_text = root_tuple

    trigger_words_second = get_trigger_words_second()
    for token in parsed_tree:

        if str(token.dep_) == 'neg' and root_lemma in ['choose', 'want', 'agree','chose']:
            return False
        if str(token.lemma_) in trigger_words_second:
            return True

    return False

##############################################################################
##############################################################################


def get_parse_tree_root_tuple(parsed_tree):
    for token in parsed_tree:
        if token.dep_ == 'ROOT':
            return token.lemma_, token.text




def determine_semantic_frame_from_parsed_tree(parsed_tree, question_context={}):

    root_tuple = get_parse_tree_root_tuple(parsed_tree)
    if triggers_greeting(
            root_tuple=root_tuple, parsed_tree=parsed_tree):
        return "greeting"
    elif triggers_request_goodbye(
            root_tuple=root_tuple, parsed_tree=parsed_tree):
        return "request_goodbye"
    elif triggers_request_cancel(
            root_tuple=root_tuple, parsed_tree=parsed_tree):
        return "request_cancel"
    elif triggers_request_second(
            root_tuple=root_tuple, parsed_tree=parsed_tree):
        return "request_second"
    elif triggers_request_first(
            root_tuple=root_tuple, parsed_tree=parsed_tree):
        return "request_first"
    elif triggers_accept_suggested(
            parsed_tree=parsed_tree, question_context=question_context):
        return "accept_suggested"
    elif triggers_deny_suggested(
            parsed_tree=parsed_tree, question_context=question_context):
        return "deny_suggested"

    else:
        return "False"

