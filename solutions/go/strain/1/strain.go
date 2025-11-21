package strain

func Keep[T any](coll []T, predicate func(T) bool) []T {
	result := []T{}

	for _, v := range coll {
		if predicate(v) {
			result = append(result, v)
		}
	}

	return result
}

func Discard[T any](coll []T, predicate func(T) bool) []T {
	result := []T{}

	for _, v := range coll {
		if !predicate(v) {
			result = append(result, v)
		}
	}

	return result
}
