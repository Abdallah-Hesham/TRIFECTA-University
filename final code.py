import sys
import tkinter as tk
from tkinter import messagebox, simpledialog

def main():
    def user_interface():
        choice = simpledialog.askinteger("Visitor Type","If you are seeking admission choose 1, if you are a student choose 2, if you need activities choose 3:")
        if choice == 1:
            addmission_managment()
        elif choice == 2:
            student_handling()
        elif choice == 3:
            handle_activities()
        else:
            messagebox.showerror("Error", "Invalid choice.")


    def addmission_managment():
        preadmission()
        nationality()
        english_exam()
        premajor()
        desires()
        PHD()

    def preadmission():
        certificate_type = simpledialog.askinteger("Certificate Type", " Enter your diploma : 1.Egyptian diploma, STEM 2.American diploma, CNISE, IGCSE, else")
        score = simpledialog.askinteger("Score", "Please enter your score:")
        discount = calculate_discount(score)
        messagebox.showinfo("Discount", discount)

    def calculate_discount(score):
        if 100 >= score >= 90:
            return "Great, you are eligible to apply to university. The value of your discount is 35%."
        elif 90 > score >= 85:
            return "Great, you are eligible to apply to university. The value of your discount is 25%."
        elif 85 > score >= 80:
            return "Great, you are eligible to apply to university. The value of your discount is 15%."
        elif 70 < score < 80:
            return "Sorry, there is no discounts for these score."
        elif score < 70 :
            messagebox.showinfo("oops", "sorry you are not eligible to apply to university.")
            sys.exit()


    def nationality():
        major = simpledialog.askinteger("Major", "Please choose the desired major: 1-CSAI 2-Science 3-Engineering 4-Business")
        nationality_choice = get_nationality()
        print_tuition_fees(major, nationality_choice)

    def get_nationality():
        return simpledialog.askinteger("Nationality", "Please enter the nationality of the student: 1.Egyptian 2.Foreign")

    def print_tuition_fees(major, nationality):
        fees = {
            (1, 1): "100000 L.E for no discount.\n65000 L.E for 35% discount.\n75000 L.E for 25% discount.\n85000 L.E for 15% discount.",
            (1, 2): "3000$ for no discount.\n1950$ for 35% discount.\n2250$ for 25% discount.\n2550$ for 15% discount.",
            (2, 1): "145000 L.E for no discount.\n94250 L.E for 35% discount.\n108750 L.E for 25% discount.\n123250 L.E for 15% discount.",
            (2, 2): "4000$ for no discount.\n2600$ for 30% discount.\n3000$ for 25% discount.\n3400$ for 15% discount.",
            (3, 1): "130000 L.E for no discount.\n84000 L.E for 35% discount.\n97500.2 L.E for 25% discount.\n110500 L.E for 15% discount.",
            (3, 2): "3200$ for no discount.\n1600$ for 50% discount.\n2080$ for 35% discount.\n2720$ for 15% discount.",
            (4, 1): "90000 L.E for no discount.\n45000 L.E for 50% discount.\n58000 L.E for 35% discount.\n76500 L.E for 15% discount.",
            (4, 2): "2250$ for no discount.\n1125$ for 50% discount.\n1462.5$ for 35% discount.\n1912.5$ for 15% discount.",
        }

        messagebox.showinfo("Tuition Fees", fees.get((major, nationality), "Invalid major or nationality."))

    def english_exam():
        has_exam = simpledialog.askinteger("English Exam", "Do you have IELTS or TOEFL? 1. Yes 2. No")
        if has_exam == 1:
            score = simpledialog.askfloat("Score", "What is your score?")
            if score >= 5.5:
                messagebox.showinfo("Exam Status", "You do not need to take the English entrance exam for Trifecta University.\nWait for an email to schedule a personal interview.")
            else:
                messagebox.showinfo("Exam Status", "You need to take the Trifecta English exam.\nWait for the university email about the date and method of payment.")
        else:
            messagebox.showinfo("Exam Status", "You need to take the Trifecta English exam.\nWait for the university email about the date and method of payment.")


    def premajor():
            major_choice = simpledialog.askinteger("Major Choice", "Please choose your major: 1.CSAI 2.SCI&ENG")
            if major_choice == 1:
                messagebox.showinfo("Info","You need to pass the English exam for Trifecta, which is held at the university.")
            else:
                study_type = simpledialog.askinteger("Study Type", "What is your type of study? 1. Math 2. Science")
                if study_type == 2:
                    messagebox.showinfo("Exams Required","You need to attend and pass the following exams: 1. Physics 2. Chemistry 3. Biology 4. MATH 1 5. Logical Thinking")
                else:
                    messagebox.showinfo("Exams Required","You need to attend and pass the following exams: 1. Physics 2. MATH 2 3. MATH 1 4. Logical Thinking")

    def desires():
        desire = simpledialog.askinteger("Desire", "Please enter your first desire: 1.CSAI 2.SCI&ENG")
        if desire == 1:
            messagebox.showinfo("Majors","Majors available in the College of Computer Science: Data science, Software, IT")
        else:
            engineering_choice = simpledialog.askinteger("Engineering Choice", "1. Science 2. Engineering")
            if engineering_choice == 1:
                messagebox.showinfo("Science Majors","Science majors: Biomedical, Physics and Earth, Materials, Nano")
            else:
                messagebox.showinfo("Engineering Majors","Engineering majors: Nano, Aerospace, Environmental, Renewable, Communications and Information")

    def PHD():
        phd_type = simpledialog.askinteger("PhD Type","Please enter your type of PhD required: 1. Science 2. ENG")
        if phd_type == 1:
            messagebox.showinfo("PhD Programs", "Trifecta University grants qualifications in the Department of Science: 1. NANO 2. Physics 3. Applied Mathematics")
        elif phd_type == 2:
            messagebox.showinfo("PhD Programs","Trifecta University grants qualifications in the Department of ENG: 1. Mathematics 2. Nano ENG 3. Environmental ENG")
        else:
            messagebox.showerror("Error", "Invalid choice.")


    def student_handling():
        identity = student_identity()
        if identity == 1:
            messagebox.showinfo("GPA", f"Your GPA = {gpa()}")
        elif identity == 2:
            major_handling()
        elif identity == 3:
            master()
        elif identity == 4:
            average()

    def student_identity():
        return simpledialog.askinteger("Student Identity", "If you need grades and GPA = 1, if you are in level 2, 3, 4 = 2, if graduate = 3, if you are official = 4:")

    def finding_grades():
        ID = simpledialog.askinteger("Student ID", "Enter your ID:")
        if ID is None:
            return 0
        try:
            with open('grade.txt', 'r') as file:
                for student in file:
                    grades = student.strip().split(",")
                    if grades[0].isnumeric() and int(grades[0]) == ID:
                        try:
                            grades_list = [int(grade) for grade in grades[1:]]
                            return sum(grades_list) / len(grades_list) if grades_list else 0
                        except ValueError:
                            messagebox.showerror("Error", "Invalid grades data in the file.")
                            return 0

        except FileNotFoundError:
            messagebox.showerror("Error", "grade.txt file not found.")
        messagebox.showinfo("Result", "Student ID not found.")
        return 0


    def gpa():
        score = finding_grades()

        if score == 0:
            return "F"
        if score == 4:
            return "A+"
        elif score >= 3.7:
            return "A"
        elif score >= 3.33:
            return "A-"
        elif score >= 3.0:
            return "B+"
        elif score >= 2.8:
            return "B"
        elif score >= 2.5:
            return "B-"
        elif score >= 2.2:
            return "C+"
        elif score >= 2:
            return "C"
        else:
            return "F"

    def major_handling():
        major = simpledialog.askinteger("Your Major","Enter number of your major: Bio=1 / Nano-tech=2 / CSAI=3 / SWD=4 / IT=5:")
        if major == 1:
            jop = simpledialog.askinteger("Job Preference", "Select if you like academic life=1 or industry=2:")
            if jop == 1:
                messagebox.showinfo("Career Options", "You could work as a research scientist.")
            elif jop == 2:
                messagebox.showinfo("Career Options", "You could work in a company of medicine.")
        elif major == 2:
            messagebox.showinfo("Career Options","You could work in the electronics and semiconductor industry or textiles and polymers industry.")
        elif major == 3:
            messagebox.showinfo("Career Options","You are lucky! You can work as:\n1. Machine Learning\n2. Data Science\n3. Algorithm Developer")
        elif major == 4:
            messagebox.showinfo("Career Options","You are lucky! You can work as:\n1. Software Development\n2. Web Developer")
        elif major == 5:
            messagebox.showinfo("Career Options", "You can work as:\n1. Cyber Security\n2. Networks")

    def master():
        graduate = simpledialog.askinteger("Graduate Status", "If you were a student in TRIFECTA select=1, not=2:")
        if graduate == 1:
            ask = simpledialog.askstring("GPA Status", "If your GPA=A enter yes, else enter no:")
            if ask.lower() == "yes":
                name = simpledialog.askstring("Full Name", "Please enter your third name:").split()
                email = f"g-{name[0]}.{name[2]}@TRIFECTA.edu.eg"
                messagebox.showinfo("Email", f"Your email is {email}")
                messagebox.showinfo("Master's Info", "The master's period requires from 1 to 3 years according to your efforts. We provide you with all the necessary resources.")
            else:
                messagebox.showinfo("Master's Info", "You can't pursue a master's degree at TRIFECTA.")
        elif graduate == 2:
            messagebox.showinfo("Master's Info", "Use your previous email; you can pursue a master's degree in your major.\nThe master's period requires from 1 to 3 years according to your efforts. We provide you with all the necessary resources.")

    def average():
        grades_students = simpledialog.askstring("Grades Input", "Hello professor: please enter the students' grades separated by spaces:").split()
        grades_students = [int(grade) for grade in grades_students]
        avg = sum(grades_students) / len(grades_students)
        messagebox.showinfo("Average Grades", f"The average of students' grades = {avg}")


    def handle_activities():
        number = simpledialog.askinteger("Activities", "If you need feedback on doctors select=1, if you need medical excuses select=2, if you need sports activities select=3, if you need statistics on sports select=4, if you need university dorms select=5:")
        number_function(number)

    def number_function(number):
        if number == 1:
            students = ["Abdelrahman", "Mohammed", "Amr", "Nour", "Khaled", "Anas", "Adam", "Omar"]
            feedback = feedback_of_doctors(students)
            messagebox.showinfo("Best Students", f"Best students are: {feedback['best']}")
            messagebox.showinfo("Worst Students", f"Worst students are: {feedback['worst']}")
        elif number == 2:
            students = ["Khaled", "Omar", "Amr"]
            excuses = medical_excuse(students)
            for student, excuse in excuses.items():
                messagebox.showinfo("Medical Excuses", f"{student}: {excuse}")
        elif number == 3:
            sports = simpledialog.askstring("Sports Inquiry", "What sport do you want to know details about? (separate with commas):").split(",")
            details = sports_activities(sports)
            for detail in details:
                messagebox.showinfo("Sport Details", detail)
        elif number == 4:
            sports = ["football", "basketball", "ping pong", "tennis", "swimming", "chess"]
            stats = statistics_on_sports(sports)
            messagebox.showinfo("Sports Statistics", f"The most practiced sport is {stats['most_practiced']}.\nThe least practiced sport is {stats['least_practiced']}.")
        elif number == 5:
            booking = simpledialog.askstring("Booking Inquiry", "Do you want to book a room in the university hotel? (yes/no):")
            university_dorms(booking)
        else:
            messagebox.showerror("Error", "Invalid input! Enter a number between 1 to 5.")


    def feedback_of_doctors(students):
        scores = []
        for student in students:
            score = simpledialog.askinteger("Doctor Feedback", f"Enter the score for {student}:")
            scores.append({'name': student, 'score': score})
        sorted_scores = sorted(scores, key=lambda student: student['score'], reverse=True)
        best_students = [student['name'] for student in sorted_scores[:4]]
        worst_students = [student['name'] for student in sorted_scores[-4:]]
        return {"best": best_students, "worst": worst_students}

    def medical_excuse(students):
        excuses = {}
        for student in students:
            question = simpledialog.askstring("Medical Excuse", f"Does {student} have a medical excuse for their absence? (yes/no):")
            if "yes" in question.lower():
                excuses[student] = "Excused and allowed to take the exam again."
            else:
                excuses[student] = "Not excused and not allowed to take the exam again."
        return excuses

    def sports_activities(sports):
        details = []
        sport_info = {
            "basketball": "Basketball is a team sport where two teams of five players compete to shoot a basketball through the opponent's hoop.",
            "football": "Football is played between two teams of eleven players with a spherical ball, and is the most popular sport worldwide.",
            "tennis": "Tennis is a racket sport played individually or in teams, where players hit a ball over a net.",
            "swimming": "Swimming is the self-propulsion of a person through water for recreation, sport, or exercise.",
            "chess": "Chess is a strategy board game for two players, aiming to capture the opponent's king.",
            "ping pong": "Ping pong is a sport where players hit a lightweight ball back and forth across a table divided by a net."
        }

        for sport in sports:
            details.append(
                sport_info.get(sport.strip().lower(), "I'm sorry, I don't have information about that sport."))
        return details

    def statistics_on_sports(sports):
        statistics = {}
        for sport in sports:
            participants = simpledialog.askinteger("Participants", f"Enter the number of participants for {sport}:")
            statistics[sport] = participants
        sorted_stats = sorted(statistics.items(), key=lambda item: item[1],)
        most_practiced = sorted_stats[-1][0]
        least_practiced = sorted_stats[0][0]
        return {"most_practiced": most_practiced, "least_practiced": least_practiced}

    def university_dorms(booking):
        if "yes" in booking.lower():
            messagebox.showinfo("Room Pricing", "- The price of the room is:\n- 100 L.E per night\n- 600 L.E per week\n- 2000 L.E per month\n- 9100 L.E per semester\n- DORMS offers the following services:\n- 24-hour front desk\n- Daily housekeeping\n- Free breakfast\n- Free Wi-Fi\n- On-site restaurant\n- Fitness center\n- Outdoor pool")
        else:
            messagebox.showinfo("Booking Info", "Thank you for considering the university hotel. Have a nice day.")



    user_interface()

if __name__ == "__main__":
    main()