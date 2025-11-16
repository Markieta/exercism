package triangle

type Kind int

const (
	NaT Kind = iota // not a triangle
	Equ             // equilateral
	Iso             // isosceles
	Sca             // scalene
)

func KindFromSides(a, b, c float64) Kind {
	if !(a+b >= c && b+c >= a && a+c >= b) || a == 0 || b == 0 || c == 0 {
		return NaT
	} else if a == b && b == c {
		return Equ
	} else if a == b || a == c || b == c {
		return Iso
	}

	return Sca
}
