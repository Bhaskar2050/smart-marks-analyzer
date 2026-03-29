Science = int(input( "Enter your science Marks: " ))
Maths = int(input("Enter your Maths Marks: " ))
English = int(input("Enter your English Marks: " ))
Hindi = int(input("Enter your Hindi Marks: " ))
Social = int(input("Enter your Social Marks: " ))
IT = int(input("Enter your IT Marks: " ))

marks = [Science, Maths, English, Hindi, Social, IT]
top5 = sorted(marks, reverse=True)[:5]

subjects = {
    "Science": Science,
    "Maths": Maths,
    "English": English,
    "Hindi": Hindi,
    "Social": Social,
    "IT": IT
}

lowest_subject = min(subjects, key=subjects.get)



total = int(sum(top5)) 
percentage = (total / 500) * 100



print("Your Top 5 Marks are: ", top5)
print("Your Lowest Mark is: ", min(marks))
print("Your Highest Mark is: ", max(marks))
print("Your Total Marks is: ", total)
print("Your Percentage is: ", percentage)

if percentage >= 90:
    print("Congratulations! You got A grade.")
elif percentage >= 80:
    print("Congratulations! You got B grade.")
elif percentage >= 70:
    print("Congratulations! You got C grade.")
elif percentage >= 60:
    print("Congratulations! You got D grade.")
else:    print("Sorry! You got F grade.")

print("You need to work hard in", lowest_subject, ".")
