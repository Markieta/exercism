package dna

import "errors"

type Histogram map[rune]int
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
// Returns an error if d contains an invalid nucleotide.
func (d DNA) Counts() (Histogram, error) {
	h := Histogram{'A': 0, 'C': 0, 'G': 0, 'T': 0}

	for _, c := range d {
		switch c {
		case 'A', 'C', 'G', 'T':
			h[c]++
		default:
			return h, errors.New("invalid")
		}
	}

	return h, nil
}
