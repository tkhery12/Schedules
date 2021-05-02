from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
import requests
import json
taks =['asdad','adad',]
lichhoc = {}
data1 = {
    '19021289':'{"scheduleList":[{"classID":"INT2211 21","dayOfWeek":7,"group":"1","courseID":"INT2211","period":"3-4","className":"Cơ sở dữ liệu","credit":4,"auditorium":"PM 313-G2","maxAmount":29,"lecturerID":326},{"classID":"INT2208E 21","dayOfWeek":3,"group":"CL","courseID":"INT2208E","period":"3-5","className":"Công nghệ phần mềm","credit":3,"auditorium":"207-GĐ3","maxAmount":60,"lecturerID":136},{"classID":"INT2213 23","dayOfWeek":5,"group":"1","courseID":"INT2213","period":"7-9","className":"Mạng máy tính","credit":4,"auditorium":"PM 313-G2","maxAmount":30,"lecturerID":159},{"classID":"PES1040 1","dayOfWeek":6,"group":"CL","courseID":"PES1040","period":"1-2","className":"Tennis","credit":1,"auditorium":"Sân bãi ĐHNN","maxAmount":43,"lecturerID":2},{"classID":"INT1050 26","dayOfWeek":7,"group":"CL","courseID":"INT1050","period":"7-10","className":"Toán học rời rạc","credit":4,"auditorium":"207-GĐ3","maxAmount":57,"lecturerID":16},{"classID":"INT3401E 20","dayOfWeek":3,"group":"CL","courseID":"INT3401E","period":"7-9","className":"Trí tuệ nhân tạo","credit":3,"auditorium":"207-GĐ3","maxAmount":51,"lecturerID":30},{"classID":"EPN1096 24","dayOfWeek":5,"group":"CL","courseID":"EPN1096","period":"3-4","className":"Vật lý đại cương 2","credit":2,"auditorium":"205-GĐ3","maxAmount":42,"lecturerID":257},{"classID":"INT2211 21","dayOfWeek":4,"group":"CL","courseID":"INT2211","period":"7-8","className":"Cơ sở dữ liệu","credit":4,"auditorium":"206-GĐ3","maxAmount":57,"lecturerID":218},{"classID":"INT2213 23","dayOfWeek":5,"group":"CL","courseID":"INT2213","period":"1-2","className":"Mạng máy tính","credit":4,"auditorium":"205-GĐ3","maxAmount":54,"lecturerID":242}]}',
    '19021288':'{"scheduleList":[{"classID":"PES1017 30","dayOfWeek":6,"group":"CL","courseID":"PES1017","period":"3-4","className":"Bóng chuyền hơi","credit":1,"auditorium":"Sân bãi ĐHNN","maxAmount":52,"lecturerID":2},{"classID":"INT2211 20","dayOfWeek":6,"group":"1","courseID":"INT2211","period":"5-6","className":"Cơ sở dữ liệu","credit":4,"auditorium":"PM 202-G2","maxAmount":30,"lecturerID":71},{"classID":"INT2208E 20","dayOfWeek":5,"group":"CL","courseID":"INT2208E","period":"7-9","className":"Công nghệ phần mềm","credit":3,"auditorium":"208-GĐ3","maxAmount":48,"lecturerID":207},{"classID":"INT2213 25","dayOfWeek":4,"group":"1","courseID":"INT2213","period":"7-9","className":"Mạng máy tính","credit":4,"auditorium":"PM 307-G2","maxAmount":21,"lecturerID":26},{"classID":"BSA2002 21","dayOfWeek":5,"group":"CL","courseID":"BSA2002","period":"1-3","className":"Nguyên lý marketing","credit":3,"auditorium":"303-G2","maxAmount":34,"lecturerID":196},{"classID":"INT1050 20","dayOfWeek":3,"group":"CL","courseID":"INT1050","period":"7-10","className":"Toán học rời rạc","credit":4,"auditorium":"208-GĐ3","maxAmount":46,"lecturerID":165},{"classID":"EPN1096 27","dayOfWeek":4,"group":"CL","courseID":"EPN1096","period":"1-2","className":"Vật lý đại cương 2","credit":2,"auditorium":"208-GĐ3","maxAmount":58,"lecturerID":190},{"classID":"INT2211 20","dayOfWeek":4,"group":"CL","courseID":"INT2211","period":"5-6","className":"Cơ sở dữ liệu","credit":4,"auditorium":"209-GĐ3","maxAmount":55,"lecturerID":49},{"classID":"INT2213 25","dayOfWeek":6,"group":"CL","courseID":"INT2213","period":"7-8","className":"Mạng máy tính","credit":4,"auditorium":"208-GĐ3","maxAmount":51,"lecturerID":170}]}',
}
link_api = 'https://uet-schedule.herokuapp.com/student/getSchedule?studentID={}'
lecture = requests.get('https://uet-schedule.herokuapp.com/lecturer/getAll').json()['lecturerList']
all_Data = requests.get('https://uet-schedule.herokuapp.com/schedule/getAll').json()['scheduleList']
class NewID(forms.Form):
     mssv = forms.CharField(max_length=64, required=False,min_length=8,error_messages={'required': "Xin vui long go lai"},
                            widget=forms.TextInput(attrs={'placeholder': 'Mã số sinh viên'})
                            )


# Create your views here.
class IDlecture(forms.Form):
    lectureid = forms.CharField(max_length=64, required=False,min_length=1,
                            widget=forms.TextInput(attrs={'placeholder': 'Tên giảng viên'})
         )

def index(request):
    mssv = 0
    if request.method == "POST" :
        form = NewID(request.POST)
        if form.is_valid():
            mssv = form.cleaned_data["mssv"]
            if not get_check(link_api.format(mssv)):
                return render(request, "Home/index.html", {
                    "form": NewID(),
                    "message": True

                })
            data = get_data(link_api.format(mssv))
            request.session["Monday"] = []
            request.session["Tuesday"] = []
            request.session["Thursday"] = []
            request.session["Friday"] = []
            request.session["Saturday"] = []
            request.session["Wednesday"] = []
            for k in data['scheduleList']:
                if k['dayOfWeek'] == 2:
                    request.session["Monday"] += [k]
                if k['dayOfWeek'] == 3:
                    request.session["Tuesday"] += [k]
                if k['dayOfWeek'] == 4:
                    request.session["Wednesday"] += [k]
                if k['dayOfWeek'] == 5:
                    request.session["Thursday"] += [k]
                if k['dayOfWeek'] == 6:
                    request.session["Friday"] += [k]
                if k['dayOfWeek'] == 7:
                    request.session["Saturday"] += [k]
            return render(request,"Shedulestudent/index.html",{
                "Monday":request.session["Monday"],
                "Tuesday": request.session["Tuesday"],
                "Wednesday": request.session["Wednesday"],
                "Thursday": request.session["Thursday"],
                "Friday": request.session["Friday"],
                "Saturday":request.session["Saturday"],
                "task":taks,

            })
        else:
            return render(request,"Home/index.html",{
                "form":form
            })
    print(mssv)
    return render(request,"Home/index.html",{
        "form": NewID()
    })
def hello(request):
    return render(request,"Shedulestudent/index.html",{
        "Monday": request.session["Monday"],
        "Tuesday": request.session["Tuesday"],
        "Wednesday": request.session["Wednesday"],
        "Thursday": request.session["Thursday"],
        "Friday": request.session["Friday"],
        "Saturday": request.session["Saturday"],
        "task": taks,
    })
def get_check(link):
    if requests.get(link).status_code == 200:
        return True
    return False
def get_data(link):
    print(type(lecture))
    if get_check(link) == True:
        data = requests.get(link).text
        data = json.loads(data)
        for k in data['scheduleList']:
            if k['period'].split('-')[0] == "1":
                k['start_time'] = '07:00'
            if k['period'].split('-')[0] == "2":
                k['start_time'] = '08:00'
            if k['period'].split('-')[0] == "3":
                k['start_time'] = '09:00'
            if k['period'].split('-')[0] == "4":
                k['start_time'] = '10:00'
            if k['period'].split('-')[0] == "5":
                k['start_time'] = '11:00'
            if k['period'].split('-')[0] == "6":
                k['start_time'] = '12:00'
            if k['period'].split('-')[0] == "7":
                k['start_time'] = '13:00'
            if k['period'].split('-')[0] == "8":
                k['start_time'] = '14:00'
            if k['period'].split('-')[0] == "9":
                k['start_time'] = '15:00'
            if k['period'].split('-')[0] == "10":
                k['start_time'] = '16:00'
            if k['period'].split('-')[0] == "11":
                k['start_time'] = '17:00'
            if k['period'].split('-')[0] == "12":
                k['start_time'] = '18:00'
            if k['period'].split('-')[1] == "1":
                k['end_time'] = '07:50'
            if k['period'].split('-')[1] == "2":
                k['end_time'] = '08:50'
            if k['period'].split('-')[1] == "3":
                k['end_time'] = '09:50'
            if k['period'].split('-')[1] == "4":
                k['end_time'] = '10:50'
            if k['period'].split('-')[1] == "5":
                k['end_time'] = '11:50'
            if k['period'].split('-')[1] == "6":
                k['end_time'] = '12:50'
            if k['period'].split('-')[1] == "7":
                k['end_time'] = '13:50'
            if k['period'].split('-')[1] == "8":
                k['end_time'] = '14:50'
            if k['period'].split('-')[1] == "9":
                k['end_time'] = '15:50'
            if k['period'].split('-')[1] == "10":
                k['end_time'] = '16:50'
            if k['period'].split('-')[1] == "11":
                k['end_time'] = '17:50'
            if k['period'].split('-')[1] == "12":
                k['end_ time'] = '18:50'
            k['color'] = "event-{}".format(k['lecturerID'] % 3 + 1)
        return data
def get_data_db(link):
    data = json.loads(data1[link.split('=')[1]])
    for k in data['scheduleList']:
        if k['period'].split('-')[0] == "1":
            k['start_time'] = '07:00'
        if k['period'].split('-')[0] == "2":
            k['start_time'] = '08:00'
        if k['period'].split('-')[0] == "3":
            k['start_time'] = '09:00'
        if k['period'].split('-')[0] == "4":
            k['start_time'] = '10:00'
        if k['period'].split('-')[0] == "5":
            k['start_time'] = '11:00'
        if k['period'].split('-')[0] == "6":
            k['start_time'] = '12:00'
        if k['period'].split('-')[0] == "7":
            k['start_time'] = '13:00'
        if k['period'].split('-')[0] == "8":
            k['start_time'] = '14:00'
        if k['period'].split('-')[0] == "9":
            k['start_time'] = '15:00'
        if k['period'].split('-')[0] == "10":
            k['start_time'] = '16:00'
        if k['period'].split('-')[0] == "11":
            k['start_time'] = '17:00'
        if k['period'].split('-')[0] == "12":
            k['start_time'] = '18:00'
        if k['period'].split('-')[1] == "1":
            k['end_time'] = '07:50'
        if k['period'].split('-')[1] == "2":
            k['end_time'] = '08:50'
        if k['period'].split('-')[1] == "3":
            k['end_time'] = '09:50'
        if k['period'].split('-')[1] == "4":
            k['end_time'] = '10:50'
        if k['period'].split('-')[1] == "5":
            k['end_time'] = '11:50'
        if k['period'].split('-')[1] == "6":
            k['end_time'] = '12:50'
        if k['period'].split('-')[1] == "7":
            k['end_time'] = '13:50'
        if k['period'].split('-')[1] == "8":
            k['end_time'] = '14:50'
        if k['period'].split('-')[1] == "9":
            k['end_time'] = '15:50'
        if k['period'].split('-')[1] == "10":
            k['end_time'] = '16:50'
        if k['period'].split('-')[1] == "11":
            k['end_time'] = '17:50'
        if k['period'].split('-')[1] == "12":
            k['end_ time'] = '18:50'
        k['color'] = "event-{}".format(k['lecturerID'] % 3 + 1)
    return data


