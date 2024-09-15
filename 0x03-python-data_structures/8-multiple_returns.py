#!/usr/bin/python3

def multiple_returns(sentence):
    urefu = len(sentence)
    kwanza = sentence[0] if urefu > 0 else None
    return(urefu, kwanza)
