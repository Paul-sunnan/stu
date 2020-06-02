from django.shortcuts import render,redirect
from django.http import HttpResponse
from stu.models import *
# Create your views here.
def index(request):
	# PWD = request.get_signed_cookie('pwd',salt='eeee')
	# print(PWD)
	UNM = request.session.get('unm')
	PWD = request.session.get('pwd')
	if not PWD:
		return render(request,'index.html',{'errorinfo':'请各位老师学生先登陆界面后进行操作。'})
	else:
		return render(request,'index.html',{'user': UNM,'rightinfo':'欢迎登陆！'})

def classall(request):
	class_all = classes.objects.all()

	print(class_all)
	return render(request,('class.html',),{
		'classInfo':class_all,
		})
	

def classinfo(request):
	class_all = classes.objects.all()

	print(class_all)
	return render(request,('class.html',),{
		'classInfo':class_all,
		})

def addInfo(request):

	StudentName = request.POST.get('student_name')
	ClassName = request.POST.get('class_name')
	TeacherName = request.POST.get('teacher_name')

	print(TeacherName)
	print("-"*50)

	if  TeacherName == "老师姓名" or TeacherName==None:
		print('老师信息没有填写')
	else:
		teachers.objects.create(name=TeacherName)

	if  ClassName == "班级名称" or ClassName==None:
		print('班级信息没有填写')
	else:	
		classes.objects.create(name=ClassName)
		if StudentName != "学生姓名" and StudentName != None:
			for temp in classes.objects.filter(name__contains=ClassName):
				students.objects.create(name=StudentName,classID=temp)
		else:
			print('无法添加学生信息')
	#查询班级信息并提取
	class_all = classes.objects.all()
	teacher_all = teachers.objects.all()
	student_all = students.objects.all()
	teacher_class_all = teacher_class.objects.all()
	print(class_all)
	return render(request,('add_info.html',),{
		'stu_Info':student_all,
		'teacher_class_all':teacher_class_all,
		'teacherInfo':teacher_all,
		'classInfo':class_all,
		}
		)

def addInfo_window(request):
	ClassName = request.POST.get('class_name')
	if ClassName:
		classes.objects.create(name=ClassName)
		return HttpResponse(ClassName)
	else:
		return HttpResponse('faild！！！')

def del_class(request):
	del_id=request.GET.get('id')
	print(del_id)
	print('-'*50)
	classes.objects.filter(cid=del_id).delete()
	return redirect('/')

def edit_class(request):
	edit_id = str(request.GET.get('cid'))
	edit_name = request.GET.get('class_name')
	print(edit_id)
	print('-'*50)
	classes.objects.filter(cid=int(edit_id[3:])).update(name=edit_name)
	return HttpResponse('okkkkkk')

def student(request):
	stu_all = students.objects.all()
	class_all = classes.objects.all()
	teacher_all = teachers.objects.all()
	if request.method == 'POST':
		stu_name = request.POST.get('stu_name')
		class_id = request.POST.get('class_id')
		class_ID = classes.objects.get(id=class_id)
		print('-'*30,class_ID.name)
		students.objects.create(name=stu_name,classID=class_ID)
	return render(request,'student.html',{
		'teacherInfo':teacher_all,
		'classInfo':class_all,
		'studentInfo':stu_all
		})

def teacher(request):
	teacherInfo = teachers.objects.all().order_by('id')
	return render(request,'teacher.html',{
		'teacherInfo':teacherInfo,
		})

from django.contrib.auth import authenticate
def login(request):
	if request.method == 'GET':
		pass
		return render(request,'login.html')
	else:
		username = request.POST.get('username')
		passwd = request.POST.get('passwd')
		user = authenticate(username=username, password=passwd)
		errorinfo = "用户名或密码错误"
		if user is not None:
			# obj = redirect("/")
			# obj.set_signed_cookie('pwd','ffff',salt='eeee')
			request.session['pwd']='1111'
			request.session['unm']='a1'
			return redirect('/')
		else:	
			return render(request,'login.html',{'errorinfo':errorinfo,})

from django.contrib.auth.models import User
def signin(request):
	if request.method == 'GET':
		return render(request,'signin.html')
	else:
		username = request.POST.get('username')
		realname = request.POST.get('realname')
		passwd = request.POST.get('passwd')
		print('输出的值为%s ,%s ,%s ,' %(type(username),type(realname),type(passwd)))

		user = User.objects.create_user(username,realname,passwd)
		if  username == '' or realname == '' or passwd == '':
			return render(request,'signin.html',{'error':'输入错误',})

		else:
			#user_info.objects.create(alias_name=username,real_name=realname,pass_word=passwd)
			
			return redirect('/login')

def tea_cla(request):
	if request.method == 'POST':
		classname = request.POST.get('classname')
		teachername = request.POST.get('teachername')

		cla = classes.objects.get(name=classname)
		tea = teachers.objects.get(name=teachername)
		teacher_class.objects.create(classID=cla,teacherID=tea)

	teacher_class_all = teacher_class.objects.all()
	class_all = classes.objects.all()
	teacher_all = teachers.objects.all()
	return render(request,'tea_cla.html',{
		'teacherInfo':teacher_all,
		'classInfo':class_all,
		'teacher_class_all':teacher_class_all,
		})		

# def page404(request,exception):
# 	render(request,'404.html')