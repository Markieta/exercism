package proverb

func Proverb(rhyme []string) []string {
	var proverb []string

	if len(rhyme) == 0 {
		return proverb
	}

	for i := 0; i < len(rhyme)-1; i++ {
		proverb = append(proverb, "For want of a "+rhyme[i]+" the "+rhyme[i+1]+" was lost.")
	}

	proverb = append(proverb, "And all for the want of a "+rhyme[0]+".")

	return proverb
}
