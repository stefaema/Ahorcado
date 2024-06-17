import pygame

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SoundMixer(metaclass=SingletonMeta):
    def __init__(self):
        # Inicializa solo si no se ha inicializado antes
        if not hasattr(self, 'sounds'):
            self.sounds = {
                "Stepping On Grass": pygame.mixer.Sound('Sounds/steppingOnGrass.wav'),
                "Button Click": pygame.mixer.Sound('Sounds/click_button.mp3'),
                "Good Choice!": pygame.mixer.Sound('Sounds/good_choice.wav'),
                "A King's Invitation": pygame.mixer.Sound("Music/aKingsInvititation.mp3"),
                "Executioner's Remorse": pygame.mixer.Sound("Music/executionersRemorse.mp3"),
                "Ouch Sound": pygame.mixer.Sound("Sounds/ouch.mp3"),
                "Hango's Salvation": pygame.mixer.Sound("Music/hangosSalvation.mp3"),
                "Hango's Demise": pygame.mixer.Sound("Music/hangosDemise.mp3"),
                "Dying Adventure": pygame.mixer.Sound("Music/dyingAdventure.mp3"),
            }
            for sound in self.sounds.values():
                sound.set_volume(0.2)
            self.sounds["Dying Adventure"].set_volume(0.1)
    def play(self, track):
        self.sounds[track].play()

    def stop(self, track):
        self.sounds[track].stop()

    def fade_out(self, track, time):
        self.sounds[track].fadeout(time)

if __name__ == "__main__":
    pygame.init()
    mixer1 = SoundMixer()
    mixer2 = SoundMixer()
    print(mixer1 is mixer2)  # Esto debería imprimir True, demostrando que ambas variables apuntan a la misma instancia.