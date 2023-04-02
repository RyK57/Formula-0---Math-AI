import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Subodhayam!")

    elif hour >= 12 and hour < 18:
        speak("some sun above ")

    else:
        speak("Get some of that workout!")

    speak("Yo i am Zeera , how may i help ya!")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone()as source:
        print("listening...")
        
        r.listen(source,timeout=2)
        audio = r.listen(source) 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)

        print("Yo wait repeat that..")
        return "None"

    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rithviks.ryk57@gmail.com','opm>naruto')
    server.sendmail('rithviks.ryk57@gmail.com', to,content)
    server.close() 

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'tell me' in query:
            speak("I'm a look it up on Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Well in wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open chezuba' in query:
            webbrowser.open("chezuba.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open zorro anime' in query:
            webbrowser.open("zoro.to")

        elif 'open slope io' in query:
            webbrowser.open("slope.io")

        elif 'open manga reader' in query:
            webbrowser.open("mangareder.to")

        elif 'open adobe express' in query:
            webbrowser.open("adobeexpress.com")

        # elif 'sushi' or 'chat' in query:
        #     webbrowser.open("chat.openai.com/chat")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Well  we are rocking at {strTime} right now')
        
        elif 'mathematics' in query:
            speak("Check printed message for list of mathematical formulas I know. The formula will be said, as well as typed in the terminal")
            area_list_formula=['Area of a Square', 'Area of a Rectangle', 'Area of a Triangle' , 'Area of a Rhombus', 'Area of a Trapezoid', 'Area of a Regular Polygon', 'Area of a Circle' , 'Lateral Surface Area of a Cone' , 'Surface Area of a Sphere']
            vol_list_formula = ['Volume of a Cube', 'Volume of a Cuboid', 'Volume of a Regular Prism', 'Volume of a Cylinder', 'Volume of a Cone', 'Volume of a Sphere']
            print("Formulas for Area:")
            print(*area_list_formula,sep = "\n")
            print("Formulas for Volume:")
            print(*vol_list_formula,sep = "\n")3
            speak("These are the formulas I know, let me know which one you want to use")

            query = takeCommand().lower()

            def speak(audio):
                engine.say(audio)
                engine.runAndWait()
               
            if 'square' in query :
                    speak('area of square is its length sqaured')
                    print('A= l^2')

            elif 'rectangle' in query:
                    speak('area of rectangle is its width multiplied by its height')
                    print('A=w*h')

            elif 'triangle' in query :
                    speak('area of trinagle is its breadth and height multipled and then divided by 2')
                    print("A=b*h/2")

            elif 'rhombus' in query :
                    speak("area of rhombus is its large and small diagonal multipled and then divided by 2")
                    print("A=D*D/2")

            elif 'trapezoid' in query :
                    speak("area of trapezoid is its large and small side added , then divided by 2 and then multipled by its height")
                    print('A=(B+b)/2*h')
                
            elif 'regular' in query:
                    speak("area of polygon is its perimeter halved and then mutplied by the apothem")
                    print("A=P/2*a")

            elif 'circle' in query:
                    speak("area of circle is the value of PI multipled with its radius sqaured")
                    print("A=π*r^2")

            elif 'cone' in query:
                    speak("lateral surface area of a cone is value of pi multipled with radius and its slant height")
                    print('A=π*r*s')

            elif 'sphere' in query:
                    speak("the surface area of sphere is four multiplied by value of pi and the radius squared")
                    print("A=4*π*r^2")
                     
            elif 'cube' in query :
                    speak('a cube volume is its side length to the power of 3')
                    print('s*s*s / s^3')

            elif 'Cuboid' in query:
                    speak('El multipled bee multipled hech . A parellelepiped, or a cuboids volume is its length , width and height multiplied')
                    print('l*b*h')

            elif 'Regular' in query :
                    speak('A regular prisms breadth multiplied by its height is its volume ')
                    print("V=b*h")

            elif 'Cylinder' in query :
                    speak("To calculate volume of cylinder, multiply its radius sqaured with the pi value and then the product of it multiplied with its height")
                    print("V=π*r^2*r*h")

            elif 'Cone' in query :
                    speak("A cone's volume is its breadth multiplied by one by 3 multiplied by height")
                    print('1/3*b*h')
                
            elif 'Sphere' in query:
                    speak("A sphere volume is calculated with its radius cubed multiplied by pi value multiplied by 4 divided by 3")
                    print("4/3*π*r^3")
        
        
                    
            elif 'stop' in query:
                    break

            else: 
                speak('error')
                print('error')
                
    
    
        elif'email to ricky'in query:
            try:
                speak('what should i say')
                content=takeCommand()
                to='rithvik.sabnekar@akahyd.org'
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e : 
                print('e')
                speak("not able to send man")

        elif 'exit' in query:
         break

        else:
            speak("error")
            continue

# listmath=["Factors of numbers,"
#               " Integers, "
#               "Number-operations ,"
#                "Prime-Numbers, "
#                 "Prime-factors ,"
#                  "Greatest-common-factor, "
#                   "lowest-common-multiple ,"
#                    "Recurring-decimals ,"
#                     "Number-Lines, "
#                      'inequalities, '    
#                      'Ratios, '
#                       'Exponents and powers, '
#                       'Squares-and-square roots ,'
#                        ' Time zones,'
#                        'clocks,'
#                         'Absolute values,'
#                          'Representing And Solving inequalities,'
#                           'Irrational numbers,'
#                             'Surds,roots and radicals,'
#                               'scientific notation,'
#                               'Laws of exponents,'  
#                                'integer and negative exponents,'
#                                 'Number system notation,'
#                                 'Direct and inverse proportion,']
#         print(listmath)
#             if'Factors'in query :
#                   speak("Factors are the numbers that can divide a number exactly. Hence, after division, there is no remainder left. Example - 1,2,3,6,12 are factors of 12")
#                   print("Factors are the numbers that can divide a number exactly. Hence, after division, there is no remainder left. Example - 1,2,3,6,12 are factors of 12")    
#             elif'Integers' in query :
#                   speak("In Maths, integers are the numbers which can be positive, negative or zero, but cannot be a fraction. Example-positive and negativ e numbers like 1 , -9 ")
#                   print("In Maths, integers are the numbers which can be positive, negative or zero, but cannot be a fraction. Example-positive and negativ e numbers like 1 , -9 ")
#               elif'Number operations' in query:
#                   speak()
#               elif'Prime numbers' in query:
#                   speak()
#               elif'Greatest common factor' in query :
#                   speak()
#               elif'lowest common multiple' in query:
#                  speak()
#               elif'recurring decimals' in query:
#                   speak()
#               elif'number lines' in query :
#                   speak()
#               elif'inequalities' in query:
#                   speak()
#               elif'ratios' in query:
#                   speak()
#               elif'exponents and powers' in query :
#                   speak()
#               elif'squares' or 'square roots' in query:
#                   speak()
#               elif'Time zones' in query:
#                   speak()
#               elif'clocks' in query :
#                   speak()
#               elif'Absolute values' in query:
#                  speak()
#               elif'solving inequalities' in query:
#                   speak()
#               elif'irrational numbers' in query :
#                   speak()
#               elif'surds' or 'roots' or 'radicals' in query:
#                   speak()
#               elif'scientifc notation' in query:
#                   speak()
#               elif'Laws' in query :
#                   speak()
#               elif'integer and negative exponents' in query:
#                   speak()
#               elif'number system notation' in query:
#                   speak()
#               elif'direct proportion' or 'inverse proportion' in query :
#                   speak()
#               else :
#                   speak("didnt get u bruh , repeat")





 
