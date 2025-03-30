class File_Section:
    NUMBER_TASKS = 1
    CYCLE_TIME = 2
    ORDER_STRENGTH = 3
    TASK_TIMES = 4
    PRECEDENCE_RELATIONS = 5
    NUMBER_WORKER_CATEGORIES = 6
    WORKER_AVAILABILITY = 7
    WORKER_MODIFIERS = 8
    NUMBER_OF_STATIONS = 9
    STATION_CAPACITY = 10
    WORKER_AMOUNT_MODIFIERS = 11
    WORKER_BOUNDS = 12


def read_file(path):
    """
    Reads all data from an instance file with a specific format.

    Will return:
    - number of tasks
    - cycle time
    - order strength
    - task times
    - precedence relations
    - number of worker categories
    - worker availability
    - worker modifiers
    - number of stations
    - station capacity
    - worker amount modifiers
    - worker bounds
    """
    with open(path, "r") as file:
        number_of_tasks = None
        cycle_time = None
        order_strength = None
        task_times = []
        precedence_relations = []
        current_section = None
        number_of_worker_categories = None
        worker_availability = []
        worker_modifiers = []
        number_of_stations = None
        station_capacity = []
        worker_amount_modifiers = []
        worker_bounds = []

        lines = file.read().splitlines()
        for line in lines:
            if line.startswith("#"):
                continue
            elif line.startswith("<number of tasks>"):
                current_section = File_Section.NUMBER_TASKS
            elif line.startswith("<cycle time>"):
                current_section = File_Section.CYCLE_TIME
            elif line.startswith("<order strength>"):
                current_section = File_Section.ORDER_STRENGTH
            elif line.startswith("<task times>"):
                current_section = File_Section.TASK_TIMES
            elif line.startswith("<precedence relations>"):
                current_section = File_Section.PRECEDENCE_RELATIONS
            elif line.startswith("<number of worker categories>"):
                current_section = File_Section.NUMBER_WORKER_CATEGORIES
            elif line.startswith("<worker availability>"):
                current_section = File_Section.WORKER_AVAILABILITY
            elif line.startswith("<worker modifiers>"):
                current_section = File_Section.WORKER_MODIFIERS
            elif line.startswith("<number of stations>"):
                current_section = File_Section.NUMBER_OF_STATIONS
            elif line.startswith("<station capacity>"):
                current_section = File_Section.STATION_CAPACITY
            elif line.startswith("<worker amount modifiers>"):
                current_section = File_Section.WORKER_AMOUNT_MODIFIERS
            elif line.startswith("<worker bounds>"):
                current_section = File_Section.WORKER_BOUNDS
            elif line.startswith("<end>"):
                current_section = None
            else:
                if line == "":
                    continue
                elif current_section == File_Section.NUMBER_TASKS:
                    number_of_tasks = int(line)
                elif current_section == File_Section.CYCLE_TIME:
                    cycle_time = int(line)
                elif current_section == File_Section.ORDER_STRENGTH:
                    order_strength = float(line.replace(",", "."))
                elif current_section == File_Section.TASK_TIMES:
                    task_times.append(int(line.split(" ")[1]))
                elif current_section == File_Section.PRECEDENCE_RELATIONS:
                    precedence_relations.append([int(line.split(",")[0]), int(line.split(",")[1])])
                elif current_section == File_Section.NUMBER_WORKER_CATEGORIES:
                    number_of_worker_categories = int(line)
                elif current_section == File_Section.WORKER_AVAILABILITY:
                    _, number = line.split(":")
                    worker_availability.append(int(number))
                elif current_section == File_Section.WORKER_MODIFIERS:
                    workers = line.split(";")
                    task_modifiers = []
                    for worker in workers:
                        modifier = worker.split(":")[-1]
                        task_modifiers.append(float(modifier))
                    worker_modifiers.append(task_modifiers)
                elif current_section == File_Section.NUMBER_OF_STATIONS:
                    number_of_stations = int(line)
                elif current_section == File_Section.STATION_CAPACITY:
                    station_capacity.append(int(line.split(":", 1)[1]))
                elif current_section == File_Section.WORKER_AMOUNT_MODIFIERS:
                    worker_amounts = line.split(";")
                    task_modifier = []
                    for worker_amount in worker_amounts:
                        modifier = worker_amount.split(":")[-1]
                        task_modifier.append(float(modifier))

                    total_available_workers = sum(worker_availability)
                    while len(task_modifier) < total_available_workers:
                        task_modifier.append(float("inf"))

                    worker_amount_modifiers.append(task_modifier)
                elif current_section == File_Section.WORKER_BOUNDS:
                    lower, upper = line.split(":")[1].split(",")
                    worker_bounds.append([int(lower), int(upper)])

        return (
            number_of_tasks,
            cycle_time,
            order_strength,
            task_times,
            precedence_relations,
            number_of_worker_categories,
            worker_availability,
            worker_modifiers,
            number_of_stations,
            station_capacity,
            worker_amount_modifiers,
            worker_bounds,
        )
