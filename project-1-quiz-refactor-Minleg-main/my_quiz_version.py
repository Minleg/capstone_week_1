"""
Project 1: User is given quiz on either art or space topic and they are asked the questions on the topic selected. There answers
are recorded and checked with the correct answer stored in the dictionary. The user can answer in anycase and should get the point
independent of the case the user answered in.

The questions and answers for a topic are stored in a dictionary for that topic as a key-value pair.
We should be able to add more questions and answer in any of the topics in the dictionary defined and the program should 
execute correctly
"""
def main():
    topic = chooseGenre() # user is prompted to choose their topic of interest
    # dictionary to store questions and answers as key value pairs
    art_questions_answer = {'Who painted the Mona Lisa?': 'Leonardo Da Vinci', 
                            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
                            'Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?': 'Chicago',
                            'Which kid\'s TV characters are named after Renaissance artists?': 'Teenage Mutant Ninja Turtles',
                            'The graphite in an artist\'s pencil is made of what chemical element?': 'Carbon'}

    space_questions_answer = {'Which planet is closest to the sun?': 'Mercury',
                              'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
                              'How many moons does Mars have?': '2',
                              'What was the first human-made object to leave the solar system?': 'Voyager 1',
                              'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?': 'Meteor'}
    
    sports_questions_answer = {'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': 'Simone Biles',
                               'Which country has won the soccer world cup the most times?': 'Brasil',
                               'What does MLB stand for?' : 'Major League Baseball'}
    
    number_of_art_questions = len(art_questions_answer) # gets the number of questions for arts topic
    number_of_space_questions = len(space_questions_answer) # gets the number of questions for space topic
    number_of_sports_questions = len(sports_questions_answer)

    if topic == 'art': 
        total = questions(art_questions_answer) # user is asked the questions on the topic and their result is stored in total variable
        output(topic,total,number_of_art_questions) # output is printed
    elif topic == 'space': 
        total = questions(space_questions_answer) # questions asked on space topic and result is obtained in total
        output(topic,total,number_of_space_questions) # their quiz result is printed
    else :
        total = questions(sports_questions_answer)
        output(topic,total,number_of_sports_questions)

def chooseGenre(): # method for user to choose the topic for quiz, either art or space
    genre = input("Would you like art, space, or sport questions ? : ")
    if(genre.lower() == 'art'):
        return 'art'
    elif(genre.lower() == 'space'):
        return 'space'
    elif(genre.lower() == 'sport'):
        return 'sport'
    else:
        return chooseGenre() # if user enters an invalid options, the questions is asked again until user selects a valid option

def questions(question_answer_dictionary): # method to ask user the questions related to the topic and return their quiz score
    total = 0  # to store the number of questions the user got correct
    for key,value in question_answer_dictionary.items(): # loops the questions dictionary
        user_answer = input(key + ': ')
        if user_answer.lower() == value.lower(): # user can answer in any case and the answer would be correct irrespective of the case
            total = total + 1
        else:
            print(f'Sorry, the correct answer is {value}') # prints message for incorrect answers
    return total

def output(topic,total,number_of_questions): # outputs the total
    print(f'Your total score on {topic} questions is {total} out of {number_of_questions}')

main()