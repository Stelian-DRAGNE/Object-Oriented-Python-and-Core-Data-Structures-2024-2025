
class NationalitateNecunoascuta(Exception):
    def __init__(self, *args):
        super().__init__("Nationalitatea trebuie sa fie de forma RO sau EN sau HU.")


if __name__ == "__main__":
    raise NationalitateNecunoascuta()