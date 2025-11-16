package reverse

func Reverse(input string) string {
	rev := []rune(input)
	i, j := 0, len(rev)-1

	for i < j {
		rev[i], rev[j] = rev[j], rev[i]
		i++
		j--
	}

	return string(rev)
}
