class Vehicle:
    def __init__(self, make, model, color, fuelType,options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options
            
    def getMake(self):
        self.make = input('Please enter the vehicle make: ')
        

    def getModel(self):
        self.model = input('Please enter the vehicle model: ')
        

    def getColor(self):
        self.color = input('Please enter the vehicle color: ')
        

    def getFuelType(self):
        self.fuelType = input('Please enter the vehicle fuel type: ')
        

    def getOptions(self):
        optionslist = []
        print('nEnter Y or N for the following options')
        radio = input('Does your vehicle have a radio: ').lower()
        bluetooth = input('Does your vehicle have bluetooth: ').lower()
        cruise = input('Does your vehicle have cruise control: ').lower()
        window = input('Does your vehicle have power windows: ').lower()
        lock = input('Does your vehicle have power locks: ').lower()
        mirror = input('Does your vehicle have power mirrors: ').lower()
        rstart = input('Does your vehicle have remote start: ').lower()
        bcamera = input('Does your vehicle have a back up camera: ').lower()

        if radio == 'y':
            optionslist.append('Radio')
        if bluetooth == 'y':
            optionslist.append('Bluetooth')
        if cruise == 'y':
            optionslist.append('Cruise Control')
        if window == 'y':
            optionslist.append('Power Windows')
        if lock == 'y':
            optionslist.append('Power Locks')
        if mirror == 'y':
            optionslist.append('Power Mirrors')
        if rstart == 'y':
            optionslist.append('Remote Start')
        if bcamera == 'y':
            optionslist.append('Backup Camera')

        self.options = optionslist    


#creates instance
selection1 = Vehicle('n','n','n','n','n')


Vehicle.getMake(selection1)
Vehicle.getModel(selection1)
Vehicle.getColor(selection1)
Vehicle.getFuelType(selection1)
Vehicle.getOptions(selection1)

#makes sure options list has at least one option
if not selection1.options:
    print('nYou need to select at least one option.')
    Vehicle.getOptions(selection1)


print(f'Your vehicle is a {selection1.color} {selection1.make} {selection1.model} that runs on {selection1.fuelType}. The options are ' + ", ".join(selection1.options) +'.')



