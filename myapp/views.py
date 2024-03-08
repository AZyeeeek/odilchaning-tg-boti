from django.shortcuts import render
from .models import Test, Submission

def submit_test(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        test_id = request.POST.get('test_id')
        answers = request.POST.get('answers')
        
        test = Test.objects.get(test_id=test_id)
        correct_answers = test.correct_answer  
        user_answers = answers          
        incorrect_answers = ""
        for idx in range(0,len(correct_answers)):
            if user_answers[idx] != correct_answers[idx]:
                incorrect_answers+= str(idx+1)
                incorrect_answers+= ","
        # Serialize the dictionary to a string
        incorrect_answers_str = incorrect_answers
        
        submission = Submission.objects.create(name=name, test_id=test_id, answers=answers, user_answers=answers, incorrect_answers=incorrect_answers_str)
        
        return render(request, 'result.html', {'submission': submission})
    
    tests = Test.objects.all()
    return render(request, 'submit_test.html', {'tests': tests})
