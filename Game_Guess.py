# coding=utf-8
import os
import re
easy_string="""
Well, you done __1__ me and you bet I felt it. 
I tried to be chill, but you're so __2__ that I melted. 
I fell right through the cracks. Now I'm trying to get back. 
Before the __3__ done run out I'll be giving it my bestest. 
And nothing's gonna stop me but divine intervention. 
I reckon, it's again my turn. To win some or learn __4__. 
But I won't __5__ No more, no more. It cannot wait, I'm yours.
"""
easy_blank=["done","hot","cool","some","hesitate"]
medium_string="""
Seems like everybody's got a __1__. 
I wonder how they __2__ at night.
When the sale comes first.
And the truth comes second.
Just stop for a minute and smile.
Why is everybody so __3__.
Acting so damn mysterious.
Got shades on your eyes.
And your heels so high that you can't even have a good time.
Everybody look to their left.Everybody look to their __4__.
Can you feel that, yeah.We're paying with love __5__.
It's not about the money money money.
We don't need your money money money.
We just wanna make the world dance.
Forget about the price tag.
Ain't about the uh cha-ching cha-ching.
Ain't about the yeah b-bling b-bling.
Wanna make the world dance.
Forget about the price tag.
"""
medium_blank=["price","sleep","serious","right","tonight"]
hard_string="""
All the times that you rain on my __1__.
And all the clubs you get in using my __2__.
You think you broke my heart Ohhh girl for goodness sake.
You think I'm crying.Oh my ohhh, well I ain't!.
And I didn't wanna write a song.
Cause I didn't want anyone thinking I still care, I don't.
But, you still hit my phone up.
And baby I be moving on.
And I think you should be somethin' I don't wanna hold back.
Maybe you should know that.
My __3__ don't like you and she like's everyone.
And I never like to admit that I was wrong.
And I've been so caught up in my __4__.
Didn't see what's going on.
But now I know I'm better sleeping on my own.
Cause if you like the way you look that much.
Ohhhh baby you should go and love __5__.
And if you think that I'm still holdin' on to somethin'.
You should go and love yourself.
"""
hard_blank=["parade","name","mama","job","yourself"]

def difficulty_choose():
	#Input: the question that user choose
	#Output: the chosen question sting and answer list
	
	chosen_level=raw_input("Please choose level of the game. You can choose easy, medium, and hard.")
	if chosen_level=="easy":
		return easy_string,easy_blank
	elif chosen_level=="medium":
		return medium_string,medium_blank
	elif chosen_level=="hard":
		return hard_string,hard_blank
	else:
		print "Wrong input, please choose again."
		return difficulty_choose()

def failure_time_choose():
	#with this function we will ask the number of times that the user want to play
	#output:game_over_time "number of lives"
	game_over_times=raw_input("Please choose failure times on which you will lose(eg:1,2,3...): ")
	return game_over_times
	

def show_and_split_question(question_string_local):
	#with this function we will to show the user the questions and split them according line
	#output:print the easy, medium or hard string
	print "The current question is:\n"+question_string_local
	question_string_local=re.split("\n",question_string_local)
	return question_string_local

def process_question(question_string_local):
	word_lists_local=[]
	#this function will put the splited string in a list
	#output: return the list that contain the splited question.
	for words in question_string_local:
		word_lists_local.append(words.split())
	return word_lists_local

def won_condition(answer_local,user_input_local):
	#this function estimate whether user won the game
	#output:print the words of congratulation
	if answer_local==user_input_local:
		print "\nCongrats! You won!\n"
		os._exit(1) 

def fail_condition(count_local):
	#this function estimate wheter user fail the game or fail to gusses
	#output: print the result of guessing
	if count_local==0:
		print "\nYou've failed too many straight guesses!  Game over!\n"
		os._exit(1) 
	else:
		print "\nYou are wrong, please try again, and you just have "+str(count_local)+" times!\n"

def substitute_blank(answer_s,blank_s,index_s,word_s,count_s,replaced_s):
	# substitute correct answers for blanks
	# output:if user input the correct answer substitute blanks and tell user it's right
	# return some intermediate variebles
	user_input=raw_input("Fill the "+str(index_s)+" blank:")
	if answer_s[index_s-1]==user_input:
		word_s=word_s.replace(blank_s,answer_s[index_s-1])
		replaced_s.append(word_s)
		won_condition(answer_s[4],user_input)
		index_s+=1
		print "\nCorrect!\n"
		return blank_s,word_s,index_s,count_s,replaced_s
		
	else:
		count_s-=1
		replaced_s.append(word_s)
		fail_condition(count_s)
		return blank_s,word_s,index_s,count_s,replaced_s


def play_game(question_string_local,answer_local,count_local,index_local,word_lists_local):
	#setup function, main logic of the game
	#output: the current question with input from user
	while count_local>0 and index_local<=5:
		word_store_list_1,word_store_list2,word_list_display=[],[],[]
		blank="__"+str(index_local)+"__"
		for word_list in word_lists_local:
			replaced=[]
			for word in word_list:
				if blank in word:
					blank,word,index_local,count_local,replaced=substitute_blank(answer_local,blank,index_local,word,count_local,replaced)
				else:
					replaced.append(word)
			word_store_list2.append(replaced)#[["aa","bb","cc","dd"]["ee","ff","gg"]]
			word_lists_local=word_store_list2
			word_list_display=" ".join(replaced)#"aa bb cc dd"
			word_store_list_1.append(word_list_display)#["aa bb cc dd","ee ff gg"]
		word_store_list_1="\n".join(word_store_list_1)
		print "The current question is:\n"+word_store_list_1




def main():
	# main function calls setup function and plays game
	question_string,answer_list=difficulty_choose()
	game_over_times=failure_time_choose()
	question_string=show_and_split_question(question_string)
	word_lists=process_question(question_string)
	count=int(game_over_times)
	index=1


	play_game(question_string,answer_list,count,index,word_lists)


main()
# Call main to kick things off
