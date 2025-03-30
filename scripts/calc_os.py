import argparse

from parse import read_file


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Calculate Order Strength", description="Calculates the order strength of a .alb file"
    )
    parser.add_argument("file_path", type=str, help="Path to the .alb file")

    return parser.parse_args()


args = parse_args()
file_path = args.file_path

(
    number_of_tasks,
    cycle_time,
    order_strength,
    op_times,
    precedence_relations,
    number_of_worker_categories,
    worker_availability,
    worker_modifiers,
    number_of_stations,
    station_capacity,
    worker_amount_modifiers,
    worker_bounds,
) = read_file(file_path)

# We need to calculate all precedence relations, even transitive ones in order to find the order strength
# Store this as an array where each entry refers to a task and stores the tasks that depend on it
complete_precedence_relations = []
for i in range(number_of_tasks):
    complete_precedence_relations.append([])

# Account for zero and one-based indexing
for i, (t1, t2) in enumerate(precedence_relations):
    complete_precedence_relations[t1 - 1].append(t2 - 1)

# Check until it converges for transitive relations
something_changed = True
while something_changed:
    something_changed = False
    for i in range(number_of_tasks):
        for j in range(number_of_tasks):
            for k in range(number_of_tasks):
                if (
                    j in complete_precedence_relations[i]
                    and k in complete_precedence_relations[j]
                    and k not in complete_precedence_relations[i]
                ):
                    something_changed = True
                    complete_precedence_relations[i].append(k)


# Now calculate the actual order strength
total_precedence_relations = 0
for i in range(number_of_tasks):
    total_precedence_relations += len(complete_precedence_relations[i])

calculated_order_strength = total_precedence_relations / ((number_of_tasks * (number_of_tasks - 1)) / 2)

print(calculated_order_strength)
