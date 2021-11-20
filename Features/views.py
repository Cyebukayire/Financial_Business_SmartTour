from django.shortcuts import render
import joblib

# Create your views here.
def tourist_attraction(req):
    return render(req, 'survey1.html')

def result(req):
    rf_model = joblib.load("rf_model.sav")

    #creating a 
    data_ls = []
    data_ls.append(req.GET['Gender'])
    data_ls.append(req.GET['Age_group'])
    data_ls.append(req.GET['City'])
    data_ls.append(req.GET['Travel_With'])
    data_ls.append(req.GET['Total_female'])
    data_ls.append(req.GET['Total_male'])
    data_ls.append(req.GET['Purpose_of_Visit'])
    data_ls.append(req.GET['Total_Days'])

    #Get User's Email
    email = req.GET['Email']
    

    Age_group = {'18-25': 0, '26-35': 1, '36-45': 2, 'less than 18': 3}
    City_Visited = {'Abuja': 0,'Bauchi': 1,'Bayelsa': 2,'Cross River': 3,
                                'Delta': 4,'Edo': 5,'Ekiti': 6,'Enugu': 7,'Gombe': 8,
                                'Kaduna': 9,'Kano': 10,'Lagos': 11,'Niger': 12,'Ogun': 13,
                                'Ondo': 14,'Osun': 15,'Oyo': 16,'Rivers': 17,'Sokoto': 18,
                                'Uyo': 19,'Yola': 20}
    Gender= {'Female': 0, 'Male': 1}
    Persons_visited_with = {'Alone': 0,'Friends': 1,'Relatives': 2,'Spouse': 3}
    Purpose_of_Visit={'Business,Meeting and conferences': 0,'Class Trip': 1,
                                    'Engagement party': 2, 'Family event': 3,'Honeymoon': 4,
                                    'Leisure and Holidays': 5,'Visiting friends and relatives': 6}
    
    print(data_ls)

    prediction = rf_model.predict([data_ls])

    pred_error = 36795 + float(prediction[0])

    return render(req, 'result.html', {'pred':float(prediction[0]), "pred_error":pred_error})
