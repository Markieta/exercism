package jedlik

import "strconv"

func (c *Car) Drive() {
	if c.battery >= c.batteryDrain {
		c.distance = c.distance + c.speed
		c.battery = c.battery - c.batteryDrain
	}
}

func (c *Car) DisplayDistance() string {
	return "Driven " + strconv.Itoa(c.distance) + " meters"
}

func (c *Car) DisplayBattery() string {
	return "Battery at " + strconv.Itoa(c.battery) + "%"
}

func (c *Car) CanFinish(trackDistance int) bool {
	moves := (trackDistance / c.speed)
	bConsumed := c.battery - (moves * c.batteryDrain)
	dDriven := moves * c.speed

	if bConsumed >= 0 && dDriven >= trackDistance {
		return true
	}

	return false
}
