from sys import argv

script, user_name = argv
prompt = '> '

print("HI %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")

print("Do you like me %s? " % user_name)
likes = input(prompt)

print("Where do you live %s" % user_name)
lives = input(prompt)

print("What kind of computer do tou have?")
computer = input(prompt)

print("""
Alright so you said %r about liking me.
And you live in %r. Not sure where that is, sounds shit anyway.
You have a %r computer, faggot."""
      % (likes, lives, computer))
