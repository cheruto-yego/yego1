name=str (input('please enter your name;'))
if name.isalpha():
    print(name)
    print('How are you',name)
    print('Good bye dear ', name)
    quit()
else:
    print('hello friend')
    age=int(input('how old are you please'))
if age<18:
    print('you are below age of working')
elif age>18 and age<25:
    print('your have the right age to look for a job')
elif age>30 and age<60:
    print('you should think about having a family')
elif age<90 and age>=60:
    print('you should retire')
else:
    print('your age',age)
    print('goodbye',name)
    print('you are an alien in nature')