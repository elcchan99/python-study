def recv_count():
    try:
        while True:
            n = yield  # Yield expression
            print("T-minus", n)
    except GeneratorExit:
        print("Kaboom!")
