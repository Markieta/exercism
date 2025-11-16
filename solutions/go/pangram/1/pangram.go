package pangram

import "strings"

func IsPangram(input string) bool {
	lower := strings.ToLower(input)

	for c := 'a'; c <= 'z'; c++ {
		if !strings.ContainsRune(lower, c) {
			return false
		}
	}

	return true
}
