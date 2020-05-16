#!/usr/bin/env python3
import sys
import os
import re

class Tag:
    def __init__(self):
        self.type = None
        self.data = None
        self.attributes = {}
        self.children = []







ROOT = Tag()
ROOT.type = 'html'




def tokenizeRawHTML(rawHTML):
    raw = str(rawHTML)
    i = 0
    inBracketTag = True
    tokenList = []
    currentTokenChars = []
    while i < len(raw):
        if raw[i] == "\n":
            # turn newlines into spaces to simplify
            currentTokenChars.append(' ')
        elif inBracketTag:
            # just need to check for > if inside bracket tag
            if raw[i] == '>':
                currentTokenChars.append('>')
                tokenList.append(''.join(currentTokenChars))
                currentTokenChars = []
                inBracketTag = False
        else:
            # if <, new bracket tag. If not, we are in data part between bracket tags.
            if raw[i] == '<':
                inBracketTag = True
                currentToken


            
            



    return 

def isClosingTag(token):
    if str(token)[1] = '/':
        return True
    else:
        return False

#returns tag type as str (like "p", "div", "h1", etc.)
def getTagType(token):
    matchTag = re.search(r'<([A-Za-z\-]*)[\s|>]', token)
    return matchTag.group()

def buildTree(tokenList):
    # starts at 1 to skip <!DOCTYPE html>
    i = 1
    historyStack = []
    currentTag = ROOT
    while i < len(tokenList):
        if isClosingTag(currentTag):
            currentTag = historyStack[-1]
        elif isData():
            currentTag.data = tokenList[i]
        else:
            # tokenlist[i] is a new tag. Get the type and set current tag to the new tag.
            historyStack.append(currentTag)
            currentTag.children.append(Tag())
            currentTag = currentTag.children[-1]
            currentTag.type = getTagType(tokenList[i])
        i += 1
        





with open('index.html', 'r') as f:
    tokenizeRawHTML(f.read())



    



