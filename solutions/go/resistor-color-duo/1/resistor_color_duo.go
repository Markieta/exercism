package resistorcolorduo

import "strconv"

var resistance = map[string]string{
	"black":  "0",
	"brown":  "1",
	"red":    "2",
	"orange": "3",
	"yellow": "4",
	"green":  "5",
	"blue":   "6",
	"violet": "7",
	"grey":   "8",
	"white":  "9",
}

// Value should return the resistance value of a resistor with a given colors.
func Value(colors []string) int {
	result, _ := strconv.Atoi(resistance[colors[0]] + resistance[colors[1]])
	return result
}
