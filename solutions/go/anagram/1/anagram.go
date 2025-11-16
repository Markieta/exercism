package anagram

import (
	"sort"
	"strings"
)

func Detect(input string, candidates []string) []string {
	res := []string{}
	sortedInput := sortedString(strings.ToLower(input))
	for _, v := range candidates {
		if len(sortedInput) != len(v) ||
			strings.ToLower(input) == strings.ToLower(v) {
			continue
		}
		if sortedInput == sortedString(strings.ToLower(v)) {
			res = append(res, v)
		}
	}
	return res
}

func sortedString(input string) string {
	split := strings.Split(input, "")
	sort.Strings(split)
	sortedInput := strings.Join(split, "")
	return sortedInput
}
