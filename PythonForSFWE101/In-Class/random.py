def steps_to_miles(steps):
    Ex = ValueError()
    Ex.strerror = f'Exception: Negative step count entered.'
    try:
        if steps<0:
                print("error")
                raise Ex
    except:
        print("Exception: Negative step count entered.")
    return steps / 2000

if __name__ == '__main__':
        steps = int(input())
        print(f'{steps_to_miles(steps):.2f}')