// Package darts provides a function to score a dart throw based on its cartesian coordinates with a 3-ring
// dartboard with a radius of 10 and scores of 10, 5 and 1 for the bullseye, middle and outer rings,
// respectively
package darts

// Score provides the integer score of a dart through on a radius 10 dart board with 3 rings of radius 1, 5
// and 10 and scores of 10, 5 and 1.
func Score(x, y float64) int {
	distance := x*x + y*y
	switch {
	case distance <= 1:
		return 10
	case distance <= 25:
		return 5
	case distance <= 100:
		return 1
	default:
		return 0
	}
}
