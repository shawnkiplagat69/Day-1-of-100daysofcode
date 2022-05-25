# Day-1-of-100daysofcode
Came up with a Mad Libs generator project
Mad Libs™ are the ultimate car-trip game, a feverish quest for the funniest words and most inadvertent puns. In addition to being a useful tool for teaching the parts of speech, playing Mad Libs™ can be fun for all ages. By creating short stories with key words removed, Mad Libs™ allows you to create your own wacky version, often leading to hilarity run amok.

**The logic behind the code for this MadLib project**
Multiple string variables are declared in order to store user details.

Once all the blanks are filled by the player, the control is then passed to the printing of the player’s story to read!

Prior to the declaration in the code, a looping variable called loop, which is initialized to 1, is declared.

A while loop is used with loop as its looping variable under which all the input() and print() statements are written.

The condition for the number of iterations under while refers to the number of times the player will be able to play around and create stories.

This means that, initially, loop=1 will be incremented each time a story is printed. While this loop value stays within the condition of the while loop, the code under it will be executed that many times. 

However, you can change this static loop value to make it dynamic and enhance the game’s code. This loop’s value can be taken from the player themselves through an input() statement that will hold the number of times they want to play the game.
