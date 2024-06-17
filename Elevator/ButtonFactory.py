from button import HallButton,ElevatorButton
from abc import ABC,abstractmethod


class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self,identifier):
        pass

class HallButtonFactory(ButtonFactory):
    def create_button(self,sign):
        return HallButton(sign)

class ElevatorButtonFactory(ButtonFactory):
    def create_button(self,sign):
        return ElevatorButton(sign)

hall_button_factory=HallButtonFactory()
elevator_button_factory=ElevatorButtonFactory()

hallbutton=hall_button_factory.create_button("UP")
print(f"Hall Button: Sign = {hallbutton.get_buttonsign()}, Is Pressed = {hallbutton.is_pressed()}")

#so here factory design pattern added







