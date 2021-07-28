import tkinter as tk
import requests
import datetime
from PIL import Image, ImageTk

def getcovidData():
    api="https://disease.sh/v3/covid-19/all"
    json_data =requests.get(api).json()

    total_cases = str(json_data['cases'])
    todal_deaths=str(json_data['deaths'])
    today_cases=str(json_data['todayCases'])
    today_deaths=str(json_data['todayDeaths'])
    today_recovered=str(json_data['todayRecovered'])
    updated_at=json_data['updated']
    date=datetime.datetime.fromtimestamp(updated_at/1e3)
    
    label.config(text="Total Cases: "+total_cases 
        + "\nTotal Deaths: " +todal_deaths 
        + "\nToday Cases: " +today_cases 
        + "\nToday Deaths: "+today_deaths
        + "\nToday Recovered: "+today_recovered)

    label2.config(text=date) 




canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Cororna Tracker App")


image1 = Image.open("/home/mayank/Downloads/fusion-medical-animation-rnr8D3FNUNY-unsplash.jpg")
newsize=(400,400)
image2=image1.resize(newsize)
test = ImageTk.PhotoImage(image2)

label1 = tk.Label(image=test)
label1.image = test

label1.pack(pady=20)



f=("poppins",15,"bold")

button = tk.Button(canvas, font=f,text="LOad",command= getcovidData)
button.pack(pady = 20)
 
label = tk.Label(canvas, font=f)
label.pack(pady=20)

label2=tk.Label(canvas, font=10)
label2.pack()







getcovidData()

canvas.mainloop()