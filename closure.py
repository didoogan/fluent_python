def make_averager():
    numbers = []

    def averages(new_value):
        numbers.append(new_value)
        return sum(numbers) / len(numbers)
    return averages

if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(20))
    print(avg(6))
