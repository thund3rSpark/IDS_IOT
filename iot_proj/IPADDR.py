import csv
import random
import argparse

def generate_random_ip():
    """Generate a random IPv4 address."""
    return f'{'192.168.2.20'}'
# return f"{random.randint(2022, 2024)}-{random.randint(1, 12)}-{random.randint(1, 28)} {random.randint(1,24)}:{random.randint(0,60 )}.{random.randint(0, 60)}"

def assign_ips_to_csv(input_file, output_file, column_name="IP"):
    """
    Assign random IPs to each row in a CSV.
    
    Args:
        input_file (str): Path to input CSV.
        output_file (str): Path to output CSV.
        column_name (str): Column to add/update with IPs.
    """
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + [column_name] if column_name not in reader.fieldnames else reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            row[column_name] = generate_random_ip()
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assign random IPs to CSV rows.")
    parser.add_argument("input", help="Input CSV file path")
    parser.add_argument("output", help="Output CSV file path")
    parser.add_argument("--column", default="IP", help="Column name for IPs (default: 'IP')")
    args = parser.parse_args()

    assign_ips_to_csv(args.input, args.output, args.column)
    print(f"✅ Random IPs assigned! Saved to: {args.output}")