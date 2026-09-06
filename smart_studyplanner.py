def main():
    while True:
        print("\n====SMART STUDY PLANNER====")  
        print("1.Add a study session")
        print("2.View study sessions")
        print("3.Analyse study sessions")
        print("4.Exit")
        choice =input("Enter your choice: 1")
        if choice =="1":
            print("You selected Add a study session")
        elif choice =="2":
            print("You have selected View Study sessions")
        elif  choice =="3":
            print("You selected Analyse study sessions")
        elif choice =="4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.Please try again.")
            
            
main()  
import json

def main():
  try :
      with open("study_sessions.json,""r") as file:
          sessions = json.load(file)
       except FileNotFoundError:
           sessions = []           
        print("\n====SMART STUDY PLANNER====")  
        print("1.Add a study session")
        print("2.View study sessions")
        print("3.Analyse study sessions")
        print("4.Exit")
         choice =input("Enter your choice: 1")
         if choice =="1" :
            subject = input("Enter the subject: Python")
            date= input("Enter the date:20th August,2015")
            minutes =int(input("Enter study time in minutes:20 mintes"))
            session ={
            "subject":subject,
             "date" :date,
             "minutes":minutes
              }
              sessions.append(session)
              with open("study_sessions.json","w") as file:
                  json.dump(sessions,file,indent=4)
              print("study session added successfully!")
                   
         if choice =="1" :
            subject = input("Enter the subject:Mathematics")
            date = input("Enter date:6th August,2026") 
            hours=float(input("Enter hours studied:3hours"))
            print("Study session added successfully!")            
         elif coice =="2"
             print("\n ----STUDY SESSIONS----")
         if len(sessions) ==0:
             print("No study sessions found.")
         else:
             for session insessions:
             print("Subject": session[0])
             print("Date:", session[1])             
             print("Hours:",session[2])
             print("------------------")
         elif choice =="2":
              print("You selected view study sessions")
         elif choice =="3":
              print("You selected Analyse study sessions")          
         elif choice =="4":
              print("Goodbye!")
              break
              else:
                  print("Invalid choice.Please try again.")
main()                  
                  
                  
         if choice =="1" :
            subject = input("Enter the subject:Mathematics")
            date = input("Enter date:6th August,2026") 
            hours=float(input("Enter hours studied:3hours"))
            print("Study session added successfully!")            
         elif coice =="2"
             print("\n ----STUDY SESSIONS----")
         if len(sessions) ==0:
             print("No study sessions found.")
         else:
             for session insessions:
             print("Subject": session[0])
             print("Date:", session[1])             
             print("Hours:",session[2])
             print("------------------")
            total_hours = total_hours + session[2]
            
             
     