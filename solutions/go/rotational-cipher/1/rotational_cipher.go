package rotationalcipher

func RotationalCipher(plain string, shiftKey int) string {
	rotated := ""
	for _, char := range plain {
		if char >= 'a' && char <= 'z' {
			rotated += string('a' + (char-'a'+rune(shiftKey))%26)
		} else if char >= 'A' && char <= 'Z' {
			rotated += string('A' + (char-'A'+rune(shiftKey))%26)
		} else {
			rotated += string(char)
		}
	}
	return rotated
}
