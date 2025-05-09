from Staff import Staff


class Branch:

    def __init__(self, location, opening_time):
        self._location = location
        self._staff = []
        self._branch_opening_times = opening_time

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff
    
    def add_staff_member(self, staff: Staff):
        self._staff.append(staff)

    def get_opening_times(self):
        return self._branch_opening_times

    def change_opening_time(self, time: str):
        self._branch_opening_times = time
