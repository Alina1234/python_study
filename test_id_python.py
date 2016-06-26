import json

with open("idjsonfile.json") as data_file:
	data = json.load(data_file)
	

# define all sections and them content in 'quiz'
def all_sections(data):
	for keys in data:
		sections = data.pop(keys)
		return sections

# get all sections		
sections = all_sections(data)

def ask_question(sections):
	result = 0
	# search in general section
	for ques_answ in sections.values():
		# search in subsection
		for ques_answ_optin in ques_answ.values():
			print
			print ques_answ_optin.get('question')
			print 
			# search in option section
			for option in ques_answ_optin.get('options'):
				print "%s." % option.get('id'),
				print option.get('option')
			# ask user answer
			user_ans = user_answer()
			correct_answer = ques_answ_optin.get('answer')
			question_result = get_result(user_ans, correct_answer)
			result = result + question_result
	print
	print ("Your result is: %s" % result)
	return True
		
def user_answer():
	print
	answer = raw_input("Please, enter your answer: ")
	# answer validation:
	while (answer != '1' and answer != '2' and answer != '3' and answer != '4'):
		answer = raw_input("Please, enter number from 1 to 4: ")
	else:
		return int(answer)
	
def get_result(user_ans, correct_answer):
	if user_ans == correct_answer:
		res = 1
	else:
		res = 0
	return res
	
	
ask_question(sections)