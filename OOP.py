import random


class Menu:

    def __init__(self):
        self.menu = []
        self.questions = []
        self.choose = ""
        self.score=0
    def addMenu(self, *args):
        if len(args) == 4:
            self.menu.extend(args)

    def show_score(self):
        print("\t\t\tYour score is: " + str(self.score)+"\n")

    def showMenu(self):
        count = 1
        for item in self.menu:
            menu = "\t\t\t"+str(count) + ". " + item
            count += 1
            print(menu)

    def select(self, usr=None):
        selection = int(input("Select one option: \n"))
        print("\t\t\tSiz " + str(self.menu[selection - 1]) + "ni tanladingiz")
        if selection == 1:
            histry=[]
            file=open("history.txt","r")
            for i in file:
                histry.append(i)
            if len(histry)==0:
                usr = User()
                usr.set_name()
                usr.set_age()
                for j in range(1, 4):
                    for i in range(4):


                        qvst = Quiz_maker()
                        qvst.read_question(j)
                        qvst.show_question(i,j)
                        qvst.show_answer(i)
                        self.choose = input("Select key: ")
                        b = qvst.chek_answer(self.choose, i)
                        if b:
                            if self.score<=300:
                                self.score+=100
                            elif self.score>300:
                                self.score+=200
                            elif self.score>=1200:
                                self.score+=300
                        m=Menu
                        m.show_score(self)
                        usr.history(self.score)
                        if b == False: break
            else:
                for j in range(1, 4):
                    for i in range(4):


                        qvst = Quiz_maker()
                        qvst.read_question(j)
                        qvst.show_question(i,j)
                        qvst.show_answer(i)
                        self.choose = input("Select key: ")
                        b = qvst.chek_answer(self.choose, i)
                        if b:
                            if self.score<=300:
                                self.score+=100
                            elif self.score>300:
                                self.score+=200
                            elif self.score>=1200:
                                self.score+=300
                        m=Menu
                        m.show_score(self)
                        usr=User()
                        usr.history(self.score)
                        if b == False: break

        elif selection == 3:
            hst=User()
            hst.show_last_score()
        elif selection == 4:
            quit(1)
        elif selection == 2:
            f=open("history.txt","w")
            f.write("")
            f.close()



class Quiz_maker:
    def __init__(self,*args):

        if len(args)==0:
            self.question=[]
            self.answer = []
            self.true_answer=[]



    def read_question(self,mode):

        letters = ['a', 'b', 'c', 'd']

        file = open("questions.txt", "r")

        for question in (file):
            answer1 = (question.split("$")[2].split(":"))

            question_level = question.split("$")[0]

            question3 = question.split("$")[1]

            if question_level == str(mode):
                random.shuffle(answer1)
                if (len(question3)>1):

                    self.question.append(question3)

                for i in range(len(answer1)):
                    self.answer.append([])
                    letter = letters[i]
                    if "#" in answer1[i]:
                        self.true_answer.append(letter+answer1[i])

                    self.answer[i].append (letter + ") " + answer1[i].lstrip("#").strip())
                answer=answer1[:4]


        file.close()
    def show_answer(self,j):
        self.answer=self.answer[:4]
        for i in self.answer:
            print(i[j])
    def show_question(self,i,j):
        if j==1:
            print("\t\t\tBoshlangich to`rtta oson savolning "+str(i+1)+" chisi"+ "\n")
        elif j==2:
            print("\t\t\tO`rtacha qiyinlikdagi to`rtta savolning "+str(i+1)+" chisi"+ "\n")
        elif j==3:
            print("\t\t\tQiyin bo`lgan to`rtta savolning "+str(i+1)+" chisi"+ "\n")
        print("\t\t\tDiqqat savol!----> "+self.question[i]+"\n")

    def show_true_answer(self):
        print(self.true_answer)

    def chek_answer(self,key,index):




        if key == self.true_answer[index].split("#")[0]:



            print("\t\t\tJavobingiz to`g`ri..\n")



            return True
        else:
            print("\t\t\tSiz noto`g`ri javobni tanladingiz!\n")
            exit(1)
            return False



class User:
    def __init__(self):
        self.user_name=""
        self.user_age=0
        self.user_id = ""
        numbers="1234567890"

        for i in range(5):
            self.user_id+=random.choice(numbers)


    def set_name(self):
        name=input("Your name:")
        self.user_name=name

    def set_age(self):
        age=input("Age: ")
        self.user_age=age
    def history(self,score):
        file = open("history.txt", "w")


        file.write(self.user_id+"#"+self.user_name+"#"+str(self.user_age)+"#"+str(score))
        file.close()
    def show_last_score(self):
        file=open("history.txt","r")
        for i in file:
            score=i.split("#")[3]
            print("Your last score: "+score)