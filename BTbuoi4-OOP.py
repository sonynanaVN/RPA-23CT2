class Pet:#class là một khuôn mẫu để tạo ra các đối tượng, nó định nghĩa các thuộc tính và phương thức mà các đối tượng của lớp đó sẽ có.
    def __init__(self, name, agem,currenthealt,status,emotion):#__init__ là một phương thức đặc biệt trong Python được gọi là constructor. Nó được tự động gọi khi một đối tượng mới của lớp được tạo ra và thường được sử dụng để khởi tạo các thuộc tính của đối tượng.
        self.name = name
        self.agem = agem
        self.currenthealt = currenthealt
        self.status = status
        self.emotion = emotion
    def eat(self):#phương thức là một hàm được định nghĩa bên trong một lớp và có thể được gọi trên các đối tượng của lớp đó. Nó thường được sử dụng để thực hiện các hành động hoặc thao tác liên quan đến đối tượng.
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def play(self):
        print(f"{self.name} is playing.")
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.agem} years")
        print(f"Current Health: {self.currenthealt}")
        print(f"Status: {self.status}")
        print(f"Emotion: {self.emotion}")
    def update_health(self, new_health):
        self.currenthealt = new_health
        print(f"{self.name}'s health has been updated to: {self.currenthealt}")
#tạo đối tượng Pet
Pet1 = Pet("Tom", 3, "Good", "Happy", "Playful")
Pet2 = Pet("Jerry", 2, "Fair", "Sad", "Sleepy")
Pet3 = Pet("Spike", 5, "Excellent", "Angry", "Energetic")
#sử dụng phương thức của đối tượng
Pet1.show_info()
Pet2.eat()
Pet3.sleep()
Pet3.play()
Pet2.currenthealt = "Poor"
Pet2.update_health("Good")