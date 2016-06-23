import json

with open("jsonfile.json") as data_file:
	data = json.load(data_file)

# define sections in dict and calculate results
def get_quiz_results(data):
	result = 0
	
	# Get value of 'quiz' key:
	new_data = data.pop('quiz')
	
	for keys in new_data:
		# Get key in string format for each section (math, sport, test, etc.)
		section_key = str(keys)
		
		# Get value for each section
		section_value = new_data.get(section_key)
		
		# get all question and answers; define user gives correct or not answer for section 
		user_true = get_quiz_qa(section_value)
		
		#if user gives correct answer, increase result:
		result = result + user_true
		
	return result

# define questions and answers for section and print questions
def get_quiz_qa(section_value):

	# for number of question:
	i = 0
	
	for keys in section_value:
	
		# get keys for each sub section
		qa_key = str(keys)
		
		# get value for each sub section 
		qa_value = section_value.get(qa_key)
		
		# get number of question
		i += 1
		print ("Question %s" % i)
		print
		
		# get text of question
		print qa_value.get("question")
		print
		
		# return key for all answers
		answers = qa_value.get("options")
		
		# return key for correct answer
		text_of_answer = qa_value.get("answer")
		
		# getting correct answer
		correct_answer = get_quiz_answers(answers, text_of_answer)
		print
		"""
		# getting answer from user
		user_answer = raw_input("Please, enter your answer: ")
		print
		"""
		#getting answer from user
		user_answer = input_user_answer()
		
		# if user answer is correct, user gets one point
		if int(user_answer) == correct_answer:
			user_true = 1
		else:
			user_true = 0
		
	return user_true

# find and print answers, define correct answer
def get_quiz_answers(answers, text_of_answer):
	# for number of correct answer
	y = 0
	
	for keys in answers:
		y += 1
		
		# printing number and text of answer
		print ("   %s. " % y),
		print keys
		
		# calculate number of correct answer 
		if keys == text_of_answer:
			correct_answer = y
	return correct_answer
	
# define user answer and validate it
def input_user_answer():
	user_answer = raw_input("Please, enter your answer: ")
	print
	while (user_answer != '1' and user_answer != '2' and user_answer != '3' and user_answer != '4'):
		print 
		user_answer = raw_input("Please, enter number from 1 to 4: ")
	else:
		return user_answer

# define printing results	
def print_quiz_result():
	result = get_quiz_results(data)
	print
	print
	print ("Your result is: %s" % result)
	return True


print_quiz_result()