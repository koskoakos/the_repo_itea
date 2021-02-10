import sys
import argparse

parser = argparse.ArgumentParser("Our program")

parser.add_argument('--input', '-i')
parser.add_argument('--output', '-o')
parser.add_argument('--column', '-c')
parser.add_argument('--desc', action='store_true')  # TODO: add sorting order


cmd_args = parser.parse_args()

in_file = cmd_args.input
out_file = cmd_args.output

if not in_file:
    in_file = input('Enter input file: ')

if not out_file:
    out_file = input('Enter output file: ')


employees = []
with open(in_file, 'r') as f_in:
    columns = f_in.readline().strip().split(',')

    for line in f_in:
        line = line.strip()
        if line:
            split_line = line.split(',')
            employee = {column: split_line[i] for i, column in enumerate(columns)}
            employees.append(employee)

sorted_employees = sorted(employees, key=lambda item: item.get(cmd_args.column, columns[0]))

with open(out_file, 'w') as f_out:
    f_out.write("%s\n" % ','.join(columns))
    for emp in sorted_employees:
        f_out.write("%s\n" % ','.join(emp.values()))
    print("Successfully written to %s" % out_file)

