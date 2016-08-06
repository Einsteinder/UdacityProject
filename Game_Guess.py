# coding=utf-8
def difficulty_choose():
	#Input: the question that user choose
	#Output: the chosen question sting and answer list
	easy_string="Well, you done __1__ me and you bet I felt it. I tried to be chill, but you're so __2__ that I melted. I fell right through the cracks. Now I'm trying to get back. Before the __3__ done run out I'll be giving it my bestest. And nothing's gonna stop me but divine intervention. I reckon, it's again my turn. To win some or learn __4__. But I won't __5__ No more, no more. It cannot wait, I'm yours."
	easy_blank=["done","hot","cool","some","hesitate"]
	medium_string="""Seems like everybody's got a __1__. I wonder how they __2__ at night.When the sale comes first.And the truth comes second.Just stop for a minute and smile.Why is everybody so __3__.Acting so damn mysterious..Got shades on your eyes..And your heels so high that you can't even have a good time..Everybody look to their left.Everybody look to their __4__.Can you feel that, yeah.We're paying with love __5__.It's not about the money money money.We don't need your money money money.We just wanna make the world dance.Forget about the price tag.Ain't about the uh cha-ching cha-ching.Ain't about the yeah b-bling b-bling.Wanna make the world dance.Forget about the price tag."""
	medium_blank=["price","sleep","serious","right","tonight"]
	hard_string=""".All the times that you rain on my __1__.And all the clubs you get in using my __2__.You think you broke my heart.Ohhh girl for goodness sake.You think I'm crying.Oh my ohhh, well I ain't!.And I didn't wanna write a song.'Cause I didn't want anyone thinking I still care, I don't.But, you still hit my phone up.And baby I be moving on.And I think you should be somethin' I don't wanna hold back.Maybe you should know that.My __3__ don't like you and she like's everyone.And I never like to admit that I was wrong.And I've been so caught up in my __4__.Didn't see what's going on.But now I know.I'm better sleeping on my own.'Cause if you like the way you look that much.Ohhhh baby you should go and love __5__.And if you think that I'm still holdin' on to somethin'.You should go and love yourself."""
	hard_blank=["parade","name","mama","job","yourself"]
	x=raw_input("Please choose level of the game. You can choose easy, medium, and hard.")
	if x=="easy":
		return easy_string,easy_blank
	if x=="medium":
		return medium_string,medium_blank
	if x=="hard":
		return hard_string,hard_blank
	else:
		print "Wrong input, please choose again."
		return 1,1

def play_game():
	#Main program
	question_string,answer_list=difficulty_choose()

	while question_string==1:
		question_string,answer_list=difficulty_choose()

	game_over_times=raw_input("Please choose failure times on which you will lose(eg:1,2,3...):")
	print "The current question is:\n"+question_string
	question_string=question_string.split()
	index=1
	count=int(game_over_times)

	while count>0 and index<=5:
		replaced=[]
		blank="__"+str(index)+"__"
		for word in question_string:
			if blank in word:
				user_input=raw_input("Fill the "+str(index)+" blank:")
				if answer_list[index-1]==user_input:
					word=word.replace(blank,answer_list[index-1])
					replaced.append(word)
					if answer_list[4]==user_input:
						print "\n"
						print "Congrats! You won!\n"
						return
					index+=1
					print '\n'
					print "Correct!\n"
					
				else:
					count-=1
					replaced.append(word)
					if count==0:
						print "\n"
						print "You've failed too many straight guesses!  Game over!\n"
						return
					else:
						print "\n"
						print "You are wrong, please try again, and you just have "+str(count)+" times!\n"
			else:
				replaced.append(word)
		question_string=replaced
		question_string=" ".join(question_string)
		print "The current question is:\n"+question_string
		question_string=question_string.split()

play_game()