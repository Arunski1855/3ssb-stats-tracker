"""Motivational quotes from famous orators."""

import random

QUOTES = [
    ("The best way to predict the future is to create it.", "Abraham Lincoln"),
    ("In the middle of difficulty lies opportunity.", "Albert Einstein"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("I have a dream that one day this nation will rise up.", "Martin Luther King Jr."),
    ("We shall fight on the beaches, we shall never surrender.", "Winston Churchill"),
    ("Ask not what your country can do for you — ask what you can do for your country.", "John F. Kennedy"),
    ("The greatest glory in living lies not in never falling, but in rising every time we fall.", "Nelson Mandela"),
    ("You must be the change you wish to see in the world.", "Mahatma Gandhi"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Darkness cannot drive out darkness; only light can do that.", "Martin Luther King Jr."),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt"),
    ("Injustice anywhere is a threat to justice everywhere.", "Martin Luther King Jr."),
    ("We are not makers of history. We are made by history.", "Martin Luther King Jr."),
    ("To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Ralph Waldo Emerson"),
    ("Speak softly and carry a big stick.", "Theodore Roosevelt"),
    ("Education is the most powerful weapon which you can use to change the world.", "Nelson Mandela"),
    ("Live as if you were to die tomorrow. Learn as if you were to live forever.", "Mahatma Gandhi"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
]


def get_random_quote():
    """Return a random (quote, author) tuple."""
    return random.choice(QUOTES)
