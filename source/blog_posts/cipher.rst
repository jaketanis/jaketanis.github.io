.. _cipher:

========================
The “unbreakable” cipher
========================

**February 8th, 2026**

Lewis Carroll is often known as the author of the childrens story
“Through the Looking Glass”, but Carroll was also a prolific
mathematician. Growing up, he was always creating puzzles and logic
games, some of which are represented in the stories he wrote. In 1868,
Carroll published a study about an invention of his called `“The
Alphabet Cipher” <https://en.wikipedia.org/wiki/The_Alphabet_Cipher>`__.
This type of cipher is known as a Vignére cipher, which Caroll described
as “unbreakable”.

The Vignére cipher encrypts a message based on a key. Each letter of the
message changes based on the position of the letters within the key. The
letters in the message shift based on the key's corresponding letters'
position in the alphabet. For example:

   ``message`` is the message to encrypt and ``key`` is the key. Since
   ``k`` is the 10th letter in the alphabet (if ``a`` is considered as
   0), and the letter ``m`` is the 12th letter, the first letter of the
   encrypted message is the 22nd letter, which is ``w``. The fully
   encrypted message is ``wiqceeo``.

What was once seen as unbreakable to Carroll is actually quite doable
for us with Python. I was able to create a script that two people could
use to encrypt and decrypt messages with the Vignére cipher in a
terminal. This was honestly an exercise to practice the lessons taught
in the first project in `Scientific Computing with
Python <https://www.freecodecamp.org/learn/scientific-computing-with-python/#learn-list-comprehension-by-building-a-case-converter-program>`__
by freeCodeCamp. After completing that project, I wanted to test what I
learned; so, I created my own script based on what I learned in the
project tutorial.

It took a lot longer than I thought, but the experience was valuable.
I'm going to walk through how I created this script, what roadblocks I
ran into, and what I learned in the process.

Creating the Vignére cipher in Python
=====================================

When I created this script, I intended to make it so that it could be
easily used. I imagined two kids sending secret messages to eachother
through text or email, using their own computer to run this script that
decrypts and encrypts the messages. This would require some user inputs,
which was different from the project tutorial I went through. But I knew
that the hardest part of the script would be to get the logic correct.
So, I spent most of my time figuring that out.

To create the logic, I first defined what I needed to create the logic
with. This included the alphabet, a key, and a message. The function
would receive the message and the key, and then determine the new
message based on that information. This looked something like this:

.. code:: python

       new_message = ''
       alphabet = 'abcdefghijklmnopqrstuvwxzy'
       message = 'Hello!'
       key = fanta

       def converter(message, key):

This cipher does not take into account for capital letters, so I needed
to convert the message string into all lower case. This is done through
the ``.lower()`` function.

My next objective was to find the position of the letter in the
alphabet. I also wanted to track the position of the letter in the
message itself. Eventually, I realized I didn't need to track the
position of the letter in the message to accomplish my goals, so I ended
up removing this later.

To track the position of the letter in the alphabet, I set up a ``for``
loop. This also served as the bedrock for further logic.

The remaining tasks for me to do in the loop were finding the letters of
the key and their position in the alphabet.

After that, I needed to find the position of the letters of the
encrypted message within the alphabet. To do this, I addeded together
the positions of the message letters in the alphabet with the positions
of the key letters in the alphabet. The final version looked likes this:

.. code:: python

       def converter(message, key, direction=1):

           lower_message = message.lower()
           key_index = 0
           final_message = ''

           for char in lower_message:
               if char.isalpha(): # used to convert
                   alpha_index = alphabet.find(char)
                   key_char = key[key_index % len(key)] # modulo of key length is used to account for wrap-around
                   key_index += 1

                   key_alpha_index = alphabet.index(key_char)
                   new_index = (alpha_index + key_alpha_index*direction) % len(alphabet) # modulo of alphabet length is to account for wrap-around

                   new_char = alphabet[new_index]
                   final_message += new_char

There are a couple things that were hard for me to understand in the
above code. The first thing was the use of the modulo operator (``%``).
This operator returns the remainder of the division of two numbers. I
learned in freeCodeCamp that it was used to account for wrap-around of a
string when trying to find a character or an index in that string. What
I had a hard time understanding was that when a number is divided by a
number larger than itself, the remainder is 0. I guess I need brush up
on math. But, this is useful to know when iterating through a string
that isn't the string used by the for loop (i.e. ``lower_message`` in
``for char in lower_message``).

The other hard thing was understanding how to do what I just alluded to:
work with strings that are not the string used in the for loop. We
needed to work with the ``key`` string to find the letter in the same
position as the message, but if the key and message had different
character counts, we needed to wrap the key since we were iterating
through each letter of the message in the for loop. I was trying to
figure out the index of the key based on the for loop iteration, but I
couldn't figure that out. So I ended up seeing how I did it in the
freeCodeCamp project, which ended being a counter.

After I figured out that logic, what was left was to combine the
positions of the message character and the key character in the alphabet
together, and then we have our encrypted letter. After that, we add that
letter to a string. We keep doing that until all of the letters in the
message are encrypted.

The final code looks like this:

.. code:: python

       # global variables
       alphabet = 'abcdefghijklmnopqrstuvwxyz'

       final_message = ''

       # inputs
       choice = input("Encrypt or decrypt? \n")

       key = input("\nWhat is the key? \n")

       message = input("\nMessage: \n")

       # functions
       def converter(message, key, direction=1):

           lower_message = message.lower()
           key_index = 0
           final_message = ''

           for char in lower_message:
               if char.isalpha(): # used to convert
                   alpha_index = alphabet.find(char)
                   key_char = key[key_index % len(key)] # modulo of key length is used to account for wrap-around
                   key_index += 1

                   key_alpha_index = alphabet.index(key_char)
                   new_index = (alpha_index + key_alpha_index*direction) % len(alphabet) # modulo of alphabet length is to account for wrap-around

                   new_char = alphabet[new_index]
                   final_message += new_char
               else: # passes on symbols
                   final_message += char
           return print(final_message)

       def encrypt(message, key):
           print("Encrypted message: \n")
           return converter(message,key)

       def decrypt(message, key):
           print ("Decrypted message: \n")
           return converter(message, key, -1)

       # outputs
       if choice == "encrypt":
           encrypt(message,key)

       elif choice == "decrypt":
           decrypt(message, key)

Other things that I included were a direction parameter for whether we
wanted to decrypt messages in the ``converter`` function. In ``encrypt``
or ``decrypt``, they determine which direction the converter function
goes when figuring out the final position of the new letter. Encryption
or decryption is determined by user inputs, as well as the key and
message.

The terminal output looks like this:

::

       Encrypt or decrypt? 
       encrypt

       What is the key? 
       dog

       Message: 
       do I want a dog?
       Encrypted message: 

       gc o zotw o jru?

Final remarks
=============

There are other things in this script that I could keep talking about,
but I mentioned my main takeaways. Overall, I really enjoyed doing this
and was pretty challenged by it. I didn’t think I would be. I’m glad I
was surprised - it’s the reason I am doing this. I want to grow, learn,
and stretch my capabilities when it comes to programming. Even if that
means doing things I assume are easy, because I may very well be
assuming I know something when I actually don’t.
