from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function


# Calculate the shipping price based on from and to coordinates and the type of shipping.
# Shipping_type is overnight by default.
"""
Calculating the shipping cost by.
"""
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    # Unpack from_coords and to_coords tuples
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords

    # Way 1 to called get_distance() - manual way.
    # distance = get_distance(from_lat, from_long, to_lat, to_long)

    # Way 2 to call get_distance() - not unpacking from_coords and to_coords
    distance = get_distance(*from_coords, *to_coords)

    # Get shipping_rate.
    shipping_rate = SHIPPING_PRICES.get(shipping_type)

    # Calculate price.
    price = distance * shipping_rate

    return format_price(price)


# Test the calculate_shipping_cost function by calling
test_function(calculate_shipping_cost)

"""
Determine the best driver by calculating the cost for the drivers to fulfill orders.
This can be achieved by:
    Looping through the drivers and
        calculate driving time by dividing the distance travelled by driving speed.
        driver price by multiplying driver salary with driving time.
        if the cheapest_driver is None which means this is the first driver:
            Set cheapest_driver and price.
        otherwise,
            Update cheapest_driver and price.
"""


def calculate_driver_cost(distance, *drivers, cheapest_driver=None, cheapest_driver_price=None):
    for driver in drivers:
        driver_time = distance / driver.speed
        price_for_driver = driver.salary * driver_time

        # if cheapest driver is not found yet which mean this is the first driver we’ve looked at.
        if cheapest_driver is None:
            # store first driver and its price as the cheapest and
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver

        # Otherwise, if the current driver price is less than the stored cheapest driver.
        # Then, update the cheapest driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver

    return cheapest_driver_price, cheapest_driver


# Test the function by calling
test_function(calculate_driver_cost)


# region The Nile Exclusive
"""
Calculate the saving money iterating the trips done and
    This function will be passed a number of Trip IDs with corresponding trip information as arguments, 
    so let’s just take any keyword arguments passed into it. Store them all as trips!
    Calculating the trip revenue by subtracting trip cost and driver cost.
    Increase total money by trip revenue
"""


def calculate_money_made(**trips):
    # money count
    total_money_made = 0
    for trip_id, trip in trips.items():
        trip_revenue = trip.cost - trip.driver.cost
        total_money_made += trip_revenue

    return total_money_made

test_function(calculate_money_made)
# endregion
