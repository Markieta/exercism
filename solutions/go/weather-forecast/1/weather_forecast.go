// Package weather provides the weather forecast.
package weather

// CurrentCondition describes the current weather condition.
var CurrentCondition string

// CurrentLocation is a location to forecast.
var CurrentLocation string

// Forecast gives the weather forecast for a location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
