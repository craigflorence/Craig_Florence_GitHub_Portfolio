def is_prime(number):

    def is_int():
        u_c = number
        while type(u_c) != int:
            try:
                u_c = int(u_c)
            except ValueError:
                return "Please pass an integer."
