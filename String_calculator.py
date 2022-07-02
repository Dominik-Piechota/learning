print('''Hello! This is simple calculator based on questions. To get a result simply type the calculation
      that need to be made, for example: "What is 124 minus 28 multiplied by 5?". Operations, that will give you proper result are:
      1. plus
      2. minus
      3. multiplied by
      4. divided by''')
import re
def answer(question):
    '''This function provide simply calculation based on the string that was given as input, for example:
    "What's 2 plus 4?" - the result will be of course 6.
    :param question: str - question with calculation.
    :return: int - the result of calculation.
    '''
    result = 0
    symbols = ['plus', 'minus', 'multiplied', 'divided']
    list_split = question.split()
    counter = 0
    for number, i in enumerate(list_split):
        if i == 'plus':
            if counter > 0:
                pattern = r'([-]*\d+\s)plus(\w*\s[-]*\d+)'
                a = re.findall(pattern, question)
                a = list(a[0])
                a[0] = result
                result = (float(a[0]) + float(a[1]))
                
            if counter == 0:
                pattern = r'([-]*\d+\s)plus(\w*\s[-]*\d+)'
                a = re.findall(pattern, question)
                a = list(a[0])
                result = (float(a[0]) + float(a[1]))
                
            counter += 1
            
        if i == 'minus':
            pattern = r'([-]*\d+\s)minus(\w*\s[-]*\d+)'
            a = re.findall(pattern, question)
            if counter == 0:
                a = list(a[0])
                result = (float(a[0]) - float(a[1]))
            if counter > 0:
                a = list(a[0])
                a[0] = result
                result = (float(a[0]) - float(a[1]))
            counter += 1
            
        if i == 'multiplied':
            pattern = r'([-]*\d+\s)multiplied by(\w*\s[-]*\d+)'
            a = re.findall(pattern, question)
            if counter == 0:
                a = list(a[0])
                result = (float(a[0]) * float(a[1]))
            if counter > 0:
                a = list(a[0])
                a[0] = result
                result = (float(a[0]) * float(a[1]))
            counter += 1
            
        if i == 'divided':
            pattern = r'([-]*\d+)\s*divided by(\w*\s[-]*\d+)'
            a = re.findall(pattern, question)
            if counter == 0:
                a = list(a[0])
                result = (float(a[0]) / float(a[1]))
            if counter > 0:
                a = list(a[0])
                a[0] = result
                result = (float(a[0]) / float(a[1]))
            counter += 1
            
        if number > 0:
            question =  ' '.join(list_split[(number -1):])
    return result
print(f'The result is : {answer(input("Provide a question with calculation you want to do:"))}')
