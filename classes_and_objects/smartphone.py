class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        # Turn the the phone on if it's off and vice versa
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory):
        if self.is_on: # Installs an app if the phone is on
            if app_memory <= self.memory: # If there is enough memory
                self.apps.append(app)
                self.memory -= app_memory
                return f'Installing {app}'

            return f'Not enough memory to install {app}' # If there is not enough memory

        return f'Turn on your phone to install {app}' # If the phone is off

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())


