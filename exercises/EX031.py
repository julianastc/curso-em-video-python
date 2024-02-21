trip_distance = int(input('Qual a distância da viagem? '))
is_trip_distance_below_limit = trip_distance <= 200


if is_trip_distance_below_limit:
    price = trip_distance * 0.5
else:
    price = trip_distance * 0.45


print(f'A passagem custará R${price:.2f}!')
