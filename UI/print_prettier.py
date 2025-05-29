def pretty_print_df(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Obtener nombre de la función
        # Obtener nombre de la clase si es método de instancia
        if args and hasattr(args[0], '__class__'):
            class_name = args[0].__class__.__name__
            header = f"{class_name}"

        # Convertir el DataFrame a string para medirlo
        result_str = result.to_string() if hasattr(result, "to_string") else str(result)

        # Obtener ancho máximo de las líneas
        lines = result_str.split('\n')
        max_width = max(len(line) for line in lines)

        # Imprimir título centrado con bordes
        print("\n" + header.center(max_width + 6, '-')) # type: ignore

        # Imprimir marco arriba
        print("-" * (max_width + 4))

        # Imprimir líneas con bordes laterales
        for line in lines:
            print(f"|| {line.ljust(max_width)} ||")

        # Imprimir marco abajo
        print("-" * (max_width + 4) + "\n")

        return result
    return wrapper
