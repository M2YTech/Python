class Player:
    def __init__(self, health, experience):
        self.health = health
        self.experience = experience
    
    @property
    def Power(self):
        power = self.health * self.experience
        return f"The player power is {power}"
    @Power.setter
    def Power(self, value):
        self.experience = value/self.health
        return f"The player experience is {self.experience}"

p = Player(100, 1.5)
print(p.Power)
p.Power = 200
print(p.experience)
