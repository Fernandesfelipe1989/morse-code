import sys

from utils import MORSE_CODE
from exceptions import InvalidInput


class StringToMorseCode:
    SPACE_BETWEEN_LETTERS = ' '
    SPACE_BETWEEN_WORDS = '/'

    def __init__(self, string: str):
        self.words = string
        morse = MORSE_CODE
        morse[' '] = self.SPACE_BETWEEN_WORDS
        self.LETTER_MORSE_CODE = morse

    @property
    def convert_to_morse(self) -> str:
        return self.SPACE_BETWEEN_LETTERS.join(
            [self.LETTER_MORSE_CODE.get(character.lower(), "") for character in self.words]
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise InvalidInput("It's necessary to pass a text message")
    _, words = sys.argv[0], sys.argv[1:]
    phrase = " ".join(words)

    print(StringToMorseCode(phrase).convert_to_morse)