import os.path
import sys
import PP3_4

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP3_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_4.input = mock_input

	PP3_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In #1: In #2: In #3: In #4: In #5: 6\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP3_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_4.input = mock_input

	PP3_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In #1: In #2: In #3: In #4: In #5: In #6: In #7: In #8: In #9: In #10: 4\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP3_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['700']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_4.input = mock_input

	PP3_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In #1: In #2: In #3: 1\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP3_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_4.input = mock_input

	PP3_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In #1: In #2: In #3: In #4: In #5: In #6: 6\n"

def test_q1_5(capsys):

	try:
		exists = os.path.exists("PP3_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['200']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_4.input = mock_input

	PP3_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In #1: In #2: In #3: In #4: In #5: In #6: In #7: 0\n"

