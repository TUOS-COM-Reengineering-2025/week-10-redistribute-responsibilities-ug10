class Customer:
    def __init__(self, name: str, address: str, phone_number: str):
        self._name = name
        self._address = address
        self._phone_number = phone_number

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name
    
    def set_address(self, new_address: str):
        self._address = new_address
        
    def get_address(self) -> str:
        return self._address

    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number
        
    def get_phone_number(self) -> str:
        return self._phone_number
    
    

