from sandstone import sandstone

class tomdemo1(sandstone.application):
    def __init__(self, area, room):
        self.roomFile = "tomdemo1/tomdemo1Rooms.json"
        self.objectFile = "tomdemo1/tomdemo1Objects.json"

        super().__init__(area, room, self.roomFile, self.objectFile, saveFile="save.json")

tomdemo1(1, 1).run()